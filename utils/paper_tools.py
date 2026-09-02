"""Deterministic document utilities that can be exposed to an Agent.

The functions in this module deliberately do not call an LLM.  They turn the
Markdown emitted by MinerU into stable, addressable sections and provide a
small lexical evidence retriever.  An Agent can call these functions before
asking a model to synthesize an answer.
"""

from __future__ import annotations

import hashlib
import math
import re
from collections import Counter
from pathlib import Path
from .evidence_graph import (
    build_document_graph,
    search_spans,
    split_chunks,
    terms as graph_terms,
)

from typing import Any, Iterable


HEADING_RE = re.compile(r"(?m)^(#{1,6})[ \t]+(.+?)\s*$")
WORD_RE = re.compile(r"[\w\u4e00-\u9fff]+", re.UNICODE)
ENGLISH_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_-]*")
CJK_TOKEN_RE = re.compile(r"[\u3400-\u9fff]+")

SEARCH_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "data",
    "for",
    "from",
    "how",
    "in",
    "is",
    "key",
    "main",
    "of",
    "on",
    "or",
    "paper",
    "the",
    "to",
    "what",
    "with",
    "什么",
    "如何",
    "论文",
    "重点",
}

DEPRIORITIZED_HEADING_RE = re.compile(
    r"data availability|online content|references?|bibliography|additional information|"
    r"acknowledgements?|author contributions?|competing interests?",
    re.IGNORECASE,
)
METHOD_ONLY_HEADING_RE = re.compile(r"test$|experimental details|characterizations?|methods?$", re.IGNORECASE)

INTENT_HEADING_PATTERNS: dict[str, re.Pattern[str]] = {
    "objective": re.compile(r"abstract|introduction|article|conclusions?|summary", re.IGNORECASE),
    "methods": re.compile(
        r"methods?|materials?|experimental|prepar|fabricat|synthesi|processing|"
        r"printing|coating|curing|peeling|characterization|simulation",
        re.IGNORECASE,
    ),
    "sample_preparation": re.compile(
        r"methods?|materials?|prepar|fabricat|synthesi|processing|printing|coating|"
        r"curing|peeling|substrate|polymer",
        re.IGNORECASE,
    ),
    "physical_mechanism": re.compile(
        r"optical|mechanism|simulation|principles?|article|field|colour|tunability",
        re.IGNORECASE,
    ),
    "key_results": re.compile(
        r"results?|conclusions?|performance|stability|principles?|tunability|article",
        re.IGNORECASE,
    ),
    "limitations": re.compile(
        r"limitations?|discussion|performance|stability|conclusions?|article",
        re.IGNORECASE,
    ),
}


def source_fingerprint(pdf_path: str | Path) -> str:
    """Return a stable cache namespace for a file path and its current stat."""

    path = Path(pdf_path).expanduser().resolve()
    stat = path.stat()
    payload = f"{path}\0{stat.st_size}\0{stat.st_mtime_ns}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:16]


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _normalise_title(title: str) -> str:
    return re.sub(r"\s+", " ", title.strip()).rstrip("†")


def split_markdown_sections(markdown: str, max_chars: int = 6000) -> list[dict[str, Any]]:
    """Split Markdown into raw chunks enriched with semantic ownership."""
    return split_chunks(markdown, max_chars=max_chars)


def _terms(value: str) -> list[str]:
    """Backwards-compatible tokenizer wrapper."""
    return graph_terms(value)


def search_markdown(
    markdown_or_path: str | Path,
    query: str,
    top_k: int = 5,
    *,
    intent: str | None = None,
) -> list[dict[str, Any]]:
    """Find exact supporting passages with chunk-compatible metadata."""
    return search_spans(
        markdown_or_path,
        query,
        top_k=top_k,
        intent=intent,
    )


def document_manifest(
    markdown: str,
    *,
    pdf_path: str | Path | None = None,
    markdown_path: str | Path | None = None,
    chunk_chars: int = 6000,
) -> dict[str, Any]:
    """Build a raw-chunk plus atomic-span manifest for an Agent or indexer."""
    manifest = build_document_graph(markdown, max_chars=chunk_chars)
    if pdf_path is not None:
        manifest["pdf_path"] = str(Path(pdf_path).expanduser().resolve())
        try:
            manifest["source_id"] = source_fingerprint(pdf_path)
        except FileNotFoundError:
            manifest["source_id"] = None
    if markdown_path is not None:
        manifest["markdown_path"] = str(Path(markdown_path).expanduser().resolve())
    return manifest


def section_index(markdown: str, chunk_chars: int = 6000) -> list[dict[str, Any]]:
    """Return raw and semantic heading metadata for the document outline."""
    return [
        {
            key: chunk[key]
            for key in (
                "chunk_id", "heading", "raw_heading", "semantic_heading",
                "heading_kind", "empty_node", "level", "part", "line_start",
                "line_end", "modalities", "figure_parents", "semantic_owner_type",
            )
        }
        for chunk in build_document_graph(markdown, max_chars=chunk_chars)["chunks"]
    ]

