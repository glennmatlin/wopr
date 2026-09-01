# Equal-council two-thirds boundary is corrected

Status: accepted historical correction; not part of the active DATE design

The equal-council manifest encodes two-thirds as `0.6666666667`. The original strict floating-point comparison treated an exact two-of-three share as below that threshold, so only unanimous votes bound. This contradicted the locked Release rule that any two of three members bind.

The aggregator now accepts numerically equal boundary values. Frozen August 18 manifests and artifacts remain unchanged, but that Sounding is superseded for equal-council behavioral claims. A corrected executor, live preflight, composition smoke, 18-cell Sounding, and Overlay Demo receive new receipts.

Consequence: regression coverage must prove that two equal-council votes bind and that a real minority remains below threshold. Packet copy cannot use the August 18 council-versus-staff tables as behavioral evidence.
