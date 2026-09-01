"""Cross-reference validation for U.S. Charter source registers."""

from __future__ import annotations

from typing import Any

from .validation import fail


def validate_source_references(
    sources: list[dict[str, Any]],
    facts: list[dict[str, Any]],
    inferences: list[dict[str, Any]],
    gaps: list[dict[str, Any]],
) -> None:
    collections = (
        (sources, "source"),
        (facts, "fact"),
        (inferences, "inference"),
        (gaps, "gap"),
    )
    identities = [
        record[f"{kind}_id"] for records, kind in collections for record in records
    ]
    if len(identities) != len(set(identities)):
        fail("duplicate_id", "source-register identity namespace repeats")
    source_ids = {record["source_id"] for record in sources}
    sources_by_id = {record["source_id"]: record for record in sources}
    fact_ids = {record["fact_id"] for record in facts}
    facts_by_id = {record["fact_id"]: record for record in facts}
    inference_ids = {record["inference_id"] for record in inferences}
    inferences_by_id = {record["inference_id"]: record for record in inferences}
    for source in sources:
        if not set(source["fact_ids"]) <= fact_ids:
            fail(
                "unbound_fact",
                f"source {source['source_id']} references an unknown fact",
            )
        if not set(source["inference_ids"]) <= inference_ids:
            fail(
                "unbound_inference",
                f"source {source['source_id']} references an unknown inference",
            )
        if any(
            source["source_id"] not in facts_by_id[fact_id]["source_ids"]
            for fact_id in source["fact_ids"]
        ):
            fail("unbound_fact", f"source {source['source_id']} has a one-way fact")
        if any(
            source["source_id"]
            not in inferences_by_id[inference_id]["source_ids"]
            for inference_id in source["inference_ids"]
        ):
            fail(
                "unbound_inference",
                f"source {source['source_id']} has a one-way inference",
            )
    for fact in facts:
        if not fact["source_ids"] or not set(fact["source_ids"]) <= source_ids:
            fail(
                "unknown_reference",
                f"fact {fact['fact_id']} references an unknown source",
            )
        if any(
            fact["fact_id"] not in sources_by_id[source_id]["fact_ids"]
            for source_id in fact["source_ids"]
        ):
            fail("unbound_fact", f"fact {fact['fact_id']} is not bound by its source")
    for inference in inferences:
        unknown_source = not inference["source_ids"] or not set(
            inference["source_ids"]
        ) <= source_ids
        unknown_fact = not set(inference["fact_ids"]) <= fact_ids
        if unknown_source or unknown_fact:
            fail(
                "unknown_reference",
                f"inference {inference['inference_id']} has an unknown reference",
            )
        if any(
            inference["inference_id"]
            not in sources_by_id[source_id]["inference_ids"]
            for source_id in inference["source_ids"]
        ):
            fail(
                "unbound_inference",
                f"inference {inference['inference_id']} is not bound by its source",
            )


__all__ = ["validate_source_references"]
