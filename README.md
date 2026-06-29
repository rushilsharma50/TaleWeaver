# TaleWeaver: Operational Memory Graph Diary (V1 Core)

TaleWeaver is an engineering-first personal knowledge management platform that transforms raw daily text journals into an interactive semantic graph network. Instead of storing entries as isolated chronological blocks of text, TaleWeaver acts as an information retrieval pipeline: automatically parsing daily logs, extracting distinct structural entities, validating schema transformations, and mapping concept intersections locally. 

Built using a modular, highly decoupled architecture, this project serves as a robust foundational ecosystem for advanced downstream integrations like local RAG (Retrieval-Augmented Generation), vector embeddings, and autonomous agent memory layers.

![System Interface Dashboard](Screenshot (1760).png)

## 🚀 Key Features

* **Schema-Validated Ingestion:** Strictly managed request payloads built with Pydantic models to verify structural consistency.
* **Asynchronous Data Pipeline:** Fast, reliable REST API endpoints engineered with FastAPI to decouple memory ingestion from analytical rendering.
* **Local Deterministic Text Parsing:** Efficient, zero-overhead regex-driven extraction layer engineered to process contextual entities while actively scrubbing common noise floor stopwords.
* **Relational Mapping of Graph Invariants:** Mathematical translation of keyword pairings into deterministic bidirectional structural graphs using structural databases.
* **Interactive Physics-Driven Visualizer:** High-performance, zoomable, draggable network diagram built natively with Vis.js inside a clean tailwind-styled presentation panel.

---

## 🛠️ System Architecture & Folder Layout

TaleWeaver is structured according to clean code principles, ensuring that each software component maintains a single, distinct responsibility:

```text
memory-graph-diary/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # FastApi initialization, routing tables, and HTTP controllers
│   ├── models.py              # Declarative SQLAlchemy ORM database schemas
│   ├── database.py            # SQLite engine configuration and session lifecycles
│   ├── schemas.py             # Pydantic validation boundaries for API requests/responses
│   ├── graph.py               # Combinatoric logic for generating node/edge collections
│   └── keyword_extractor.py   # Deterministic parsing engine for token isolation
│
├── data/
│   └── diary.db               # SQLite database file housing transaction data
│
├── static/
│   └── style.css              # Custom layout properties
│
├── templates/
│   └── index.html             # UI presentation layer loading interactive Canvas views
│
└── requirements.txt           # Explicit tracking of production ecosystem dependencies
