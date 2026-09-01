# Use five bounded Formal Action families

Status: superseded for DATE by ADR 0033; retained as the closed-interface alternative selected in D47

The first episode must support exactly five Formal Action families: `communicate`, `collect_or_share_intelligence`, `provide_support_or_adjust_posture`, `apply_economic_measure`, and `schedule_contingency_or_reassessment`. Each accepted Formal Action belongs to one family, retains its source Policy Package component, and carries the common actor, object or recipient, scope, timing, authority path, conditions, and constraints plus bounded family-specific parameters frozen before the run.

These execution families are not D45 policy-coverage domains or D14 authority classes. One package component may produce no action or several actions; content spanning families is split into separately linked actions. `no_action` and `not_applicable` remain attributable package dispositions rather than invented Formal Actions.

The Room may deliberate in open language, but the Interpreter may populate a Formal Action only from the decided package, frozen Charter, action catalog, and World state. It may request bounded clarification, but it may not invent policy, targets, recipients, capabilities, authority, conditions, or consequences. Unsupported or unresolved content fails closed for the affected component; EXCON and the World alone accept actions and apply consequences.

## Considered options

- Use one generic policy-action type and let the Interpreter infer its operational meaning.
- Build an exhaustive department-specific action catalog before the first episode.

Both remain non-Setup system alternatives. A generic type leaves consequential interpretation inside arbitrary prose. An exhaustive catalog would make general government coverage a submission gate. Five bounded families give the D45 package and D46 request a finite execution boundary while leaving exact episode templates and authored consequences to the next design layer.

## Consequences

Matched runs must freeze the same family and concrete action-catalog versions. Exact action templates, allowed parameter values, domain-to-template mappings, clarification serialization, World preconditions, and consequence hooks remain open. The existing harness already represents typed actions with stable IDs and payloads, rejects selections outside a finite legal set, and links selected action IDs to replay actions; 11 focused baseline tests passed on 2026-08-25. Those receipts establish a reusable seam, not a DATE Interpreter, World, or end-to-end run.
