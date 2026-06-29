import os

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app import models
from app.schemas import MemoryCreate
from app.keyword_extractor import extract_keywords
from app.graph import build_relationships

app = FastAPI()

os.makedirs("data", exist_ok=True)
Base.metadata.create_all(bind=engine)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


# ---------------- DB Dependency ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- UI ----------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


# ---------------- Save Memory ----------------
@app.post("/memory")
def create_memory(payload: MemoryCreate, db: Session = Depends(get_db)):

    # 1. Save memory text
    memory = models.Memory(text=payload.text)
    db.add(memory)
    db.commit()
    db.refresh(memory)

    # 2. Extract keywords
    keywords = extract_keywords(payload.text)

    # 3. Save keywords
    for kw in keywords:
        db.add(models.Keyword(memory_id=memory.id, keyword=kw))

    # 4. Create relationships
    edges = build_relationships(keywords)

    for a, b in edges:
        db.add(models.Relationship(keyword1=a, keyword2=b))

    db.commit()

    return {
        "message": "Memory saved",
        "memory_id": memory.id,
        "keywords": keywords
    }


# ---------------- Get All Memories ----------------
@app.get("/memories")
def get_memories(db: Session = Depends(get_db)):
    return db.query(models.Memory).all()


# ---------------- Search ----------------
@app.get("/search")
def search(keyword: str, db: Session = Depends(get_db)):

    results = (
        db.query(models.Memory)
        .join(models.Keyword, models.Memory.id == models.Keyword.memory_id)
        .filter(models.Keyword.keyword.ilike(f"%{keyword}%"))
        .all()
    )

    return results


# ---------------- Graph API ----------------
@app.get("/graph")
def graph(db: Session = Depends(get_db)):

    relationships = db.query(models.Relationship).all()

    nodes = set()
    edges = []

    for r in relationships:
        nodes.add(r.keyword1)
        nodes.add(r.keyword2)
        edges.append({"from": r.keyword1, "to": r.keyword2})

    return {
        "nodes": list(nodes),
        "edges": edges
    }