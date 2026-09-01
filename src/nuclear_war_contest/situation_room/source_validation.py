"""Fail-closed validation for U.S. Charter source registers."""

from __future__ import annotations

from typing import Any

from .source_reference_validation import validate_source_references
from .validation import (
    fail,
    reject_officeholder_fields,
    require_date,
    require_records,
    require_text,
    require_text_list,
)

REGISTER_FIELDS = {
    "schema_version",
    "register_id",
    "register_version",
    "status",
    "snapshot_date",
    "sources",
    "facts",
    "inferences",
    "gaps",
}
SOURCE_FIELDS = {
    "source_id",
    "issuing_institution",
    "public_title",
    "canonical_url",
    "publication_date",
    "effective_date",
    "retrieval_date",
    "source_type",
    "claim_paraphrase",
    "applicable_office_ids",
    "applicable_process_ids",
    "evidence_status",
    "fact_ids",
    "inference_ids",
}
FACT_FIELDS = {"fact_id", "statement", "source_ids", "office_ids", "process_ids"}
INFERENCE_FIELDS = {
    "inference_id",
    "statement",
    "source_ids",
    "fact_ids",
    "scope_ids",
}
GAP_FIELDS = {"gap_id", "statement", "affected_ids", "blocks_activation"}
SOURCE_TYPES = {
    "agency_mission",
    "executive_order",
    "official_description",
    "official_strategy",
    "presidential_memorandum",
    "statute",
}
EVIDENCE_STATUSES = {"fact", "inference_support", "context_only"}


def _validate_source(source: dict[str, Any]) -> None:
    if set(source) != SOURCE_FIELDS:
        fail("invalid_envelope", "source fields are invalid")
    text_fields = (
        "source_id",
        "issuing_institution",
        "public_title",
        "claim_paraphrase",
    )
    for field in text_fields:
        require_text(source[field], f"source {field}")
    url = require_text(source["canonical_url"], "source canonical_url")
    if not url.startswith("https://"):
        fail("invalid_envelope", "source canonical_url must use HTTPS")
    for field in ("publication_date", "effective_date"):
        require_date(source[field], f"source {field}", optional=True)
    require_date(source["retrieval_date"], "source retrieval_date")
    if source["source_type"] not in SOURCE_TYPES:
        fail("invalid_envelope", "source type is unsupported")
    if source["evidence_status"] not in EVIDENCE_STATUSES:
        fail("invalid_envelope", "source evidence status is unsupported")
    list_fields = (
        "applicable_office_ids",
        "applicable_process_ids",
        "fact_ids",
        "inference_ids",
    )
    for field in list_fields:
        require_text_list(source[field], f"source {field}")


def _validate_claim(record: dict[str, Any], kind: str) -> None:
    fields = FACT_FIELDS if kind == "fact" else INFERENCE_FIELDS
    if set(record) != fields:
        fail("invalid_envelope", f"{kind} fields are invalid")
    require_text(record[f"{kind}_id"], f"{kind} identity")
    require_text(record["statement"], f"{kind} statement")
    for field in fields - {f"{kind}_id", "statement"}:
        require_text_list(record[field], f"{kind} {field}")


def _validate_gap(record: dict[str, Any]) -> None:
    if set(record) != GAP_FIELDS:
        fail("invalid_envelope", "gap fields are invalid")
    require_text(record["gap_id"], "gap identity")
    require_text(record["statement"], "gap statement")
    require_text_list(record["affected_ids"], "gap affected_ids")
    if not isinstance(record["blocks_activation"], bool):
        fail("invalid_envelope", "gap blocks_activation must be boolean")


def validate_source_register(payload: dict[str, Any]) -> None:
    reject_officeholder_fields(payload)
    if set(payload) != REGISTER_FIELDS:
        fail("invalid_envelope", "source-register fields are invalid")
    if payload.get("schema_version") != "us-source-register.v0.1":
        fail("invalid_envelope", "source-register schema is unsupported")
    if payload.get("status") != "candidate":
        fail("invalid_envelope", "source-register status is invalid")
    for field in ("register_id", "register_version"):
        require_text(payload.get(field), f"source-register {field}")
    require_date(payload.get("snapshot_date"), "source-register snapshot_date")
    sources = require_records(payload, "sources")
    facts = require_records(payload, "facts")
    inferences = require_records(payload, "inferences")
    gaps = require_records(payload, "gaps")
    if not sources or not facts:
        fail("invalid_envelope", "source register requires sources and facts")
    for source in sources:
        _validate_source(source)
    for fact in facts:
        _validate_claim(fact, "fact")
    for inference in inferences:
        _validate_claim(inference, "inference")
    for gap in gaps:
        _validate_gap(gap)
    validate_source_references(sources, facts, inferences, gaps)


__all__ = ["validate_source_register"]
