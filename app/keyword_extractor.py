import re

STOPWORDS = {
    "i", "the", "a", "an", "to", "and", "is", "was", "were",
    "today", "tomorrow", "yesterday", "also", "want", "learned", "practiced"
}

def extract_keywords(text: str):
    words = re.findall(r"[A-Za-z]+", text)

    keywords = []
    for w in words:
        w_lower = w.lower()
        if len(w_lower) > 2 and w_lower not in STOPWORDS:
            keywords.append(w)

    # remove duplicates while preserving order
    seen = set()
    result = []
    for k in keywords:
        if k.lower() not in seen:
            result.append(k)
            seen.add(k.lower())

    return result