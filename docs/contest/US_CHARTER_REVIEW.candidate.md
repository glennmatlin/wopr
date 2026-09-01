# U.S. Room Charter candidate review

Source register: `US_PUBLIC_2026Q3.sources`
Source register SHA-256: `73dbda61ad01472abeadb5bd8aae2aead8a84b5596bbd00c5afbccba21d5051f`
U.S. Charter: `US_PUBLIC_2026Q3`
U.S. Charter SHA-256: `fe3837ad22a898218c3c298d1facf91e1ddd09b1a2d58dfc9a48b9d3c4bf83d2`

## Source register

```json
{
  "schema_version": "us-source-register.v0.1",
  "register_id": "US_PUBLIC_2026Q3.sources",
  "register_version": "0.1.0",
  "status": "candidate",
  "snapshot_date": "2026-08-26",
  "sources": [
    {
      "source_id": "SRC_NSPM1_2025",
      "issuing_institution": "The White House",
      "public_title": "Organization of the National Security Council and Subcommittees",
      "canonical_url": "https://www.whitehouse.gov/presidential-actions/2025/01/organization-of-the-national-security-council-and-subcommittees/",
      "publication_date": "2025-01-20",
      "effective_date": "2025-01-20",
      "retrieval_date": "2026-08-26",
      "source_type": "presidential_memorandum",
      "claim_paraphrase": "NSPM-1 states the public NSC and HSC functions, membership and non-voting attendance classes, staff and Executive Secretary roles, and Principals Committee consensus and referral process.",
      "applicable_office_ids": [
        "SEAT_PRESIDENT",
        "SEAT_VICE_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_ENERGY",
        "SEAT_PANDEMIC_PREPAREDNESS",
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_INTERIOR",
        "SEAT_CHIEF_OF_STAFF",
        "SEAT_NSA",
        "SEAT_HOMELAND_SECURITY",
        "SEAT_HSA",
        "SEAT_DNI",
        "SEAT_CJCS",
        "SEAT_CIA_DIRECTOR",
        "SEAT_WHITE_HOUSE_COUNSEL",
        "SEAT_POLICY_ASSISTANT",
        "SEAT_COUNSELOR"
      ],
      "applicable_process_ids": [
        "SERVICE_EXECUTIVE_SECRETARY",
        "GROUP_PC",
        "GROUP_NSC",
        "GROUP_HSC"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
        "FACT_PUBLIC_ADVISER_STATUS",
        "FACT_PUBLIC_EXECUTIVE_SECRETARY",
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_US_ACTOR_OBJECTIVES",
        "INF_FIRST_EPISODE_ACTIVATION",
        "INF_DETERMINISTIC_WATCH",
        "INF_DETERMINISTIC_EXECUTIVE_SECRETARY",
        "INF_PERSISTENT_OFFICE_SEATS",
        "INF_REPRESENTED_STAFF_ROLES",
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS",
        "INF_POLICY_PACKAGE_SCHEMA",
        "INF_PRESIDENTIAL_ROUTE_SCHEMA",
        "INF_REQUIRED_CONFIRMATION_SCHEMA",
        "INF_WEATHER_SPECIALIST_ROUTE"
      ]
    },
    {
      "source_id": "SRC_USC_50_3021",
      "issuing_institution": "Office of the Law Revision Counsel, U.S. House of Representatives",
      "public_title": "50 U.S.C. 3021 - National Security Council",
      "canonical_url": "https://uscode.house.gov/view.xhtml?req=%28title%3A50+section%3A3021+edition%3Aprelim%29",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "statute",
      "claim_paraphrase": "The statute establishes the NSC to advise the President and support integration of domestic, foreign, and military national-security policy, and specifies statutory membership classes.",
      "applicable_office_ids": [
        "SEAT_PRESIDENT",
        "SEAT_VICE_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_ENERGY",
        "SEAT_PANDEMIC_PREPAREDNESS"
      ],
      "applicable_process_ids": [
        "GROUP_NSC"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_PUBLIC_COUNCIL_MEMBERSHIP"
      ],
      "inference_ids": []
    },
    {
      "source_id": "SRC_USC_22_2651A",
      "issuing_institution": "Office of the Law Revision Counsel, U.S. House of Representatives",
      "public_title": "22 U.S.C. 2651a - Organization of Department of State",
      "canonical_url": "https://uscode.house.gov/view.xhtml?req=%28title%3A22+section%3A2651a+edition%3Aprelim%29",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "statute",
      "claim_paraphrase": "The statute establishes the Secretary of State as head of the Department and assigns administration and foreign-affairs functions subject to law and Presidential direction.",
      "applicable_office_ids": [
        "SEAT_STATE"
      ],
      "applicable_process_ids": [
        "GROUP_DIPLOMATIC_ECONOMIC"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_STATE_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "source_id": "SRC_TREASURY_ROLE",
      "issuing_institution": "U.S. Department of the Treasury",
      "public_title": "Role of the Treasury",
      "canonical_url": "https://home.treasury.gov/about/general-information/role-of-the-treasury",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "agency_mission",
      "claim_paraphrase": "Treasury describes its role in economic and financial policy, financial systems, sanctions, and protection of financial integrity.",
      "applicable_office_ids": [
        "SEAT_TREASURY"
      ],
      "applicable_process_ids": [
        "GROUP_DIPLOMATIC_ECONOMIC"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_TREASURY_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "source_id": "SRC_USC_31_321",
      "issuing_institution": "Office of the Law Revision Counsel, U.S. House of Representatives",
      "public_title": "31 U.S.C. 321 - General authority of the Secretary",
      "canonical_url": "https://uscode.house.gov/view.xhtml?req=%28title%3A31+section%3A321+edition%3Aprelim%29",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "statute",
      "claim_paraphrase": "The statute establishes the Secretary of the Treasury's general duties, authorities, delegation, and administration of the Department.",
      "applicable_office_ids": [
        "SEAT_TREASURY"
      ],
      "applicable_process_ids": [
        "GROUP_DIPLOMATIC_ECONOMIC"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_TREASURY_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "source_id": "SRC_USC_10_113",
      "issuing_institution": "Office of the Law Revision Counsel, U.S. House of Representatives",
      "public_title": "10 U.S.C. 113 - Secretary of Defense",
      "canonical_url": "https://uscode.house.gov/view.xhtml?req=%28title%3A10+section%3A113+edition%3Aprelim%29",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "statute",
      "claim_paraphrase": "The statute identifies the Secretary of Defense as head of the Department of Defense and places the Department under that Secretary's authority, direction, and control.",
      "applicable_office_ids": [
        "SEAT_DEFENSE"
      ],
      "applicable_process_ids": [
        "GROUP_DEFENSE_ESCALATION",
        "GROUP_NUCLEAR_RADIOLOGICAL"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_DEFENSE_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS",
        "INF_STABLE_DEFENSE_OFFICE_LABEL"
      ]
    },
    {
      "source_id": "SRC_ENERGY_MISSION",
      "issuing_institution": "U.S. Department of Energy",
      "public_title": "Mission",
      "canonical_url": "https://www.energy.gov/mission",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "agency_mission",
      "claim_paraphrase": "Energy describes national-security, energy-security, scientific, and environmental responsibilities that bound the department-level contribution.",
      "applicable_office_ids": [
        "SEAT_ENERGY"
      ],
      "applicable_process_ids": [
        "GROUP_NUCLEAR_RADIOLOGICAL"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_ENERGY_NUCLEAR_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "source_id": "SRC_NNSA_MISSION",
      "issuing_institution": "National Nuclear Security Administration",
      "public_title": "About NNSA",
      "canonical_url": "https://www.energy.gov/nnsa/about-nnsa",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "agency_mission",
      "claim_paraphrase": "NNSA describes stockpile stewardship, nonproliferation, and nuclear and radiological emergency-response responsibilities within the Energy Department.",
      "applicable_office_ids": [
        "SEAT_ENERGY"
      ],
      "applicable_process_ids": [
        "GROUP_NUCLEAR_RADIOLOGICAL"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_ENERGY_NUCLEAR_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "source_id": "SRC_USC_28_503",
      "issuing_institution": "Office of the Law Revision Counsel, U.S. House of Representatives",
      "public_title": "28 U.S.C. 503 - Attorney General",
      "canonical_url": "https://uscode.house.gov/view.xhtml?req=%28title%3A28+section%3A503+edition%3Aprelim%29",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "statute",
      "claim_paraphrase": "The statute establishes the Attorney General as head of the Department of Justice.",
      "applicable_office_ids": [
        "SEAT_ATTORNEY_GENERAL"
      ],
      "applicable_process_ids": [
        "GROUP_LEGAL_AUTHORITY",
        "GROUP_HOMELAND_CONSEQUENCES"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_JUSTICE_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "source_id": "SRC_DOJ_NSD_MISSION",
      "issuing_institution": "U.S. Department of Justice",
      "public_title": "About the National Security Division",
      "canonical_url": "https://www.justice.gov/nsd/about-national-security-division-nsd",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "agency_mission",
      "claim_paraphrase": "Justice describes the National Security Division's public counterterrorism, counterintelligence, export-control, sanctions-enforcement, and related legal responsibilities.",
      "applicable_office_ids": [
        "SEAT_ATTORNEY_GENERAL"
      ],
      "applicable_process_ids": [
        "GROUP_LEGAL_AUTHORITY",
        "GROUP_HOMELAND_CONSEQUENCES"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_JUSTICE_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "source_id": "SRC_INTERIOR_MISSION",
      "issuing_institution": "U.S. Department of the Interior",
      "public_title": "About Interior",
      "canonical_url": "https://www.doi.gov/about",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "agency_mission",
      "claim_paraphrase": "Interior describes responsibilities for public lands, natural resources, trust responsibilities, and affected communities.",
      "applicable_office_ids": [
        "SEAT_INTERIOR"
      ],
      "applicable_process_ids": [
        "GROUP_NSC",
        "GROUP_HSC"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_INTERIOR_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "source_id": "SRC_USC_6_112",
      "issuing_institution": "Office of the Law Revision Counsel, U.S. House of Representatives",
      "public_title": "6 U.S.C. 112 - Secretary; functions",
      "canonical_url": "https://uscode.house.gov/view.xhtml?req=%28title%3A6+section%3A112+edition%3Aprelim%29",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "statute",
      "claim_paraphrase": "The statute identifies the Secretary of Homeland Security as head of the Department and assigns authority, direction, and control over the Department.",
      "applicable_office_ids": [
        "SEAT_HOMELAND_SECURITY"
      ],
      "applicable_process_ids": [
        "GROUP_HOMELAND_CONSEQUENCES",
        "GROUP_HSC"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_DHS_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "source_id": "SRC_USC_42_300HH3",
      "issuing_institution": "Office of the Law Revision Counsel, U.S. House of Representatives",
      "public_title": "42 U.S.C. 300hh-3 - Office of Pandemic Preparedness and Response Policy",
      "canonical_url": "https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title42-section300hh-3",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "statute",
      "claim_paraphrase": "The statute assigns the office and its Director advisory and coordination responsibilities for pandemic and other biological threats.",
      "applicable_office_ids": [
        "SEAT_PANDEMIC_PREPAREDNESS"
      ],
      "applicable_process_ids": [
        "GROUP_NSC",
        "GROUP_HSC"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_PANDEMIC_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "source_id": "SRC_USC_50_3024",
      "issuing_institution": "Office of the Law Revision Counsel, U.S. House of Representatives",
      "public_title": "50 U.S.C. 3024 - Responsibilities and authorities of the Director of National Intelligence",
      "canonical_url": "https://uscode.house.gov/view.xhtml?edition=prelim&hl=false&req=granuleid%3AUSC-prelim-title50-section3024",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "statute",
      "claim_paraphrase": "The statute assigns the DNI timely, objective, independent all-source intelligence and requires competitive analysis and presentation of intelligence disagreements where appropriate.",
      "applicable_office_ids": [
        "SEAT_DNI"
      ],
      "applicable_process_ids": [
        "GROUP_THREAT_ATTRIBUTION",
        "GROUP_DEFENSE_ESCALATION",
        "GROUP_NUCLEAR_RADIOLOGICAL"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_DNI_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS",
        "INF_WEATHER_SPECIALIST_ROUTE"
      ]
    },
    {
      "source_id": "SRC_USC_50_3036",
      "issuing_institution": "Office of the Law Revision Counsel, U.S. House of Representatives",
      "public_title": "50 U.S.C. 3036 - Central Intelligence Agency",
      "canonical_url": "https://uscode.house.gov/view.xhtml?edition=prelim&f=treesort&jumpTo=true&num=0&req=%28title%3A50+section%3A3036+edition%3Aprelim%29+OR+%28granuleid%3AUSC-prelim-title50-section3036%29",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "statute",
      "claim_paraphrase": "The statute assigns CIA foreign-intelligence collection, evaluation, and dissemination functions and excludes police, subpoena, and domestic law-enforcement powers.",
      "applicable_office_ids": [
        "SEAT_CIA_DIRECTOR"
      ],
      "applicable_process_ids": [
        "GROUP_THREAT_ATTRIBUTION"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_CIA_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "source_id": "SRC_USC_10_151",
      "issuing_institution": "Office of the Law Revision Counsel, U.S. House of Representatives",
      "public_title": "10 U.S.C. 151 - Joint Chiefs of Staff: composition; functions",
      "canonical_url": "https://uscode.house.gov/view.xhtml?req=%28title%3A10+section%3A151+edition%3Aprelim%29",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "statute",
      "claim_paraphrase": "The statute identifies the CJCS as principal military adviser, requires consultation with other military advisers, and preserves presentation of a range of military advice.",
      "applicable_office_ids": [
        "SEAT_CJCS"
      ],
      "applicable_process_ids": [
        "GROUP_THREAT_ATTRIBUTION",
        "GROUP_DEFENSE_ESCALATION",
        "GROUP_NUCLEAR_RADIOLOGICAL"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_CJCS_ADVICE_NO_COMMAND"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "source_id": "SRC_USC_10_163",
      "issuing_institution": "Office of the Law Revision Counsel, U.S. House of Representatives",
      "public_title": "10 U.S.C. 163 - Role of Chairman of Joint Chiefs of Staff",
      "canonical_url": "https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title10-section163",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "statute",
      "claim_paraphrase": "The statute places the CJCS in the communications and oversight chain while stating that the CJCS does not exercise military command over the Joint Chiefs or armed forces.",
      "applicable_office_ids": [
        "SEAT_CJCS",
        "SEAT_THEATER_COMMANDER"
      ],
      "applicable_process_ids": [
        "GROUP_DEFENSE_ESCALATION"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_CJCS_ADVICE_NO_COMMAND",
        "FACT_COMBATANT_COMMAND_ROLE"
      ],
      "inference_ids": [
        "INF_THEATER_COMMANDER_TRIGGER"
      ]
    },
    {
      "source_id": "SRC_USC_10_164",
      "issuing_institution": "Office of the Law Revision Counsel, U.S. House of Representatives",
      "public_title": "10 U.S.C. 164 - Commanders of combatant commands: assignment; powers and duties",
      "canonical_url": "https://uscode.house.gov/view.xhtml?req=title%3A10+section%3A164+edition%3Aprelim",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "statute",
      "claim_paraphrase": "The statute assigns combatant commanders command and operational responsibilities, which remain distinct from the CJCS advisory function.",
      "applicable_office_ids": [
        "SEAT_THEATER_COMMANDER",
        "SEAT_CJCS"
      ],
      "applicable_process_ids": [
        "GROUP_DEFENSE_ESCALATION"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_COMBATANT_COMMAND_ROLE"
      ],
      "inference_ids": [
        "INF_THEATER_COMMANDER_TRIGGER"
      ]
    },
    {
      "source_id": "SRC_NDS_2026",
      "issuing_institution": "U.S. Department of Defense",
      "public_title": "2026 National Defense Strategy",
      "canonical_url": "https://media.defense.gov/2026/Jan/23/2003864773/-1/-1/0/2026-NATIONAL-DEFENSE-STRATEGY.PDF",
      "publication_date": "2026-01-23",
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "official_strategy",
      "claim_paraphrase": "The dated public strategy describes homeland defense, Indo-Pacific access and balance, partner contributions, nuclear deterrence, and strategic-stability or deconfliction concerns.",
      "applicable_office_ids": [
        "SEAT_DEFENSE",
        "SEAT_CJCS",
        "SEAT_NSA",
        "SEAT_PRESIDENT"
      ],
      "applicable_process_ids": [
        "PERSONA_POSTURE",
        "GROUP_DEFENSE_ESCALATION"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_DATED_PUBLIC_POSTURE"
      ],
      "inference_ids": [
        "INF_US_ACTOR_OBJECTIVES",
        "INF_FIRST_EPISODE_ACTIVATION",
        "INF_DATED_PERSONA_POSTURE",
        "INF_STABLE_DEFENSE_OFFICE_LABEL",
        "INF_THEATER_COMMANDER_TRIGGER"
      ]
    },
    {
      "source_id": "SRC_NSS_2025",
      "issuing_institution": "The White House",
      "public_title": "2025 National Security Strategy",
      "canonical_url": "https://www.whitehouse.gov/wp-content/uploads/2025/12/2025-National-Security-Strategy.pdf",
      "publication_date": null,
      "effective_date": null,
      "retrieval_date": "2026-08-26",
      "source_type": "official_strategy",
      "claim_paraphrase": "The dated public strategy supplies administration-level national-interest, deterrence, regional access, partner, economic, and strategic-stability posture for bounded persona context.",
      "applicable_office_ids": [
        "SEAT_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_NSA"
      ],
      "applicable_process_ids": [
        "PERSONA_POSTURE"
      ],
      "evidence_status": "fact",
      "fact_ids": [
        "FACT_DATED_PUBLIC_POSTURE"
      ],
      "inference_ids": [
        "INF_US_ACTOR_OBJECTIVES",
        "INF_FIRST_EPISODE_ACTIVATION",
        "INF_DATED_PERSONA_POSTURE"
      ]
    }
  ],
  "facts": [
    {
      "fact_id": "FACT_NSC_HSC_FUNCTION",
      "statement": "Public law and NSPM-1 describe the NSC as advising the President on integrated domestic, foreign, and military national-security policy, while the HSC advises on homeland-security matters.",
      "source_ids": [
        "SRC_NSPM1_2025",
        "SRC_USC_50_3021"
      ],
      "office_ids": [
        "SEAT_PRESIDENT",
        "SEAT_NSA",
        "SEAT_HSA"
      ],
      "process_ids": [
        "GROUP_NSC",
        "GROUP_HSC"
      ]
    },
    {
      "fact_id": "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
      "statement": "NSPM-1 publicly enumerates statutory and presidentially designated NSC member classes and adds Homeland Security and the Homeland Security Advisor when the NSC convenes as the HSC.",
      "source_ids": [
        "SRC_NSPM1_2025",
        "SRC_USC_50_3021"
      ],
      "office_ids": [
        "SEAT_PRESIDENT",
        "SEAT_VICE_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_ENERGY",
        "SEAT_PANDEMIC_PREPAREDNESS",
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_INTERIOR",
        "SEAT_CHIEF_OF_STAFF",
        "SEAT_NSA",
        "SEAT_HOMELAND_SECURITY",
        "SEAT_HSA"
      ],
      "process_ids": [
        "GROUP_NSC",
        "GROUP_HSC"
      ]
    },
    {
      "fact_id": "FACT_PUBLIC_ADVISER_STATUS",
      "statement": "NSPM-1 publicly distinguishes regular non-voting DNI, CJCS, and CIA attendance from regular non-voting invitees and issue-relevant attendance discretion.",
      "source_ids": [
        "SRC_NSPM1_2025"
      ],
      "office_ids": [
        "SEAT_DNI",
        "SEAT_CJCS",
        "SEAT_CIA_DIRECTOR",
        "SEAT_WHITE_HOUSE_COUNSEL",
        "SEAT_POLICY_ASSISTANT",
        "SEAT_COUNSELOR"
      ],
      "process_ids": [
        "GROUP_PC",
        "GROUP_NSC",
        "GROUP_HSC"
      ]
    },
    {
      "fact_id": "FACT_PUBLIC_EXECUTIVE_SECRETARY",
      "statement": "NSPM-1 describes one NSC staff serving NSC and HSC, headed by an Executive Secretary who prepares, records, and communicates committee materials, conclusions, decisions, omissions, and taskings.",
      "source_ids": [
        "SRC_NSPM1_2025"
      ],
      "office_ids": [],
      "process_ids": [
        "SERVICE_EXECUTIVE_SECRETARY",
        "GROUP_PC"
      ]
    },
    {
      "fact_id": "FACT_PUBLIC_PC_PROCESS",
      "statement": "NSPM-1 describes the PC as the senior Cabinet-level interagency forum, requires full consensus among present voting attendees for PC action, separately polls presidential attention, and routes specified disagreement or presidential matters to the NSC.",
      "source_ids": [
        "SRC_NSPM1_2025"
      ],
      "office_ids": [
        "SEAT_NSA",
        "SEAT_HSA",
        "SEAT_PRESIDENT"
      ],
      "process_ids": [
        "GROUP_PC",
        "GROUP_NSC",
        "GROUP_HSC"
      ]
    },
    {
      "fact_id": "FACT_STATE_MANDATE",
      "statement": "Public law places the Department of State under the Secretary of State and supplies the stable office boundary for foreign-affairs and diplomatic contributions.",
      "source_ids": [
        "SRC_USC_22_2651A"
      ],
      "office_ids": [
        "SEAT_STATE"
      ],
      "process_ids": [
        "GROUP_DIPLOMATIC_ECONOMIC"
      ]
    },
    {
      "fact_id": "FACT_TREASURY_MANDATE",
      "statement": "Public law establishes the Secretary's general authority and Treasury's public mission includes economic and financial policy, financial systems, sanctions, and financial integrity.",
      "source_ids": [
        "SRC_TREASURY_ROLE",
        "SRC_USC_31_321"
      ],
      "office_ids": [
        "SEAT_TREASURY"
      ],
      "process_ids": [
        "GROUP_DIPLOMATIC_ECONOMIC"
      ]
    },
    {
      "fact_id": "FACT_DEFENSE_MANDATE",
      "statement": "Public law identifies the Secretary of Defense as head of the Department of Defense and places the Department under that Secretary's authority, direction, and control.",
      "source_ids": [
        "SRC_USC_10_113"
      ],
      "office_ids": [
        "SEAT_DEFENSE"
      ],
      "process_ids": [
        "GROUP_DEFENSE_ESCALATION",
        "GROUP_NUCLEAR_RADIOLOGICAL"
      ]
    },
    {
      "fact_id": "FACT_ENERGY_NUCLEAR_MANDATE",
      "statement": "Public Energy and NNSA mission statements cover energy security, nuclear-security and stockpile responsibilities, nonproliferation, and nuclear or radiological emergency response.",
      "source_ids": [
        "SRC_ENERGY_MISSION",
        "SRC_NNSA_MISSION"
      ],
      "office_ids": [
        "SEAT_ENERGY"
      ],
      "process_ids": [
        "GROUP_NUCLEAR_RADIOLOGICAL"
      ]
    },
    {
      "fact_id": "FACT_JUSTICE_MANDATE",
      "statement": "Public law makes the Attorney General head of Justice, and Justice's public national-security mission covers relevant legal, counterintelligence, sanctions-enforcement, and law-enforcement functions.",
      "source_ids": [
        "SRC_USC_28_503",
        "SRC_DOJ_NSD_MISSION"
      ],
      "office_ids": [
        "SEAT_ATTORNEY_GENERAL"
      ],
      "process_ids": [
        "GROUP_LEGAL_AUTHORITY",
        "GROUP_HOMELAND_CONSEQUENCES"
      ]
    },
    {
      "fact_id": "FACT_INTERIOR_MANDATE",
      "statement": "Interior's public mission covers public lands, natural resources, trust responsibilities, and affected communities.",
      "source_ids": [
        "SRC_INTERIOR_MISSION"
      ],
      "office_ids": [
        "SEAT_INTERIOR"
      ],
      "process_ids": [
        "GROUP_NSC",
        "GROUP_HSC"
      ]
    },
    {
      "fact_id": "FACT_DHS_MANDATE",
      "statement": "Public law identifies the Secretary of Homeland Security as head of DHS with authority, direction, and control over the Department.",
      "source_ids": [
        "SRC_USC_6_112"
      ],
      "office_ids": [
        "SEAT_HOMELAND_SECURITY"
      ],
      "process_ids": [
        "GROUP_HOMELAND_CONSEQUENCES",
        "GROUP_HSC"
      ]
    },
    {
      "fact_id": "FACT_PANDEMIC_MANDATE",
      "statement": "Public law assigns the pandemic-preparedness office advisory and coordination duties for pandemic and other biological threats.",
      "source_ids": [
        "SRC_USC_42_300HH3"
      ],
      "office_ids": [
        "SEAT_PANDEMIC_PREPAREDNESS"
      ],
      "process_ids": [
        "GROUP_NSC",
        "GROUP_HSC"
      ]
    },
    {
      "fact_id": "FACT_DNI_MANDATE",
      "statement": "Public law assigns the DNI timely, objective, independent all-source intelligence and requires competitive analysis and appropriate presentation of disagreements.",
      "source_ids": [
        "SRC_USC_50_3024"
      ],
      "office_ids": [
        "SEAT_DNI"
      ],
      "process_ids": [
        "GROUP_THREAT_ATTRIBUTION",
        "GROUP_DEFENSE_ESCALATION",
        "GROUP_NUCLEAR_RADIOLOGICAL"
      ]
    },
    {
      "fact_id": "FACT_CIA_MANDATE",
      "statement": "Public law assigns CIA foreign-intelligence collection, evaluation, and dissemination functions while withholding domestic police and law-enforcement powers.",
      "source_ids": [
        "SRC_USC_50_3036"
      ],
      "office_ids": [
        "SEAT_CIA_DIRECTOR"
      ],
      "process_ids": [
        "GROUP_THREAT_ATTRIBUTION"
      ]
    },
    {
      "fact_id": "FACT_CJCS_ADVICE_NO_COMMAND",
      "statement": "Public law makes the CJCS the principal military adviser, preserves a range of military advice, and states that the CJCS does not exercise military command.",
      "source_ids": [
        "SRC_USC_10_151",
        "SRC_USC_10_163"
      ],
      "office_ids": [
        "SEAT_CJCS"
      ],
      "process_ids": [
        "GROUP_THREAT_ATTRIBUTION",
        "GROUP_DEFENSE_ESCALATION",
        "GROUP_NUCLEAR_RADIOLOGICAL"
      ]
    },
    {
      "fact_id": "FACT_COMBATANT_COMMAND_ROLE",
      "statement": "Public law assigns operational command responsibilities to combatant commanders and keeps that role distinct from the CJCS advisory function.",
      "source_ids": [
        "SRC_USC_10_163",
        "SRC_USC_10_164"
      ],
      "office_ids": [
        "SEAT_THEATER_COMMANDER",
        "SEAT_CJCS"
      ],
      "process_ids": [
        "GROUP_DEFENSE_ESCALATION"
      ]
    },
    {
      "fact_id": "FACT_DATED_PUBLIC_POSTURE",
      "statement": "The dated public national-security and defense strategies describe homeland protection, deterrence, Indo-Pacific access and balance, economic interests, partner contributions, nuclear deterrence, and strategic-stability concerns.",
      "source_ids": [
        "SRC_NDS_2026",
        "SRC_NSS_2025"
      ],
      "office_ids": [
        "SEAT_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_NSA",
        "SEAT_CJCS"
      ],
      "process_ids": [
        "PERSONA_POSTURE"
      ]
    }
  ],
  "inferences": [
    {
      "inference_id": "INF_US_ACTOR_OBJECTIVES",
      "statement": "The five unweighted U.S. actor objectives are an exercise abstraction synthesized from the public institutional mission and dated posture, not an official priority ordering.",
      "source_ids": [
        "SRC_NSPM1_2025",
        "SRC_NDS_2026",
        "SRC_NSS_2025"
      ],
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_DATED_PUBLIC_POSTURE"
      ],
      "scope_ids": [
        "US_PUBLIC_2026Q3",
        "OBJ_US_PROTECT",
        "OBJ_US_DETER",
        "OBJ_US_SUPPORT_HIMALDESH",
        "OBJ_US_PRESERVE_ACCESS",
        "OBJ_US_STRATEGIC_STABILITY"
      ]
    },
    {
      "inference_id": "INF_FIRST_EPISODE_ACTIVATION",
      "statement": "The ridge episode's active, triggered, and unavailable seat dispositions are exercise-specific relevance judgments over the public roster, not public facts about an actual meeting.",
      "source_ids": [
        "SRC_NSPM1_2025",
        "SRC_NDS_2026",
        "SRC_NSS_2025"
      ],
      "fact_ids": [
        "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
        "FACT_PUBLIC_ADVISER_STATUS",
        "FACT_DATED_PUBLIC_POSTURE"
      ],
      "scope_ids": [
        "US_PUBLIC_2026Q3",
        "ridge_seizure.limited_fait_accompli.episode_01"
      ]
    },
    {
      "inference_id": "INF_PERSISTENT_OFFICE_SEATS",
      "statement": "One persistent model-mediated identity per declared office, reused across groups, is a simulation design that preserves office boundaries without claiming official staffing fidelity.",
      "source_ids": [
        "SRC_NSPM1_2025"
      ],
      "fact_ids": [
        "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
        "FACT_PUBLIC_ADVISER_STATUS"
      ],
      "scope_ids": [
        "US_PUBLIC_2026Q3",
        "institution_registry"
      ]
    },
    {
      "inference_id": "INF_DETERMINISTIC_WATCH",
      "statement": "A non-judgmental deterministic Watch is the selected simulation transport for authorized World injects; it is not asserted to reproduce an official watch-floor procedure.",
      "source_ids": [
        "SRC_NSPM1_2025"
      ],
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION"
      ],
      "scope_ids": [
        "SERVICE_WATCH"
      ]
    },
    {
      "inference_id": "INF_DETERMINISTIC_EXECUTIVE_SECRETARY",
      "statement": "The public Executive Secretary record function is implemented as a deterministic service so recording cannot add policy judgment.",
      "source_ids": [
        "SRC_NSPM1_2025"
      ],
      "fact_ids": [
        "FACT_PUBLIC_EXECUTIVE_SECRETARY"
      ],
      "scope_ids": [
        "SERVICE_EXECUTIVE_SECRETARY"
      ]
    },
    {
      "inference_id": "INF_REPRESENTED_STAFF_ROLES",
      "statement": "Deputy and staff roles named by NSPM-1 remain represented inside the corresponding principal office product in the first slice rather than becoming additional model seats.",
      "source_ids": [
        "SRC_NSPM1_2025"
      ],
      "fact_ids": [
        "FACT_PUBLIC_ADVISER_STATUS",
        "FACT_PUBLIC_EXECUTIVE_SECRETARY"
      ],
      "scope_ids": [
        "institution_registry"
      ]
    },
    {
      "inference_id": "INF_SPECIALIST_GROUP_GRAPH",
      "statement": "The seven specialist and synthesis groups are an episode-bounded decomposition of public office mandates and the public requirement for integrated, balanced interagency analysis.",
      "source_ids": [
        "SRC_NSPM1_2025",
        "SRC_USC_22_2651A",
        "SRC_TREASURY_ROLE",
        "SRC_USC_31_321",
        "SRC_USC_10_113",
        "SRC_ENERGY_MISSION",
        "SRC_NNSA_MISSION",
        "SRC_USC_28_503",
        "SRC_USC_6_112",
        "SRC_USC_50_3024",
        "SRC_USC_50_3036",
        "SRC_USC_10_151"
      ],
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_STATE_MANDATE",
        "FACT_TREASURY_MANDATE",
        "FACT_DEFENSE_MANDATE",
        "FACT_ENERGY_NUCLEAR_MANDATE",
        "FACT_JUSTICE_MANDATE",
        "FACT_DHS_MANDATE",
        "FACT_DNI_MANDATE",
        "FACT_CIA_MANDATE",
        "FACT_CJCS_ADVICE_NO_COMMAND"
      ],
      "scope_ids": [
        "groups"
      ]
    },
    {
      "inference_id": "INF_SYNTHETIC_ENTITLEMENTS",
      "statement": "Every information entitlement and disclosure permission is a synthetic least-access design for this evaluation and is not an assertion about classified or actual distribution.",
      "source_ids": [
        "SRC_NSPM1_2025",
        "SRC_USC_22_2651A",
        "SRC_TREASURY_ROLE",
        "SRC_USC_31_321",
        "SRC_USC_10_113",
        "SRC_ENERGY_MISSION",
        "SRC_NNSA_MISSION",
        "SRC_USC_28_503",
        "SRC_DOJ_NSD_MISSION",
        "SRC_INTERIOR_MISSION",
        "SRC_USC_6_112",
        "SRC_USC_42_300HH3",
        "SRC_USC_50_3024",
        "SRC_USC_50_3036",
        "SRC_USC_10_151"
      ],
      "fact_ids": [
        "FACT_STATE_MANDATE",
        "FACT_TREASURY_MANDATE",
        "FACT_DEFENSE_MANDATE",
        "FACT_ENERGY_NUCLEAR_MANDATE",
        "FACT_JUSTICE_MANDATE",
        "FACT_INTERIOR_MANDATE",
        "FACT_DHS_MANDATE",
        "FACT_PANDEMIC_MANDATE",
        "FACT_DNI_MANDATE",
        "FACT_CIA_MANDATE",
        "FACT_CJCS_ADVICE_NO_COMMAND"
      ],
      "scope_ids": [
        "information_classes",
        "disclosure_permissions"
      ]
    },
    {
      "inference_id": "INF_WEATHER_SPECIALIST_ROUTE",
      "statement": "The first episode routes the unchanged forecast through Threat and Attribution before Defense and Escalation, then passes attributable products rather than the raw report into senior synthesis.",
      "source_ids": [
        "SRC_NSPM1_2025",
        "SRC_USC_50_3024"
      ],
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_DNI_MANDATE"
      ],
      "scope_ids": [
        "GROUP_THREAT_ATTRIBUTION",
        "GROUP_DEFENSE_ESCALATION",
        "GROUP_PRESIDENTIAL_SYNTHESIS"
      ]
    },
    {
      "inference_id": "INF_THEATER_COMMANDER_TRIGGER",
      "statement": "A functional synthetic U.S. Theater Commander activates for the ridge episode's access, logistics, readiness, and force-protection questions without binding the fictional arena to a real command or granting combat authority.",
      "source_ids": [
        "SRC_USC_10_163",
        "SRC_USC_10_164",
        "SRC_NDS_2026"
      ],
      "fact_ids": [
        "FACT_CJCS_ADVICE_NO_COMMAND",
        "FACT_COMBATANT_COMMAND_ROLE",
        "FACT_DATED_PUBLIC_POSTURE"
      ],
      "scope_ids": [
        "SEAT_THEATER_COMMANDER",
        "GROUP_DEFENSE_ESCALATION"
      ]
    },
    {
      "inference_id": "INF_POLICY_PACKAGE_SCHEMA",
      "statement": "The integrated conditional Policy Package and its mandatory domain dispositions are evaluation artifacts for preserving contributions, dissent, authority questions, sequencing, and reassessment.",
      "source_ids": [
        "SRC_NSPM1_2025"
      ],
      "fact_ids": [
        "FACT_PUBLIC_PC_PROCESS",
        "FACT_PUBLIC_EXECUTIVE_SECRETARY"
      ],
      "scope_ids": [
        "PRODUCT_POLICY_PACKAGE",
        "GROUP_PC"
      ]
    },
    {
      "inference_id": "INF_PRESIDENTIAL_ROUTE_SCHEMA",
      "statement": "The candidate encodes only presidential policy-direction routes; it encodes no crisis-specific PC or departmental delegation that the public snapshot does not establish.",
      "source_ids": [
        "SRC_NSPM1_2025"
      ],
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "scope_ids": [
        "ROUTE_PRESIDENTIAL_POLICY",
        "ROUTE_PRESIDENTIAL_HOMELAND_POLICY"
      ]
    },
    {
      "inference_id": "INF_REQUIRED_CONFIRMATION_SCHEMA",
      "statement": "Required Confirmations verify that the presidential decision and legal-authority record exist; they do not give advisers a policy vote or claim an official confirmation protocol.",
      "source_ids": [
        "SRC_NSPM1_2025"
      ],
      "fact_ids": [
        "FACT_PUBLIC_EXECUTIVE_SECRETARY",
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "scope_ids": [
        "required_confirmations"
      ]
    },
    {
      "inference_id": "INF_DATED_PERSONA_POSTURE",
      "statement": "Persona posture may use bounded themes from the dated public strategies but cannot convert rhetoric into authority, hidden intent, or a fixed decision preference.",
      "source_ids": [
        "SRC_NDS_2026",
        "SRC_NSS_2025"
      ],
      "fact_ids": [
        "FACT_DATED_PUBLIC_POSTURE"
      ],
      "scope_ids": [
        "PERSONA_POSTURE"
      ]
    },
    {
      "inference_id": "INF_STABLE_DEFENSE_OFFICE_LABEL",
      "statement": "The Charter retains the stable statutory Secretary of Defense office class even where dated strategy copy uses a different administration-specific department label.",
      "source_ids": [
        "SRC_USC_10_113",
        "SRC_NDS_2026"
      ],
      "fact_ids": [
        "FACT_DEFENSE_MANDATE",
        "FACT_DATED_PUBLIC_POSTURE"
      ],
      "scope_ids": [
        "SEAT_DEFENSE"
      ]
    }
  ],
  "gaps": [
    {
      "gap_id": "GAP_PC_DELEGATION_INSTRUMENT",
      "statement": "The public snapshot does not establish a crisis-specific delegation that would let this PC or a department issue a final state-changing policy action; the candidate therefore encodes no such route.",
      "affected_ids": [
        "GROUP_PC",
        "effect_level_action_routes"
      ],
      "blocks_activation": true
    },
    {
      "gap_id": "GAP_EFFECT_AUTHORITY_CONFIRMATION_MAP",
      "statement": "Component-level authority, consultation, capability, and confirmation rules for future Open Action Proposals remain outside Milestone 1 and must be source-bound before any World effect path activates.",
      "affected_ids": [
        "decision_routes",
        "required_confirmations",
        "MILESTONE_2"
      ],
      "blocks_activation": true
    },
    {
      "gap_id": "GAP_ADDITIONAL_INVITEE_MANDATES",
      "statement": "No additional public portfolio mandate was selected for the Policy Assistant or Counselor, so those public invitee classes remain unavailable rather than receiving invented cross-cutting mandates.",
      "affected_ids": [
        "SEAT_POLICY_ASSISTANT",
        "SEAT_COUNSELOR"
      ],
      "blocks_activation": true
    },
    {
      "gap_id": "GAP_CLASSIFIED_PROCESS_FIDELITY",
      "statement": "Public sources cannot establish classified information flows, deliberation practices, or crisis procedures; the Charter claims only a dated public-source abstraction.",
      "affected_ids": [
        "US_PUBLIC_2026Q3"
      ],
      "blocks_activation": false
    },
    {
      "gap_id": "GAP_REAL_COMMAND_MAPPING",
      "statement": "The fictional arena is intentionally not mapped to a real combatant command; the Theater Commander remains a functional synthetic role with bounded information and no invented policy authority.",
      "affected_ids": [
        "SEAT_THEATER_COMMANDER"
      ],
      "blocks_activation": false
    },
    {
      "gap_id": "GAP_DEFENSE_LABEL_DIVERGENCE",
      "statement": "Dated public strategy copy and current statutory naming diverge; the candidate uses the statutory Secretary of Defense office class and records the dated wording only as posture context.",
      "affected_ids": [
        "SEAT_DEFENSE",
        "INF_DATED_PERSONA_POSTURE"
      ],
      "blocks_activation": false
    }
  ]
}
```

## U.S. Charter

```json
{
  "schema_version": "us-room-charter.v0.1",
  "charter_id": "US_PUBLIC_2026Q3",
  "charter_version": "0.1.0",
  "status": "candidate",
  "source_register_id": "US_PUBLIC_2026Q3.sources",
  "source_register_hash": "73dbda61ad01472abeadb5bd8aae2aead8a84b5596bbd00c5afbccba21d5051f",
  "actor_id": "ACTOR_UNITED_STATES",
  "objective_ids": [
    "OBJ_US_PROTECT",
    "OBJ_US_DETER",
    "OBJ_US_SUPPORT_HIMALDESH",
    "OBJ_US_PRESERVE_ACCESS",
    "OBJ_US_STRATEGIC_STABILITY"
  ],
  "institution_registry": {
    "seats": [
      {
        "seat_id": "SEAT_PRESIDENT",
        "office_class": "President of the United States",
        "first_slice_disposition": "active",
        "adviser_status": "voting_principal",
        "mandate": "Set the desired end state and decide presidential policy after receiving integrated options, dissent, confidence, legal status, and implementation status.",
        "supported_contributions": [
          "decide_presidential_policy",
          "narrow_or_sequence_options",
          "reject_or_return_package",
          "request_underlying_brief"
        ],
        "prohibited_actions": [
          "receive_hidden_world_truth",
          "treat_adviser_input_as_policy_vote",
          "create_unencoded_authority"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD",
          "INFO_ROUTING_STATE",
          "INFO_RETRIEVED_UNDERLYING"
        ],
        "group_ids": [
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_PRESIDENTIAL_POLICY"
        ],
        "decision_route_roles": [
          "owning_authority",
          "presidential_decider"
        ],
        "persona_posture_ids": [
          "INF_DATED_PERSONA_POSTURE"
        ],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_NSC_HSC_FUNCTION",
          "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
          "FACT_PUBLIC_PC_PROCESS"
        ],
        "inference_ids": [
          "INF_US_ACTOR_OBJECTIVES",
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SYNTHETIC_ENTITLEMENTS",
          "INF_PRESIDENTIAL_ROUTE_SCHEMA"
        ]
      },
      {
        "seat_id": "SEAT_VICE_PRESIDENT",
        "office_class": "Vice President of the United States",
        "first_slice_disposition": "active",
        "adviser_status": "voting_principal",
        "mandate": "Supply independent senior challenge, continuity, and cross-portfolio consequence analysis without claiming separate policy authority absent succession or another encoded authority.",
        "supported_contributions": [
          "independent_senior_advice",
          "challenge_assumptions",
          "surface_cross_portfolio_consequences"
        ],
        "prohibited_actions": [
          "claim_separate_presidential_authority",
          "substitute_for_president_without_encoded_condition"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_PRESIDENTIAL_SYNTHESIS",
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_SENIOR_DECISION"
        ],
        "decision_route_roles": [
          "consulted_principal"
        ],
        "persona_posture_ids": [
          "INF_DATED_PERSONA_POSTURE"
        ],
        "represented_role_ids": [
          "ROLE_VICE_PRESIDENT_NSA"
        ],
        "fact_ids": [
          "FACT_PUBLIC_COUNCIL_MEMBERSHIP"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_REPRESENTED_STAFF_ROLES",
          "INF_SYNTHETIC_ENTITLEMENTS"
        ]
      },
      {
        "seat_id": "SEAT_STATE",
        "office_class": "Secretary of State",
        "first_slice_disposition": "active",
        "adviser_status": "voting_principal",
        "mandate": "Own diplomatic analysis, partner and adversary channels, negotiation and signaling options, and checks against unsupported commitments.",
        "supported_contributions": [
          "diplomatic_assessment",
          "private_and_public_channels",
          "partner_support_options",
          "unsupported_commitment_check"
        ],
        "prohibited_actions": [
          "invent_treaty_guarantee",
          "promise_unapproved_military_action",
          "mutate_world_state"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_RAW_WEATHER_FORECAST",
          "INFO_DIPLOMATIC_PRIVATE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_THREAT_ATTRIBUTION",
          "GROUP_DIPLOMATIC_ECONOMIC",
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_BASELINE_ARENA"
        ],
        "decision_route_roles": [
          "consulted_principal"
        ],
        "persona_posture_ids": [
          "INF_DATED_PERSONA_POSTURE"
        ],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
          "FACT_STATE_MANDATE"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SPECIALIST_GROUP_GRAPH",
          "INF_SYNTHETIC_ENTITLEMENTS",
          "INF_WEATHER_SPECIALIST_ROUTE"
        ]
      },
      {
        "seat_id": "SEAT_TREASURY",
        "office_class": "Secretary of the Treasury",
        "first_slice_disposition": "active",
        "adviser_status": "voting_principal",
        "mandate": "Own financial, sanctions, market, and implementation analysis within Treasury's public mission and encoded authorities.",
        "supported_contributions": [
          "financial_exposure_analysis",
          "sanctions_design",
          "market_consequence_analysis",
          "financial_implementation_constraints"
        ],
        "prohibited_actions": [
          "make_military_commitment",
          "make_diplomatic_commitment",
          "invent_financial_authority"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_FINANCIAL_PRIVATE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_DIPLOMATIC_ECONOMIC",
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_ECONOMIC_EXPOSURE"
        ],
        "decision_route_roles": [
          "consulted_principal"
        ],
        "persona_posture_ids": [
          "INF_DATED_PERSONA_POSTURE"
        ],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
          "FACT_TREASURY_MANDATE"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SPECIALIST_GROUP_GRAPH",
          "INF_SYNTHETIC_ENTITLEMENTS"
        ]
      },
      {
        "seat_id": "SEAT_DEFENSE",
        "office_class": "Secretary of Defense",
        "first_slice_disposition": "active",
        "adviser_status": "voting_principal",
        "mandate": "Own civilian defense policy, posture, readiness, logistics, support capacity, force risk, and military-option framing through encoded decision paths.",
        "supported_contributions": [
          "defense_policy_options",
          "posture_and_readiness_analysis",
          "logistics_and_support_capacity",
          "force_protection_and_escalation_risk"
        ],
        "prohibited_actions": [
          "issue_unencoded_world_action",
          "replace_combatant_command_advice",
          "treat_access_as_combat_authority"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_RAW_WEATHER_FORECAST",
          "INFO_DEFENSE_PRIVATE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_DEFENSE_ESCALATION",
          "GROUP_NUCLEAR_RADIOLOGICAL",
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_BASELINE_ARENA"
        ],
        "decision_route_roles": [
          "consulted_principal"
        ],
        "persona_posture_ids": [
          "INF_DATED_PERSONA_POSTURE",
          "INF_STABLE_DEFENSE_OFFICE_LABEL"
        ],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
          "FACT_DEFENSE_MANDATE"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SPECIALIST_GROUP_GRAPH",
          "INF_SYNTHETIC_ENTITLEMENTS",
          "INF_WEATHER_SPECIALIST_ROUTE",
          "INF_STABLE_DEFENSE_OFFICE_LABEL"
        ]
      },
      {
        "seat_id": "SEAT_ENERGY",
        "office_class": "Secretary of Energy",
        "first_slice_disposition": "active",
        "adviser_status": "voting_principal",
        "mandate": "Own nuclear-security, radiological, stockpile, emergency-response, energy-system, and energy-market technical analysis within the public Energy mission.",
        "supported_contributions": [
          "nuclear_security_analysis",
          "radiological_emergency_options",
          "stockpile_and_nonproliferation_context",
          "energy_system_consequences"
        ],
        "prohibited_actions": [
          "exercise_military_command",
          "invent_nuclear_status",
          "treat_technical_advice_as_use_authority"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_NUCLEAR_PRIVATE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_NUCLEAR_RADIOLOGICAL",
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_NUCLEAR_RISK"
        ],
        "decision_route_roles": [
          "consulted_principal"
        ],
        "persona_posture_ids": [
          "INF_DATED_PERSONA_POSTURE"
        ],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
          "FACT_ENERGY_NUCLEAR_MANDATE"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SPECIALIST_GROUP_GRAPH",
          "INF_SYNTHETIC_ENTITLEMENTS"
        ]
      },
      {
        "seat_id": "SEAT_PANDEMIC_PREPAREDNESS",
        "office_class": "Director of the Office of Pandemic Preparedness and Response Policy",
        "first_slice_disposition": "triggered",
        "adviser_status": "voting_principal",
        "mandate": "Supply pandemic and biological-threat preparedness and coordination advice only when a supported biological trigger is present.",
        "supported_contributions": [
          "biological_threat_assessment",
          "preparedness_and_response_coordination"
        ],
        "prohibited_actions": [
          "expand_beyond_biological_mandate",
          "activate_without_supported_trigger"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_BIO_PRIVATE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_BIOLOGICAL_THREAT"
        ],
        "decision_route_roles": [
          "consulted_principal"
        ],
        "persona_posture_ids": [],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
          "FACT_PANDEMIC_MANDATE"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SYNTHETIC_ENTITLEMENTS"
        ]
      },
      {
        "seat_id": "SEAT_ATTORNEY_GENERAL",
        "office_class": "Attorney General",
        "first_slice_disposition": "triggered",
        "adviser_status": "voting_principal",
        "mandate": "Own departmental legal, national-security law-enforcement, counterintelligence, and domestic investigative analysis while keeping legal constraint distinct from a policy vote.",
        "supported_contributions": [
          "departmental_legal_analysis",
          "authority_and_consultation_review",
          "law_enforcement_and_counterintelligence_analysis",
          "record_legal_disagreement"
        ],
        "prohibited_actions": [
          "convert_legal_review_into_policy_veto",
          "act_for_white_house_counsel",
          "invent_authority"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_LEGAL_PRIVATE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_LEGAL_AUTHORITY",
          "GROUP_HOMELAND_CONSEQUENCES",
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_LEGAL_AUTHORITY_REVIEW"
        ],
        "decision_route_roles": [
          "consulted_principal",
          "authority_record_reviewer"
        ],
        "persona_posture_ids": [],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
          "FACT_JUSTICE_MANDATE"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SPECIALIST_GROUP_GRAPH",
          "INF_SYNTHETIC_ENTITLEMENTS",
          "INF_REQUIRED_CONFIRMATION_SCHEMA"
        ]
      },
      {
        "seat_id": "SEAT_INTERIOR",
        "office_class": "Secretary of the Interior",
        "first_slice_disposition": "triggered",
        "adviser_status": "voting_principal",
        "mandate": "Supply protective and consequence analysis only for affected U.S. territory, lands, resources, trust responsibilities, or communities placed in scope.",
        "supported_contributions": [
          "territorial_and_resource_impact",
          "trust_and_community_impact",
          "interior_protective_measures"
        ],
        "prohibited_actions": [
          "claim_foreign_policy_portfolio",
          "activate_without_domestic_interest",
          "invent_territorial_interest"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_INTERIOR_PRIVATE",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_INTERIOR_INTEREST"
        ],
        "decision_route_roles": [
          "consulted_principal"
        ],
        "persona_posture_ids": [],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
          "FACT_INTERIOR_MANDATE"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SYNTHETIC_ENTITLEMENTS"
        ]
      },
      {
        "seat_id": "SEAT_CHIEF_OF_STAFF",
        "office_class": "White House Chief of Staff",
        "first_slice_disposition": "active",
        "adviser_status": "voting_principal",
        "mandate": "Test White House execution, surface implementation conflicts, and handle the encoded appeal concerning an inaccurate committee record without substituting a personal policy vote for the President's decision.",
        "supported_contributions": [
          "white_house_execution_challenge",
          "implementation_conflict_analysis",
          "encoded_record_appeal"
        ],
        "prohibited_actions": [
          "substitute_for_presidential_policy",
          "create_chair_weight",
          "rewrite_attributable_dissent"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD",
          "INFO_ROUTING_STATE"
        ],
        "group_ids": [
          "GROUP_PRESIDENTIAL_SYNTHESIS",
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_SENIOR_DECISION"
        ],
        "decision_route_roles": [
          "consulted_principal",
          "record_appeal"
        ],
        "persona_posture_ids": [
          "INF_DATED_PERSONA_POSTURE"
        ],
        "represented_role_ids": [
          "ROLE_DEPUTY_CHIEF_OF_STAFF_POLICY"
        ],
        "fact_ids": [
          "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
          "FACT_PUBLIC_EXECUTIVE_SECRETARY"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_REPRESENTED_STAFF_ROLES",
          "INF_SYNTHETIC_ENTITLEMENTS"
        ]
      },
      {
        "seat_id": "SEAT_NSA",
        "office_class": "National Security Advisor",
        "first_slice_disposition": "active",
        "adviser_status": "voting_principal",
        "mandate": "Activate and coordinate the national-security process, chair the PC, integrate attributable products, preserve dissent, and route issues without extra chair weight.",
        "supported_contributions": [
          "convene_and_schedule",
          "integrate_products",
          "preserve_dissent",
          "chair_pc",
          "route_presidential_attention"
        ],
        "prohibited_actions": [
          "exercise_chair_weight",
          "erase_nonconcurrence",
          "invent_portfolio_authority",
          "repair_model_omission"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD",
          "INFO_ROUTING_STATE",
          "INFO_RETRIEVED_UNDERLYING"
        ],
        "group_ids": [
          "GROUP_PRESIDENTIAL_SYNTHESIS",
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_EVERY_NATIONAL_SECURITY_CYCLE"
        ],
        "decision_route_roles": [
          "route_coordinator",
          "pc_chair"
        ],
        "persona_posture_ids": [
          "INF_DATED_PERSONA_POSTURE"
        ],
        "represented_role_ids": [
          "ROLE_PRINCIPAL_DEPUTY_NSA"
        ],
        "fact_ids": [
          "FACT_NSC_HSC_FUNCTION",
          "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
          "FACT_PUBLIC_PC_PROCESS"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_REPRESENTED_STAFF_ROLES",
          "INF_SPECIALIST_GROUP_GRAPH",
          "INF_SYNTHETIC_ENTITLEMENTS",
          "INF_PRESIDENTIAL_ROUTE_SCHEMA"
        ]
      },
      {
        "seat_id": "SEAT_HOMELAND_SECURITY",
        "office_class": "Secretary of Homeland Security",
        "first_slice_disposition": "triggered",
        "adviser_status": "voting_principal",
        "mandate": "Own homeland protection, border, infrastructure, cyber-consequence, and domestic-response analysis when a supported homeland trigger is present.",
        "supported_contributions": [
          "homeland_threat_assessment",
          "critical_infrastructure_consequence",
          "border_and_domestic_response",
          "homeland_protective_measures"
        ],
        "prohibited_actions": [
          "conduct_foreign_military_action",
          "activate_without_homeland_relevance",
          "replace_hsa_process_role"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_HOMELAND_PRIVATE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_HOMELAND_CONSEQUENCES",
          "GROUP_PC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_HOMELAND_CONSEQUENCE"
        ],
        "decision_route_roles": [
          "consulted_principal"
        ],
        "persona_posture_ids": [],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
          "FACT_DHS_MANDATE"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SPECIALIST_GROUP_GRAPH",
          "INF_SYNTHETIC_ENTITLEMENTS"
        ]
      },
      {
        "seat_id": "SEAT_HSA",
        "office_class": "Homeland Security Advisor",
        "first_slice_disposition": "triggered",
        "adviser_status": "voting_principal",
        "mandate": "Perform the HSA process role for HSC-class matters, chair the homeland PC path, preserve dissent, and route without claiming a separate operational portfolio.",
        "supported_contributions": [
          "hsc_process_integration",
          "homeland_pc_chair",
          "hsc_referral",
          "preserve_homeland_dissent"
        ],
        "prohibited_actions": [
          "claim_independent_portfolio_action",
          "exercise_chair_weight",
          "activate_hsc_without_supported_trigger"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_HOMELAND_PRIVATE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD",
          "INFO_ROUTING_STATE",
          "INFO_RETRIEVED_UNDERLYING"
        ],
        "group_ids": [
          "GROUP_HOMELAND_CONSEQUENCES",
          "GROUP_PC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_HOMELAND_CONSEQUENCE"
        ],
        "decision_route_roles": [
          "homeland_route_coordinator",
          "homeland_pc_chair"
        ],
        "persona_posture_ids": [],
        "represented_role_ids": [
          "ROLE_DEPUTY_HOMELAND_SECURITY_ADVISOR"
        ],
        "fact_ids": [
          "FACT_NSC_HSC_FUNCTION",
          "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
          "FACT_PUBLIC_PC_PROCESS"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_REPRESENTED_STAFF_ROLES",
          "INF_SPECIALIST_GROUP_GRAPH",
          "INF_SYNTHETIC_ENTITLEMENTS",
          "INF_PRESIDENTIAL_ROUTE_SCHEMA"
        ]
      },
      {
        "seat_id": "SEAT_DNI",
        "office_class": "Director of National Intelligence",
        "first_slice_disposition": "active",
        "adviser_status": "non_voting_adviser",
        "mandate": "Provide objective all-source assessment with confidence, alternatives, gaps, warning, competitive analysis, and preserved disagreement without making policy.",
        "supported_contributions": [
          "all_source_assessment",
          "confidence_and_alternatives",
          "warning_and_collection_gaps",
          "intelligence_dissent"
        ],
        "prohibited_actions": [
          "cast_policy_vote",
          "recommend_as_owning_policy_authority",
          "invent_hidden_world_truth"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_RAW_WEATHER_FORECAST",
          "INFO_INTELLIGENCE_PRIVATE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_THREAT_ATTRIBUTION",
          "GROUP_DEFENSE_ESCALATION",
          "GROUP_NUCLEAR_RADIOLOGICAL",
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_BASELINE_ARENA"
        ],
        "decision_route_roles": [
          "consulted_adviser"
        ],
        "persona_posture_ids": [],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_PUBLIC_ADVISER_STATUS",
          "FACT_DNI_MANDATE"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SPECIALIST_GROUP_GRAPH",
          "INF_SYNTHETIC_ENTITLEMENTS",
          "INF_WEATHER_SPECIALIST_ROUTE"
        ]
      },
      {
        "seat_id": "SEAT_CJCS",
        "office_class": "Chairman of the Joint Chiefs of Staff",
        "first_slice_disposition": "active",
        "adviser_status": "non_voting_adviser",
        "mandate": "Provide independent joint military advice, feasibility, risk, requirements, alternatives, and commander views without exercising command or voting on policy.",
        "supported_contributions": [
          "joint_military_advice",
          "military_feasibility_and_risk",
          "commander_views",
          "military_dissent"
        ],
        "prohibited_actions": [
          "cast_policy_vote",
          "issue_military_command",
          "invent_force_availability",
          "replace_civilian_defense_policy"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_RAW_WEATHER_FORECAST",
          "INFO_MILITARY_ADVICE_PRIVATE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_THREAT_ATTRIBUTION",
          "GROUP_DEFENSE_ESCALATION",
          "GROUP_NUCLEAR_RADIOLOGICAL",
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_BASELINE_ARENA"
        ],
        "decision_route_roles": [
          "consulted_adviser"
        ],
        "persona_posture_ids": [
          "INF_DATED_PERSONA_POSTURE"
        ],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_PUBLIC_ADVISER_STATUS",
          "FACT_CJCS_ADVICE_NO_COMMAND"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SPECIALIST_GROUP_GRAPH",
          "INF_SYNTHETIC_ENTITLEMENTS",
          "INF_WEATHER_SPECIALIST_ROUTE"
        ]
      },
      {
        "seat_id": "SEAT_CIA_DIRECTOR",
        "office_class": "Director of the Central Intelligence Agency",
        "first_slice_disposition": "active",
        "adviser_status": "non_voting_adviser",
        "mandate": "Provide foreign-source reporting, leadership and intent assessment, access and source-risk analysis, and bounded feasibility advice within the public CIA mission.",
        "supported_contributions": [
          "foreign_source_reporting",
          "leadership_and_intent_assessment",
          "access_and_source_risk",
          "bounded_feasibility_advice"
        ],
        "prohibited_actions": [
          "cast_policy_vote",
          "invent_collection_or_covert_capability",
          "claim_domestic_law_enforcement_power",
          "approve_policy_action"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_RAW_WEATHER_FORECAST",
          "INFO_FOREIGN_SOURCE_PRIVATE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_THREAT_ATTRIBUTION",
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_BASELINE_ARENA"
        ],
        "decision_route_roles": [
          "consulted_adviser"
        ],
        "persona_posture_ids": [],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_PUBLIC_ADVISER_STATUS",
          "FACT_CIA_MANDATE"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SPECIALIST_GROUP_GRAPH",
          "INF_SYNTHETIC_ENTITLEMENTS",
          "INF_WEATHER_SPECIALIST_ROUTE"
        ]
      },
      {
        "seat_id": "SEAT_WHITE_HOUSE_COUNSEL",
        "office_class": "Counsel to the President",
        "first_slice_disposition": "triggered",
        "adviser_status": "non_voting_invitee",
        "mandate": "Advise the President and Executive Office on presidential actions, process, and EOP legal issues without replacing Justice or becoming a policy voter.",
        "supported_contributions": [
          "eop_legal_advice",
          "presidential_action_review",
          "process_objection",
          "record_legal_disagreement"
        ],
        "prohibited_actions": [
          "cast_policy_vote",
          "replace_attorney_general",
          "take_independent_policy_action"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_EOP_LEGAL_PRIVATE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_LEGAL_AUTHORITY",
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_LEGAL_AUTHORITY_REVIEW"
        ],
        "decision_route_roles": [
          "consulted_adviser",
          "authority_record_reviewer"
        ],
        "persona_posture_ids": [],
        "represented_role_ids": [
          "ROLE_DEPUTY_COUNSEL_NATIONAL_SECURITY"
        ],
        "fact_ids": [
          "FACT_PUBLIC_ADVISER_STATUS"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_REPRESENTED_STAFF_ROLES",
          "INF_SPECIALIST_GROUP_GRAPH",
          "INF_SYNTHETIC_ENTITLEMENTS",
          "INF_REQUIRED_CONFIRMATION_SCHEMA"
        ]
      },
      {
        "seat_id": "SEAT_POLICY_ASSISTANT",
        "office_class": "Assistant to the President for Policy",
        "first_slice_disposition": "unavailable_without_mandate",
        "adviser_status": "non_voting_invitee",
        "mandate": "Contribute only after a separate public source binds a relevant cross-cutting policy portfolio for the frozen Charter version.",
        "supported_contributions": [
          "source_bound_cross_cutting_policy_advice"
        ],
        "prohibited_actions": [
          "activate_without_additional_mandate",
          "become_generic_extra_adviser",
          "cast_policy_vote"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_PC",
          "GROUP_NSC",
          "GROUP_HSC"
        ],
        "activation_predicate_ids": [
          "ACT_ADDITIONAL_INVITEE_MANDATE"
        ],
        "decision_route_roles": [
          "consulted_adviser"
        ],
        "persona_posture_ids": [],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_PUBLIC_ADVISER_STATUS"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SYNTHETIC_ENTITLEMENTS"
        ]
      },
      {
        "seat_id": "SEAT_COUNSELOR",
        "office_class": "Counselor to the President",
        "first_slice_disposition": "unavailable_without_mandate",
        "adviser_status": "non_voting_invitee",
        "mandate": "Contribute only after a separate public source binds a relevant advisory portfolio for the frozen Charter version.",
        "supported_contributions": [
          "source_bound_presidential_advice"
        ],
        "prohibited_actions": [
          "activate_without_additional_mandate",
          "become_generic_extra_adviser",
          "cast_policy_vote"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_PC"
        ],
        "activation_predicate_ids": [
          "ACT_ADDITIONAL_INVITEE_MANDATE"
        ],
        "decision_route_roles": [
          "consulted_adviser"
        ],
        "persona_posture_ids": [],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_PUBLIC_ADVISER_STATUS"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SYNTHETIC_ENTITLEMENTS"
        ]
      },
      {
        "seat_id": "SEAT_THEATER_COMMANDER",
        "office_class": "Functional U.S. Theater Commander",
        "first_slice_disposition": "triggered",
        "adviser_status": "non_voting_adviser",
        "mandate": "Supply synthetic theater operational feasibility, requirements, alternatives, timing, logistics, force-protection risk, and dissent for the bounded fictional AOR.",
        "supported_contributions": [
          "operational_feasibility",
          "theater_requirements_and_alternatives",
          "logistics_and_force_protection_risk",
          "operational_dissent"
        ],
        "prohibited_actions": [
          "set_policy",
          "promise_forces",
          "issue_state_changing_order",
          "replace_defense_or_cjcs",
          "map_fictional_aor_to_real_command"
        ],
        "information_entitlement_ids": [
          "INFO_COMMON_CRISIS_PICTURE",
          "INFO_RAW_WEATHER_FORECAST",
          "INFO_THEATER_PRIVATE",
          "INFO_CELL_PRODUCTS",
          "INFO_SYNTHESIS_PRODUCT",
          "INFO_POLICY_PACKAGE",
          "INFO_DECISION_RECORD"
        ],
        "group_ids": [
          "GROUP_DEFENSE_ESCALATION",
          "GROUP_PC",
          "GROUP_NSC"
        ],
        "activation_predicate_ids": [
          "ACT_THEATER_OPERATIONAL_RISK"
        ],
        "decision_route_roles": [
          "consulted_adviser"
        ],
        "persona_posture_ids": [],
        "represented_role_ids": [],
        "fact_ids": [
          "FACT_CJCS_ADVICE_NO_COMMAND",
          "FACT_COMBATANT_COMMAND_ROLE"
        ],
        "inference_ids": [
          "INF_FIRST_EPISODE_ACTIVATION",
          "INF_PERSISTENT_OFFICE_SEATS",
          "INF_SYNTHETIC_ENTITLEMENTS",
          "INF_THEATER_COMMANDER_TRIGGER",
          "INF_WEATHER_SPECIALIST_ROUTE"
        ]
      }
    ],
    "services": [
      {
        "service_id": "SERVICE_WATCH",
        "purpose": "Deliver authorized World injects without policy judgment or content repair.",
        "responsibilities": [
          "validate_declared_delivery_identity",
          "deliver_unchanged_payload",
          "apply_disclosure_permissions",
          "record_delivery_and_retrieval"
        ],
        "prohibited_actions": [
          "summarize_or_reinterpret_inject",
          "promote_private_input_to_common",
          "repair_omitted_analysis",
          "exercise_room_judgment"
        ],
        "activation_predicate_ids": [
          "ACT_EVERY_NATIONAL_SECURITY_CYCLE"
        ],
        "fact_ids": [
          "FACT_NSC_HSC_FUNCTION"
        ],
        "inference_ids": [
          "INF_DETERMINISTIC_WATCH",
          "INF_SYNTHETIC_ENTITLEMENTS"
        ]
      },
      {
        "service_id": "SERVICE_EXECUTIVE_SECRETARY",
        "purpose": "Prepare and preserve the exact committee record without adding policy judgment.",
        "responsibilities": [
          "prepare_required_papers",
          "record_conclusions_and_decisions",
          "record_what_was_not_decided",
          "record_taskings_and_dissent",
          "communicate_final_record"
        ],
        "prohibited_actions": [
          "cast_policy_vote",
          "resolve_substantive_disagreement",
          "invent_missing_decision",
          "alter_attributable_position"
        ],
        "activation_predicate_ids": [
          "ACT_EVERY_NATIONAL_SECURITY_CYCLE"
        ],
        "fact_ids": [
          "FACT_PUBLIC_EXECUTIVE_SECRETARY"
        ],
        "inference_ids": [
          "INF_DETERMINISTIC_EXECUTIVE_SECRETARY"
        ]
      }
    ]
  },
  "groups": [
    {
      "group_id": "GROUP_THREAT_ATTRIBUTION",
      "purpose": "Produce an attributable threat, intent, attribution, warning, confidence, alternatives, and gaps assessment.",
      "ordered_eligible_member_ids": [
        "SEAT_DNI",
        "SEAT_CIA_DIRECTOR",
        "SEAT_STATE",
        "SEAT_CJCS"
      ],
      "active_member_rule": "activated_voting_and_advisers",
      "input_entitlement_ids": [
        "INFO_COMMON_CRISIS_PICTURE",
        "INFO_RAW_WEATHER_FORECAST",
        "INFO_INTELLIGENCE_PRIVATE",
        "INFO_FOREIGN_SOURCE_PRIVATE",
        "INFO_DIPLOMATIC_PRIVATE",
        "INFO_MILITARY_ADVICE_PRIVATE"
      ],
      "dependency_group_ids": [],
      "shared_seat_barrier_ids": [
        "SEAT_DNI",
        "SEAT_CIA_DIRECTOR",
        "SEAT_STATE",
        "SEAT_CJCS"
      ],
      "activation_predicate_id": "ACT_BASELINE_ARENA",
      "product_schema_id": "PRODUCT_THREAT_ASSESSMENT",
      "collection_order": 10,
      "failure_effect": "missing_required_product",
      "fact_ids": [
        "FACT_STATE_MANDATE",
        "FACT_DNI_MANDATE",
        "FACT_CIA_MANDATE",
        "FACT_CJCS_ADVICE_NO_COMMAND"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS",
        "INF_WEATHER_SPECIALIST_ROUTE"
      ]
    },
    {
      "group_id": "GROUP_DIPLOMATIC_ECONOMIC",
      "purpose": "Produce integrated diplomatic, signaling, partner-support, financial, trade, sanctions, and humanitarian options.",
      "ordered_eligible_member_ids": [
        "SEAT_STATE",
        "SEAT_TREASURY"
      ],
      "active_member_rule": "activated_voting_and_advisers",
      "input_entitlement_ids": [
        "INFO_COMMON_CRISIS_PICTURE",
        "INFO_DIPLOMATIC_PRIVATE",
        "INFO_FINANCIAL_PRIVATE"
      ],
      "dependency_group_ids": [],
      "shared_seat_barrier_ids": [
        "SEAT_STATE",
        "SEAT_TREASURY"
      ],
      "activation_predicate_id": "ACT_ECONOMIC_EXPOSURE",
      "product_schema_id": "PRODUCT_DIPLOMATIC_ECONOMIC_OPTIONS",
      "collection_order": 20,
      "failure_effect": "missing_required_product",
      "fact_ids": [
        "FACT_STATE_MANDATE",
        "FACT_TREASURY_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "group_id": "GROUP_NUCLEAR_RADIOLOGICAL",
      "purpose": "Produce nuclear and radiological technical status, warning, ambiguity, deterrence, escalation, and emergency-option analysis.",
      "ordered_eligible_member_ids": [
        "SEAT_ENERGY",
        "SEAT_DEFENSE",
        "SEAT_CJCS",
        "SEAT_DNI"
      ],
      "active_member_rule": "activated_voting_and_advisers",
      "input_entitlement_ids": [
        "INFO_COMMON_CRISIS_PICTURE",
        "INFO_NUCLEAR_PRIVATE",
        "INFO_DEFENSE_PRIVATE",
        "INFO_MILITARY_ADVICE_PRIVATE",
        "INFO_INTELLIGENCE_PRIVATE"
      ],
      "dependency_group_ids": [],
      "shared_seat_barrier_ids": [
        "SEAT_ENERGY",
        "SEAT_DEFENSE",
        "SEAT_CJCS",
        "SEAT_DNI"
      ],
      "activation_predicate_id": "ACT_NUCLEAR_RISK",
      "product_schema_id": "PRODUCT_NUCLEAR_RADIOLOGICAL_ASSESSMENT",
      "collection_order": 30,
      "failure_effect": "missing_required_product",
      "fact_ids": [
        "FACT_ENERGY_NUCLEAR_MANDATE",
        "FACT_DEFENSE_MANDATE",
        "FACT_CJCS_ADVICE_NO_COMMAND",
        "FACT_DNI_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "group_id": "GROUP_DEFENSE_ESCALATION",
      "purpose": "Produce posture, support, readiness, logistics, operational feasibility, force-risk, deterrence, and escalation-pathway analysis.",
      "ordered_eligible_member_ids": [
        "SEAT_DEFENSE",
        "SEAT_CJCS",
        "SEAT_DNI",
        "SEAT_THEATER_COMMANDER"
      ],
      "active_member_rule": "activated_voting_and_advisers",
      "input_entitlement_ids": [
        "INFO_COMMON_CRISIS_PICTURE",
        "INFO_RAW_WEATHER_FORECAST",
        "INFO_CELL_PRODUCTS",
        "INFO_DEFENSE_PRIVATE",
        "INFO_MILITARY_ADVICE_PRIVATE",
        "INFO_INTELLIGENCE_PRIVATE",
        "INFO_THEATER_PRIVATE"
      ],
      "dependency_group_ids": [
        "GROUP_THREAT_ATTRIBUTION"
      ],
      "shared_seat_barrier_ids": [
        "SEAT_DEFENSE",
        "SEAT_CJCS",
        "SEAT_DNI",
        "SEAT_THEATER_COMMANDER"
      ],
      "activation_predicate_id": "ACT_BASELINE_ARENA",
      "product_schema_id": "PRODUCT_DEFENSE_ESCALATION_OPTIONS",
      "collection_order": 40,
      "failure_effect": "missing_required_product",
      "fact_ids": [
        "FACT_DEFENSE_MANDATE",
        "FACT_CJCS_ADVICE_NO_COMMAND",
        "FACT_DNI_MANDATE",
        "FACT_COMBATANT_COMMAND_ROLE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS",
        "INF_WEATHER_SPECIALIST_ROUTE",
        "INF_THEATER_COMMANDER_TRIGGER"
      ]
    },
    {
      "group_id": "GROUP_LEGAL_AUTHORITY",
      "purpose": "Produce an attributable legal and authority record with bases, required consultation, disagreement, missing authority, and inadmissible elements.",
      "ordered_eligible_member_ids": [
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_WHITE_HOUSE_COUNSEL"
      ],
      "active_member_rule": "activated_voting_and_advisers",
      "input_entitlement_ids": [
        "INFO_COMMON_CRISIS_PICTURE",
        "INFO_CELL_PRODUCTS",
        "INFO_LEGAL_PRIVATE",
        "INFO_EOP_LEGAL_PRIVATE"
      ],
      "dependency_group_ids": [
        "GROUP_DIPLOMATIC_ECONOMIC",
        "GROUP_NUCLEAR_RADIOLOGICAL",
        "GROUP_DEFENSE_ESCALATION"
      ],
      "shared_seat_barrier_ids": [
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_WHITE_HOUSE_COUNSEL"
      ],
      "activation_predicate_id": "ACT_LEGAL_AUTHORITY_REVIEW",
      "product_schema_id": "PRODUCT_LEGAL_AUTHORITY_REVIEW",
      "collection_order": 50,
      "failure_effect": "missing_authority_record",
      "fact_ids": [
        "FACT_JUSTICE_MANDATE",
        "FACT_PUBLIC_ADVISER_STATUS"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS",
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "group_id": "GROUP_HOMELAND_CONSEQUENCES",
      "purpose": "Produce domestic exposure, preparedness, critical-infrastructure, border, law-enforcement, and response analysis for supported homeland consequences.",
      "ordered_eligible_member_ids": [
        "SEAT_HOMELAND_SECURITY",
        "SEAT_HSA",
        "SEAT_ATTORNEY_GENERAL"
      ],
      "active_member_rule": "activated_voting_and_advisers",
      "input_entitlement_ids": [
        "INFO_COMMON_CRISIS_PICTURE",
        "INFO_HOMELAND_PRIVATE",
        "INFO_LEGAL_PRIVATE"
      ],
      "dependency_group_ids": [],
      "shared_seat_barrier_ids": [
        "SEAT_HOMELAND_SECURITY",
        "SEAT_HSA",
        "SEAT_ATTORNEY_GENERAL"
      ],
      "activation_predicate_id": "ACT_HOMELAND_CONSEQUENCE",
      "product_schema_id": "PRODUCT_HOMELAND_CONSEQUENCES",
      "collection_order": 60,
      "failure_effect": "missing_required_product",
      "fact_ids": [
        "FACT_DHS_MANDATE",
        "FACT_JUSTICE_MANDATE",
        "FACT_NSC_HSC_FUNCTION"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "group_id": "GROUP_PRESIDENTIAL_SYNTHESIS",
      "purpose": "Integrate attributable specialist products, objectives, dissent, unresolved questions, confidence, legal status, implementation status, and the senior forum route.",
      "ordered_eligible_member_ids": [
        "SEAT_NSA",
        "SEAT_VICE_PRESIDENT",
        "SEAT_CHIEF_OF_STAFF"
      ],
      "active_member_rule": "activated_voting_and_advisers",
      "input_entitlement_ids": [
        "INFO_COMMON_CRISIS_PICTURE",
        "INFO_CELL_PRODUCTS",
        "INFO_ROUTING_STATE"
      ],
      "dependency_group_ids": [
        "GROUP_THREAT_ATTRIBUTION",
        "GROUP_DIPLOMATIC_ECONOMIC",
        "GROUP_NUCLEAR_RADIOLOGICAL",
        "GROUP_DEFENSE_ESCALATION",
        "GROUP_LEGAL_AUTHORITY"
      ],
      "shared_seat_barrier_ids": [
        "SEAT_NSA",
        "SEAT_VICE_PRESIDENT",
        "SEAT_CHIEF_OF_STAFF"
      ],
      "activation_predicate_id": "ACT_SENIOR_DECISION",
      "product_schema_id": "PRODUCT_PRESIDENTIAL_SYNTHESIS",
      "collection_order": 70,
      "failure_effect": "missing_required_product",
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_POLICY_PACKAGE_SCHEMA",
        "INF_WEATHER_SPECIALIST_ROUTE"
      ]
    },
    {
      "group_id": "GROUP_PC",
      "purpose": "Develop one integrated conditional Policy Package, preserve each participant's position, and refer unsupported or presidential matters without chair weight.",
      "ordered_eligible_member_ids": [
        "SEAT_NSA",
        "SEAT_VICE_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_ENERGY",
        "SEAT_PANDEMIC_PREPAREDNESS",
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_INTERIOR",
        "SEAT_CHIEF_OF_STAFF",
        "SEAT_HOMELAND_SECURITY",
        "SEAT_HSA",
        "SEAT_DNI",
        "SEAT_CJCS",
        "SEAT_CIA_DIRECTOR",
        "SEAT_WHITE_HOUSE_COUNSEL",
        "SEAT_POLICY_ASSISTANT",
        "SEAT_COUNSELOR",
        "SEAT_THEATER_COMMANDER"
      ],
      "active_member_rule": "activated_voting_and_advisers",
      "input_entitlement_ids": [
        "INFO_COMMON_CRISIS_PICTURE",
        "INFO_CELL_PRODUCTS",
        "INFO_SYNTHESIS_PRODUCT",
        "INFO_ROUTING_STATE"
      ],
      "dependency_group_ids": [
        "GROUP_PRESIDENTIAL_SYNTHESIS"
      ],
      "shared_seat_barrier_ids": [
        "SEAT_NSA",
        "SEAT_VICE_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_ENERGY",
        "SEAT_PANDEMIC_PREPAREDNESS",
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_INTERIOR",
        "SEAT_CHIEF_OF_STAFF",
        "SEAT_HOMELAND_SECURITY",
        "SEAT_HSA",
        "SEAT_DNI",
        "SEAT_CJCS",
        "SEAT_CIA_DIRECTOR",
        "SEAT_WHITE_HOUSE_COUNSEL",
        "SEAT_POLICY_ASSISTANT",
        "SEAT_THEATER_COMMANDER"
      ],
      "activation_predicate_id": "ACT_SENIOR_DECISION",
      "product_schema_id": "PRODUCT_POLICY_PACKAGE",
      "collection_order": 80,
      "failure_effect": "refer_or_record_no_supported_package",
      "fact_ids": [
        "FACT_PUBLIC_PC_PROCESS",
        "FACT_PUBLIC_EXECUTIVE_SECRETARY"
      ],
      "inference_ids": [
        "INF_POLICY_PACKAGE_SCHEMA",
        "INF_PRESIDENTIAL_ROUTE_SCHEMA",
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "group_id": "GROUP_NSC",
      "purpose": "Provide the President-chaired national-security decision forum for presidential policy and routed PC disagreement.",
      "ordered_eligible_member_ids": [
        "SEAT_PRESIDENT",
        "SEAT_VICE_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_ENERGY",
        "SEAT_PANDEMIC_PREPAREDNESS",
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_INTERIOR",
        "SEAT_CHIEF_OF_STAFF",
        "SEAT_NSA",
        "SEAT_DNI",
        "SEAT_CJCS",
        "SEAT_CIA_DIRECTOR",
        "SEAT_WHITE_HOUSE_COUNSEL",
        "SEAT_POLICY_ASSISTANT",
        "SEAT_THEATER_COMMANDER"
      ],
      "active_member_rule": "activated_voting_and_advisers",
      "input_entitlement_ids": [
        "INFO_COMMON_CRISIS_PICTURE",
        "INFO_SYNTHESIS_PRODUCT",
        "INFO_POLICY_PACKAGE",
        "INFO_ROUTING_STATE",
        "INFO_RETRIEVED_UNDERLYING"
      ],
      "dependency_group_ids": [
        "GROUP_PC"
      ],
      "shared_seat_barrier_ids": [
        "SEAT_PRESIDENT",
        "SEAT_VICE_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_ENERGY",
        "SEAT_PANDEMIC_PREPAREDNESS",
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_INTERIOR",
        "SEAT_CHIEF_OF_STAFF",
        "SEAT_NSA",
        "SEAT_DNI",
        "SEAT_CJCS",
        "SEAT_CIA_DIRECTOR",
        "SEAT_WHITE_HOUSE_COUNSEL",
        "SEAT_POLICY_ASSISTANT",
        "SEAT_THEATER_COMMANDER"
      ],
      "activation_predicate_id": "ACT_PRESIDENTIAL_POLICY",
      "product_schema_id": "PRODUCT_NSC_DECISION_RECORD",
      "collection_order": 90,
      "failure_effect": "no_supported_decision",
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
        "FACT_PUBLIC_ADVISER_STATUS",
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_PRESIDENTIAL_ROUTE_SCHEMA",
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "group_id": "GROUP_HSC",
      "purpose": "Provide the President-chaired homeland-security decision forum when the NSC convenes as the HSC.",
      "ordered_eligible_member_ids": [
        "SEAT_PRESIDENT",
        "SEAT_VICE_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_ENERGY",
        "SEAT_PANDEMIC_PREPAREDNESS",
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_INTERIOR",
        "SEAT_CHIEF_OF_STAFF",
        "SEAT_NSA",
        "SEAT_HOMELAND_SECURITY",
        "SEAT_HSA",
        "SEAT_DNI",
        "SEAT_CJCS",
        "SEAT_CIA_DIRECTOR",
        "SEAT_WHITE_HOUSE_COUNSEL",
        "SEAT_POLICY_ASSISTANT"
      ],
      "active_member_rule": "activated_voting_and_advisers",
      "input_entitlement_ids": [
        "INFO_COMMON_CRISIS_PICTURE",
        "INFO_CELL_PRODUCTS",
        "INFO_SYNTHESIS_PRODUCT",
        "INFO_POLICY_PACKAGE",
        "INFO_ROUTING_STATE",
        "INFO_RETRIEVED_UNDERLYING"
      ],
      "dependency_group_ids": [
        "GROUP_HOMELAND_CONSEQUENCES",
        "GROUP_PC"
      ],
      "shared_seat_barrier_ids": [
        "SEAT_PRESIDENT",
        "SEAT_VICE_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_ENERGY",
        "SEAT_PANDEMIC_PREPAREDNESS",
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_INTERIOR",
        "SEAT_CHIEF_OF_STAFF",
        "SEAT_NSA",
        "SEAT_HOMELAND_SECURITY",
        "SEAT_HSA",
        "SEAT_DNI",
        "SEAT_CJCS",
        "SEAT_CIA_DIRECTOR",
        "SEAT_WHITE_HOUSE_COUNSEL",
        "SEAT_POLICY_ASSISTANT"
      ],
      "activation_predicate_id": "ACT_HOMELAND_CONSEQUENCE",
      "product_schema_id": "PRODUCT_HSC_DECISION_RECORD",
      "collection_order": 90,
      "failure_effect": "no_supported_decision",
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_PUBLIC_COUNCIL_MEMBERSHIP",
        "FACT_PUBLIC_ADVISER_STATUS",
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_PRESIDENTIAL_ROUTE_SCHEMA",
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    }
  ],
  "information_classes": [
    {
      "information_class_id": "INFO_COMMON_CRISIS_PICTURE",
      "description": "Common synthetic facts and admitted observations available to every active seat, including the Cycle 2 confirmation but excluding hidden World truth and the Cycle 1 raw forecast.",
      "sensitivity": "common",
      "fact_ids": [],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_RAW_WEATHER_FORECAST",
      "description": "The unchanged Cycle 1 forecast delivered only to the authorized Threat and Attribution and Defense and Escalation participants.",
      "sensitivity": "seat_private",
      "fact_ids": [],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS",
        "INF_WEATHER_SPECIALIST_ROUTE"
      ]
    },
    {
      "information_class_id": "INFO_INTELLIGENCE_PRIVATE",
      "description": "Synthetic all-source evidence, confidence, alternatives, collection gaps, and intelligence disagreements for the DNI seat.",
      "sensitivity": "seat_private",
      "fact_ids": [
        "FACT_DNI_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_FOREIGN_SOURCE_PRIVATE",
      "description": "Synthetic foreign-source reporting, leadership assessment, access, and source-risk information for the CIA seat.",
      "sensitivity": "seat_private",
      "fact_ids": [
        "FACT_CIA_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_DIPLOMATIC_PRIVATE",
      "description": "Synthetic diplomatic reporting, requests, positions, and available channels for the State seat.",
      "sensitivity": "seat_private",
      "fact_ids": [
        "FACT_STATE_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_FINANCIAL_PRIVATE",
      "description": "Synthetic finance, trade, sanctions, market, and implementation information for the Treasury seat.",
      "sensitivity": "seat_private",
      "fact_ids": [
        "FACT_TREASURY_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_DEFENSE_PRIVATE",
      "description": "Synthetic posture, readiness, logistics, support-capacity, and civilian defense-policy constraints for the Defense seat.",
      "sensitivity": "seat_private",
      "fact_ids": [
        "FACT_DEFENSE_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_NUCLEAR_PRIVATE",
      "description": "Synthetic nuclear-security, radiological, stockpile, energy-flow, and emergency-response information for the Energy seat.",
      "sensitivity": "seat_private",
      "fact_ids": [
        "FACT_ENERGY_NUCLEAR_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_LEGAL_PRIVATE",
      "description": "Synthetic departmental authority records, proposed actions, law-enforcement facts, and legal analysis for the Attorney General seat.",
      "sensitivity": "seat_private",
      "fact_ids": [
        "FACT_JUSTICE_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_EOP_LEGAL_PRIVATE",
      "description": "Synthetic presidential-action, process-record, and Executive Office legal information for the White House Counsel seat.",
      "sensitivity": "seat_private",
      "fact_ids": [
        "FACT_PUBLIC_ADVISER_STATUS"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_INTERIOR_PRIVATE",
      "description": "Synthetic affected-territory, resource, land, trust, and community information for the Interior seat.",
      "sensitivity": "seat_private",
      "fact_ids": [
        "FACT_INTERIOR_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_HOMELAND_PRIVATE",
      "description": "Synthetic domestic threat, critical-infrastructure, border, cyber-consequence, and response-capacity information for homeland seats.",
      "sensitivity": "seat_private",
      "fact_ids": [
        "FACT_DHS_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_BIO_PRIVATE",
      "description": "Synthetic biological-threat, preparedness, and response-capacity information for the pandemic-preparedness seat.",
      "sensitivity": "seat_private",
      "fact_ids": [
        "FACT_PANDEMIC_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_MILITARY_ADVICE_PRIVATE",
      "description": "Synthetic joint-force requirements, feasibility, risks, and commander views for the CJCS seat.",
      "sensitivity": "seat_private",
      "fact_ids": [
        "FACT_CJCS_ADVICE_NO_COMMAND"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_THEATER_PRIVATE",
      "description": "Synthetic AOR, mission, resources, access, readiness, logistics, timing, and constraints for the functional Theater Commander seat.",
      "sensitivity": "seat_private",
      "fact_ids": [
        "FACT_COMBATANT_COMMAND_ROLE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS",
        "INF_THEATER_COMMANDER_TRIGGER"
      ]
    },
    {
      "information_class_id": "INFO_CELL_PRODUCTS",
      "description": "Attributable specialist-group products with evidence links, confidence, dissent, and unresolved questions.",
      "sensitivity": "group_product",
      "fact_ids": [],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH"
      ]
    },
    {
      "information_class_id": "INFO_SYNTHESIS_PRODUCT",
      "description": "The attributable Presidential Synthesis product containing integrated options, dissent, unresolved questions, and route status.",
      "sensitivity": "group_product",
      "fact_ids": [
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_POLICY_PACKAGE_SCHEMA"
      ]
    },
    {
      "information_class_id": "INFO_POLICY_PACKAGE",
      "description": "The versioned integrated conditional Policy Package produced by the PC with domain dispositions and no implied World effect.",
      "sensitivity": "group_product",
      "fact_ids": [
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_POLICY_PACKAGE_SCHEMA"
      ]
    },
    {
      "information_class_id": "INFO_DECISION_RECORD",
      "description": "The exact final decision, nondecision, tasking, dissent, confirmation, and failure record communicated by the Executive Secretary.",
      "sensitivity": "group_product",
      "fact_ids": [
        "FACT_PUBLIC_EXECUTIVE_SECRETARY"
      ],
      "inference_ids": [
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "information_class_id": "INFO_ROUTING_STATE",
      "description": "Deterministic activation, dependency, consensus, presidential-attention, consultation, confirmation, and referral state.",
      "sensitivity": "group_product",
      "fact_ids": [
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_PRESIDENTIAL_ROUTE_SCHEMA",
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "information_class_id": "INFO_RETRIEVED_UNDERLYING",
      "description": "A logged, scope-bounded retrieval of an underlying synthetic brief already authorized by the Charter.",
      "sensitivity": "underlying_retrieval",
      "fact_ids": [],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "information_class_id": "INFO_WORLD_GROUND_TRUTH",
      "description": "Hidden World truth that is never a Room seat entitlement and has no disclosure permission.",
      "sensitivity": "world_ground_truth",
      "fact_ids": [],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    }
  ],
  "disclosure_permissions": [
    {
      "permission_id": "PERMISSION_COMMON_ACTIVE_SEATS",
      "information_class_id": "INFO_COMMON_CRISIS_PICTURE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_PRESIDENT",
        "SEAT_VICE_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_ENERGY",
        "SEAT_PANDEMIC_PREPAREDNESS",
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_INTERIOR",
        "SEAT_CHIEF_OF_STAFF",
        "SEAT_NSA",
        "SEAT_HOMELAND_SECURITY",
        "SEAT_HSA",
        "SEAT_DNI",
        "SEAT_CJCS",
        "SEAT_CIA_DIRECTOR",
        "SEAT_WHITE_HOUSE_COUNSEL",
        "SEAT_POLICY_ASSISTANT",
        "SEAT_COUNSELOR",
        "SEAT_THEATER_COMMANDER"
      ],
      "delivery_mode": "direct",
      "fact_ids": [],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_RAW_FORECAST_SPECIALISTS",
      "information_class_id": "INFO_RAW_WEATHER_FORECAST",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "GROUP_THREAT_ATTRIBUTION",
        "GROUP_DEFENSE_ESCALATION"
      ],
      "delivery_mode": "group_delivery",
      "fact_ids": [],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS",
        "INF_WEATHER_SPECIALIST_ROUTE"
      ]
    },
    {
      "permission_id": "PERMISSION_DNI_PRIVATE",
      "information_class_id": "INFO_INTELLIGENCE_PRIVATE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_DNI"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_DNI_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_CIA_PRIVATE",
      "information_class_id": "INFO_FOREIGN_SOURCE_PRIVATE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_CIA_DIRECTOR"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_CIA_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_STATE_PRIVATE",
      "information_class_id": "INFO_DIPLOMATIC_PRIVATE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_STATE"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_STATE_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_TREASURY_PRIVATE",
      "information_class_id": "INFO_FINANCIAL_PRIVATE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_TREASURY"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_TREASURY_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_DEFENSE_PRIVATE",
      "information_class_id": "INFO_DEFENSE_PRIVATE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_DEFENSE"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_DEFENSE_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_ENERGY_PRIVATE",
      "information_class_id": "INFO_NUCLEAR_PRIVATE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_ENERGY"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_ENERGY_NUCLEAR_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_JUSTICE_PRIVATE",
      "information_class_id": "INFO_LEGAL_PRIVATE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_ATTORNEY_GENERAL"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_JUSTICE_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_EOP_LEGAL_PRIVATE",
      "information_class_id": "INFO_EOP_LEGAL_PRIVATE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_WHITE_HOUSE_COUNSEL"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_PUBLIC_ADVISER_STATUS"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_INTERIOR_PRIVATE",
      "information_class_id": "INFO_INTERIOR_PRIVATE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_INTERIOR"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_INTERIOR_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_HOMELAND_PRIVATE",
      "information_class_id": "INFO_HOMELAND_PRIVATE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_HOMELAND_SECURITY",
        "SEAT_HSA"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_DHS_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_BIO_PRIVATE",
      "information_class_id": "INFO_BIO_PRIVATE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_PANDEMIC_PREPAREDNESS"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_PANDEMIC_MANDATE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_CJCS_PRIVATE",
      "information_class_id": "INFO_MILITARY_ADVICE_PRIVATE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_CJCS"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_CJCS_ADVICE_NO_COMMAND"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_THEATER_PRIVATE",
      "information_class_id": "INFO_THEATER_PRIVATE",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_THEATER_COMMANDER"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_COMBATANT_COMMAND_ROLE"
      ],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS",
        "INF_THEATER_COMMANDER_TRIGGER"
      ]
    },
    {
      "permission_id": "PERMISSION_CELL_PRODUCTS_TO_SYNTHESIS",
      "information_class_id": "INFO_CELL_PRODUCTS",
      "sender_ids": [
        "GROUP_THREAT_ATTRIBUTION",
        "GROUP_DIPLOMATIC_ECONOMIC",
        "GROUP_NUCLEAR_RADIOLOGICAL",
        "GROUP_DEFENSE_ESCALATION",
        "GROUP_LEGAL_AUTHORITY",
        "GROUP_HOMELAND_CONSEQUENCES"
      ],
      "recipient_ids": [
        "GROUP_PRESIDENTIAL_SYNTHESIS"
      ],
      "delivery_mode": "group_delivery",
      "fact_ids": [],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_SYNTHETIC_ENTITLEMENTS"
      ]
    },
    {
      "permission_id": "PERMISSION_SYNTHESIS_TO_PC",
      "information_class_id": "INFO_SYNTHESIS_PRODUCT",
      "sender_ids": [
        "GROUP_PRESIDENTIAL_SYNTHESIS"
      ],
      "recipient_ids": [
        "GROUP_PC"
      ],
      "delivery_mode": "group_delivery",
      "fact_ids": [
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_POLICY_PACKAGE_SCHEMA"
      ]
    },
    {
      "permission_id": "PERMISSION_POLICY_PACKAGE_TO_COUNCILS",
      "information_class_id": "INFO_POLICY_PACKAGE",
      "sender_ids": [
        "GROUP_PC"
      ],
      "recipient_ids": [
        "GROUP_NSC",
        "GROUP_HSC"
      ],
      "delivery_mode": "group_delivery",
      "fact_ids": [
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_POLICY_PACKAGE_SCHEMA",
        "INF_PRESIDENTIAL_ROUTE_SCHEMA"
      ]
    },
    {
      "permission_id": "PERMISSION_DECISION_RECORD",
      "information_class_id": "INFO_DECISION_RECORD",
      "sender_ids": [
        "SERVICE_EXECUTIVE_SECRETARY"
      ],
      "recipient_ids": [
        "SEAT_PRESIDENT",
        "SEAT_VICE_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_ENERGY",
        "SEAT_PANDEMIC_PREPAREDNESS",
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_INTERIOR",
        "SEAT_CHIEF_OF_STAFF",
        "SEAT_NSA",
        "SEAT_HOMELAND_SECURITY",
        "SEAT_HSA",
        "SEAT_DNI",
        "SEAT_CJCS",
        "SEAT_CIA_DIRECTOR",
        "SEAT_WHITE_HOUSE_COUNSEL",
        "SEAT_POLICY_ASSISTANT",
        "SEAT_COUNSELOR",
        "SEAT_THEATER_COMMANDER"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_PUBLIC_EXECUTIVE_SECRETARY"
      ],
      "inference_ids": [
        "INF_DETERMINISTIC_EXECUTIVE_SECRETARY",
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "permission_id": "PERMISSION_ROUTING_STATE",
      "information_class_id": "INFO_ROUTING_STATE",
      "sender_ids": [
        "SERVICE_EXECUTIVE_SECRETARY"
      ],
      "recipient_ids": [
        "SEAT_NSA",
        "SEAT_CHIEF_OF_STAFF",
        "SEAT_HSA"
      ],
      "delivery_mode": "direct",
      "fact_ids": [
        "FACT_PUBLIC_PC_PROCESS",
        "FACT_PUBLIC_EXECUTIVE_SECRETARY"
      ],
      "inference_ids": [
        "INF_PRESIDENTIAL_ROUTE_SCHEMA",
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "permission_id": "PERMISSION_LOGGED_UNDERLYING_RETRIEVAL",
      "information_class_id": "INFO_RETRIEVED_UNDERLYING",
      "sender_ids": [
        "SERVICE_WATCH"
      ],
      "recipient_ids": [
        "SEAT_PRESIDENT",
        "SEAT_NSA",
        "SEAT_HSA"
      ],
      "delivery_mode": "logged_retrieval",
      "fact_ids": [],
      "inference_ids": [
        "INF_SYNTHETIC_ENTITLEMENTS",
        "INF_WEATHER_SPECIALIST_ROUTE"
      ]
    }
  ],
  "activation_predicates": [
    {
      "activation_predicate_id": "ACT_EVERY_NATIONAL_SECURITY_CYCLE",
      "predicate_type": "always",
      "condition_ids": [],
      "first_episode_value": true,
      "description": "Active for every national-security Room cycle and deterministic service invocation.",
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION"
      ],
      "inference_ids": [
        "INF_FIRST_EPISODE_ACTIVATION"
      ]
    },
    {
      "activation_predicate_id": "ACT_BASELINE_ARENA",
      "predicate_type": "episode_relevance",
      "condition_ids": [
        "CONDITION_FOREIGN_BORDER_CRISIS",
        "CONDITION_US_SUPPORT_REQUEST"
      ],
      "first_episode_value": true,
      "description": "The conventional Himaldesh-Olvana border crisis and support request make the core foreign-policy, defense, and intelligence contributions relevant.",
      "fact_ids": [
        "FACT_DATED_PUBLIC_POSTURE"
      ],
      "inference_ids": [
        "INF_FIRST_EPISODE_ACTIVATION"
      ]
    },
    {
      "activation_predicate_id": "ACT_SENIOR_DECISION",
      "predicate_type": "episode_relevance",
      "condition_ids": [
        "CONDITION_POLICY_PACKAGE_DUE"
      ],
      "first_episode_value": true,
      "description": "The first episode requires an integrated senior Policy Package before the partner decision clock.",
      "fact_ids": [
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_FIRST_EPISODE_ACTIVATION",
        "INF_POLICY_PACKAGE_SCHEMA"
      ]
    },
    {
      "activation_predicate_id": "ACT_PRESIDENTIAL_POLICY",
      "predicate_type": "episode_relevance",
      "condition_ids": [
        "CONDITION_NO_VERIFIED_DELEGATION",
        "CONDITION_PRESIDENTIAL_POLICY_DIRECTION"
      ],
      "first_episode_value": true,
      "description": "The candidate contains no crisis-specific delegation, so the first supported final policy direction is presidential and routes to the NSC.",
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_FIRST_EPISODE_ACTIVATION",
        "INF_PRESIDENTIAL_ROUTE_SCHEMA"
      ]
    },
    {
      "activation_predicate_id": "ACT_ECONOMIC_EXPOSURE",
      "predicate_type": "episode_relevance",
      "condition_ids": [
        "CONDITION_TARGETED_ECONOMIC_PRESSURE_REQUESTED"
      ],
      "first_episode_value": true,
      "description": "The partner request and Policy Package require a disposition on targeted economic and financial measures.",
      "fact_ids": [
        "FACT_TREASURY_MANDATE"
      ],
      "inference_ids": [
        "INF_FIRST_EPISODE_ACTIVATION",
        "INF_POLICY_PACKAGE_SCHEMA"
      ]
    },
    {
      "activation_predicate_id": "ACT_NUCLEAR_RISK",
      "predicate_type": "episode_relevance",
      "condition_ids": [
        "CONDITION_NUCLEAR_ESCALATION_REACHABLE"
      ],
      "first_episode_value": true,
      "description": "The conventional crisis has a reachable nuclear-escalation path and requires technical and strategic-risk analysis without scripting use.",
      "fact_ids": [
        "FACT_ENERGY_NUCLEAR_MANDATE",
        "FACT_DATED_PUBLIC_POSTURE"
      ],
      "inference_ids": [
        "INF_FIRST_EPISODE_ACTIVATION"
      ]
    },
    {
      "activation_predicate_id": "ACT_LEGAL_AUTHORITY_REVIEW",
      "predicate_type": "episode_relevance",
      "condition_ids": [
        "CONDITION_POLICY_COMPONENTS_REQUIRE_AUTHORITY_RECORD"
      ],
      "first_episode_value": true,
      "description": "The integrated package must record legal bases, consultations, unresolved disagreement, and unsupported elements before a final route can be supported.",
      "fact_ids": [
        "FACT_JUSTICE_MANDATE",
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_FIRST_EPISODE_ACTIVATION",
        "INF_POLICY_PACKAGE_SCHEMA",
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "activation_predicate_id": "ACT_THEATER_OPERATIONAL_RISK",
      "predicate_type": "episode_relevance",
      "condition_ids": [
        "CONDITION_US_ISR_WINDOW_AT_RISK",
        "CONDITION_HIMALDESHI_SUPPORT_WINDOW_AT_RISK"
      ],
      "first_episode_value": true,
      "description": "The paired weather risk materially affects synthetic observation, access, logistics, support, readiness, and force-protection questions.",
      "fact_ids": [
        "FACT_CJCS_ADVICE_NO_COMMAND",
        "FACT_COMBATANT_COMMAND_ROLE"
      ],
      "inference_ids": [
        "INF_FIRST_EPISODE_ACTIVATION",
        "INF_WEATHER_SPECIALIST_ROUTE",
        "INF_THEATER_COMMANDER_TRIGGER"
      ]
    },
    {
      "activation_predicate_id": "ACT_HOMELAND_CONSEQUENCE",
      "predicate_type": "episode_relevance",
      "condition_ids": [
        "CONDITION_MATERIAL_US_HOMELAND_CONSEQUENCE"
      ],
      "first_episode_value": false,
      "description": "Activates only for a material supported homeland, border, infrastructure, domestic-response, or cyber consequence; none is present in the first episode baseline.",
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_DHS_MANDATE"
      ],
      "inference_ids": [
        "INF_FIRST_EPISODE_ACTIVATION"
      ]
    },
    {
      "activation_predicate_id": "ACT_BIOLOGICAL_THREAT",
      "predicate_type": "episode_relevance",
      "condition_ids": [
        "CONDITION_BIOLOGICAL_OR_PANDEMIC_THREAT"
      ],
      "first_episode_value": false,
      "description": "Activates only for a supported biological or pandemic threat; none is present in the first episode baseline.",
      "fact_ids": [
        "FACT_PANDEMIC_MANDATE"
      ],
      "inference_ids": [
        "INF_FIRST_EPISODE_ACTIVATION"
      ]
    },
    {
      "activation_predicate_id": "ACT_INTERIOR_INTEREST",
      "predicate_type": "episode_relevance",
      "condition_ids": [
        "CONDITION_US_INTERIOR_INTEREST"
      ],
      "first_episode_value": false,
      "description": "Activates only when supported U.S. territory, lands, resources, trust responsibilities, or communities are materially affected; none is present in the baseline.",
      "fact_ids": [
        "FACT_INTERIOR_MANDATE"
      ],
      "inference_ids": [
        "INF_FIRST_EPISODE_ACTIVATION"
      ]
    },
    {
      "activation_predicate_id": "ACT_ADDITIONAL_INVITEE_MANDATE",
      "predicate_type": "all_of",
      "condition_ids": [
        "CONDITION_PUBLIC_PORTFOLIO_SOURCE",
        "CONDITION_EPISODE_RELEVANCE"
      ],
      "first_episode_value": false,
      "description": "Requires both an additional public portfolio source and supported episode relevance; neither invitee receives a generic mandate in this candidate.",
      "fact_ids": [
        "FACT_PUBLIC_ADVISER_STATUS"
      ],
      "inference_ids": [
        "INF_FIRST_EPISODE_ACTIVATION"
      ]
    }
  ],
  "decision_routes": [
    {
      "route_id": "ROUTE_PRESIDENTIAL_POLICY",
      "action_class": "presidential_policy_direction",
      "applicability_predicate_id": "ACT_PRESIDENTIAL_POLICY",
      "owning_authority_seat_id": "SEAT_PRESIDENT",
      "eligible_forum_group_id": "GROUP_NSC",
      "decision_rule": "president_decides",
      "presidential_attention_rule": "required",
      "consultation_group_ids": [
        "GROUP_PC",
        "GROUP_LEGAL_AUTHORITY"
      ],
      "required_confirmation_ids": [
        "CONFIRM_NSC_PRESIDENTIAL_DECISION",
        "CONFIRM_NSC_AUTHORITY_RECORD"
      ],
      "final_decision_record_schema_id": "PRODUCT_NSC_DECISION_RECORD",
      "failure_effect": "no_supported_decision_and_no_world_effect",
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_PRESIDENTIAL_ROUTE_SCHEMA",
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "route_id": "ROUTE_PRESIDENTIAL_HOMELAND_POLICY",
      "action_class": "presidential_homeland_policy_direction",
      "applicability_predicate_id": "ACT_HOMELAND_CONSEQUENCE",
      "owning_authority_seat_id": "SEAT_PRESIDENT",
      "eligible_forum_group_id": "GROUP_HSC",
      "decision_rule": "president_decides",
      "presidential_attention_rule": "required",
      "consultation_group_ids": [
        "GROUP_PC",
        "GROUP_HOMELAND_CONSEQUENCES",
        "GROUP_LEGAL_AUTHORITY"
      ],
      "required_confirmation_ids": [
        "CONFIRM_HSC_PRESIDENTIAL_DECISION",
        "CONFIRM_HSC_AUTHORITY_RECORD"
      ],
      "final_decision_record_schema_id": "PRODUCT_HSC_DECISION_RECORD",
      "failure_effect": "no_supported_decision_and_no_world_effect",
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_PRESIDENTIAL_ROUTE_SCHEMA",
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    }
  ],
  "required_confirmations": [
    {
      "confirmation_id": "CONFIRM_NSC_PRESIDENTIAL_DECISION",
      "description": "The President confirms the exact NSC presidential decision record; this confirmation does not validate downstream effect-level authority or capability.",
      "requester_seat_id": "SEAT_NSA",
      "confirmer_seat_ids": [
        "SEAT_PRESIDENT"
      ],
      "applicability_predicate_id": "ACT_PRESIDENTIAL_POLICY",
      "failure_effect": "no_supported_decision_and_no_world_effect",
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_PUBLIC_EXECUTIVE_SECRETARY"
      ],
      "inference_ids": [
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "confirmation_id": "CONFIRM_NSC_AUTHORITY_RECORD",
      "description": "The Attorney General and White House Counsel confirm that the legal basis, missing authority, required consultation, and any disagreement are recorded, without expressing a policy vote.",
      "requester_seat_id": "SEAT_NSA",
      "confirmer_seat_ids": [
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_WHITE_HOUSE_COUNSEL"
      ],
      "applicability_predicate_id": "ACT_LEGAL_AUTHORITY_REVIEW",
      "failure_effect": "no_supported_decision_and_no_world_effect",
      "fact_ids": [
        "FACT_JUSTICE_MANDATE",
        "FACT_PUBLIC_ADVISER_STATUS"
      ],
      "inference_ids": [
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "confirmation_id": "CONFIRM_HSC_PRESIDENTIAL_DECISION",
      "description": "The President confirms the exact HSC presidential decision record; this confirmation does not validate downstream effect-level authority or capability.",
      "requester_seat_id": "SEAT_HSA",
      "confirmer_seat_ids": [
        "SEAT_PRESIDENT"
      ],
      "applicability_predicate_id": "ACT_HOMELAND_CONSEQUENCE",
      "failure_effect": "no_supported_decision_and_no_world_effect",
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_PUBLIC_EXECUTIVE_SECRETARY"
      ],
      "inference_ids": [
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "confirmation_id": "CONFIRM_HSC_AUTHORITY_RECORD",
      "description": "The Attorney General and White House Counsel confirm that the HSC legal basis, missing authority, required consultation, and any disagreement are recorded, without expressing a policy vote.",
      "requester_seat_id": "SEAT_HSA",
      "confirmer_seat_ids": [
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_WHITE_HOUSE_COUNSEL"
      ],
      "applicability_predicate_id": "ACT_HOMELAND_CONSEQUENCE",
      "failure_effect": "no_supported_decision_and_no_world_effect",
      "fact_ids": [
        "FACT_JUSTICE_MANDATE",
        "FACT_PUBLIC_ADVISER_STATUS"
      ],
      "inference_ids": [
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    }
  ],
  "product_schemas": [
    {
      "product_schema_id": "PRODUCT_THREAT_ASSESSMENT",
      "product_type": "threat_and_attribution_assessment",
      "producing_group_ids": [
        "GROUP_THREAT_ATTRIBUTION"
      ],
      "required_fields": [
        "hypotheses",
        "confidence",
        "alternatives",
        "gaps",
        "warning",
        "attribution_limits",
        "us_observation_window",
        "material_dissent",
        "source_fact_ids"
      ],
      "preserves_dissent": true,
      "fact_ids": [
        "FACT_DNI_MANDATE",
        "FACT_CIA_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_WEATHER_SPECIALIST_ROUTE"
      ]
    },
    {
      "product_schema_id": "PRODUCT_DIPLOMATIC_ECONOMIC_OPTIONS",
      "product_type": "diplomatic_and_economic_options",
      "producing_group_ids": [
        "GROUP_DIPLOMATIC_ECONOMIC"
      ],
      "required_fields": [
        "negotiation_options",
        "private_and_public_signaling",
        "partner_support",
        "financial_and_trade_options",
        "humanitarian_considerations",
        "unsupported_commitment_checks",
        "implementation_constraints",
        "material_dissent",
        "source_fact_ids"
      ],
      "preserves_dissent": true,
      "fact_ids": [
        "FACT_STATE_MANDATE",
        "FACT_TREASURY_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH"
      ]
    },
    {
      "product_schema_id": "PRODUCT_NUCLEAR_RADIOLOGICAL_ASSESSMENT",
      "product_type": "nuclear_and_radiological_assessment",
      "producing_group_ids": [
        "GROUP_NUCLEAR_RADIOLOGICAL"
      ],
      "required_fields": [
        "technical_status",
        "warning_and_ambiguity",
        "deterrence_implications",
        "escalation_pathways",
        "emergency_options",
        "authority_limits",
        "material_dissent",
        "source_fact_ids"
      ],
      "preserves_dissent": true,
      "fact_ids": [
        "FACT_ENERGY_NUCLEAR_MANDATE",
        "FACT_CJCS_ADVICE_NO_COMMAND",
        "FACT_DNI_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH"
      ]
    },
    {
      "product_schema_id": "PRODUCT_DEFENSE_ESCALATION_OPTIONS",
      "product_type": "defense_and_escalation_options",
      "producing_group_ids": [
        "GROUP_DEFENSE_ESCALATION"
      ],
      "required_fields": [
        "posture_and_readiness",
        "support_options",
        "operational_feasibility",
        "logistics_and_timing",
        "force_protection",
        "himaldeshi_support_window",
        "deterrence_and_escalation_pathways",
        "no_combat_authority_statement",
        "material_dissent",
        "source_fact_ids"
      ],
      "preserves_dissent": true,
      "fact_ids": [
        "FACT_DEFENSE_MANDATE",
        "FACT_CJCS_ADVICE_NO_COMMAND",
        "FACT_COMBATANT_COMMAND_ROLE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_WEATHER_SPECIALIST_ROUTE",
        "INF_THEATER_COMMANDER_TRIGGER"
      ]
    },
    {
      "product_schema_id": "PRODUCT_LEGAL_AUTHORITY_REVIEW",
      "product_type": "legal_and_authority_record",
      "producing_group_ids": [
        "GROUP_LEGAL_AUTHORITY"
      ],
      "required_fields": [
        "proposed_component_ids",
        "legal_basis_by_component",
        "owning_authority_by_component",
        "required_consultations",
        "missing_authority",
        "inadmissible_elements",
        "legal_disagreement",
        "record_completeness",
        "source_fact_ids"
      ],
      "preserves_dissent": true,
      "fact_ids": [
        "FACT_JUSTICE_MANDATE",
        "FACT_PUBLIC_ADVISER_STATUS"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "product_schema_id": "PRODUCT_HOMELAND_CONSEQUENCES",
      "product_type": "homeland_consequence_assessment",
      "producing_group_ids": [
        "GROUP_HOMELAND_CONSEQUENCES"
      ],
      "required_fields": [
        "domestic_exposure",
        "preparedness",
        "critical_infrastructure",
        "border_and_law_enforcement",
        "response_options",
        "authority_limits",
        "material_dissent",
        "source_fact_ids"
      ],
      "preserves_dissent": true,
      "fact_ids": [
        "FACT_DHS_MANDATE",
        "FACT_JUSTICE_MANDATE"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH"
      ]
    },
    {
      "product_schema_id": "PRODUCT_PRESIDENTIAL_SYNTHESIS",
      "product_type": "presidential_synthesis",
      "producing_group_ids": [
        "GROUP_PRESIDENTIAL_SYNTHESIS"
      ],
      "required_fields": [
        "desired_end_state",
        "objective_ids",
        "integrated_options",
        "evidence_and_confidence",
        "material_dissent",
        "unresolved_questions",
        "legal_status",
        "implementation_status",
        "recommended_forum_route",
        "source_fact_ids"
      ],
      "preserves_dissent": true,
      "fact_ids": [
        "FACT_PUBLIC_PC_PROCESS"
      ],
      "inference_ids": [
        "INF_SPECIALIST_GROUP_GRAPH",
        "INF_POLICY_PACKAGE_SCHEMA",
        "INF_WEATHER_SPECIALIST_ROUTE"
      ]
    },
    {
      "product_schema_id": "PRODUCT_POLICY_PACKAGE",
      "product_type": "integrated_conditional_policy_package",
      "producing_group_ids": [
        "GROUP_PC"
      ],
      "required_fields": [
        "package_version",
        "desired_end_state",
        "objective_ids",
        "evidence_basis",
        "current_assessment",
        "competing_hypotheses",
        "confidence_and_gaps",
        "components",
        "triggers_sequence_timing_dependencies",
        "authority_consultation_confirmation_safeguards",
        "domain_dispositions",
        "principal_policy_positions",
        "principal_attention_positions",
        "material_dissent",
        "dissent_disposition",
        "decision_or_return_record",
        "reassessment_point",
        "source_fact_ids"
      ],
      "preserves_dissent": true,
      "fact_ids": [
        "FACT_PUBLIC_PC_PROCESS",
        "FACT_PUBLIC_EXECUTIVE_SECRETARY"
      ],
      "inference_ids": [
        "INF_POLICY_PACKAGE_SCHEMA",
        "INF_PRESIDENTIAL_ROUTE_SCHEMA"
      ]
    },
    {
      "product_schema_id": "PRODUCT_NSC_DECISION_RECORD",
      "product_type": "presidential_national_security_decision_record",
      "producing_group_ids": [
        "GROUP_NSC"
      ],
      "required_fields": [
        "route_id",
        "policy_package_id",
        "presidential_decision",
        "decided_components",
        "returned_or_rejected_components",
        "required_confirmations",
        "consultations",
        "material_dissent",
        "what_was_not_decided",
        "taskings",
        "reassessment_point",
        "failure_records",
        "source_fact_ids"
      ],
      "preserves_dissent": true,
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_PUBLIC_PC_PROCESS",
        "FACT_PUBLIC_EXECUTIVE_SECRETARY"
      ],
      "inference_ids": [
        "INF_PRESIDENTIAL_ROUTE_SCHEMA",
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    },
    {
      "product_schema_id": "PRODUCT_HSC_DECISION_RECORD",
      "product_type": "presidential_homeland_security_decision_record",
      "producing_group_ids": [
        "GROUP_HSC"
      ],
      "required_fields": [
        "route_id",
        "policy_package_id",
        "presidential_decision",
        "decided_components",
        "returned_or_rejected_components",
        "required_confirmations",
        "consultations",
        "material_dissent",
        "what_was_not_decided",
        "taskings",
        "reassessment_point",
        "failure_records",
        "source_fact_ids"
      ],
      "preserves_dissent": true,
      "fact_ids": [
        "FACT_NSC_HSC_FUNCTION",
        "FACT_PUBLIC_PC_PROCESS",
        "FACT_PUBLIC_EXECUTIVE_SECRETARY"
      ],
      "inference_ids": [
        "INF_PRESIDENTIAL_ROUTE_SCHEMA",
        "INF_REQUIRED_CONFIRMATION_SCHEMA"
      ]
    }
  ],
  "evidence_labels": [
    {
      "evidence_label_id": "EVIDENCE_FACT",
      "label": "FACT",
      "description": "A bounded claim directly supported by one or more public official sources in the bound source register."
    },
    {
      "evidence_label_id": "EVIDENCE_INFERENCE",
      "label": "INFERENCE",
      "description": "A declared exercise-design choice inferred from public facts and never presented as official procedure."
    },
    {
      "evidence_label_id": "EVIDENCE_GAP",
      "label": "GAP",
      "description": "A missing source, authority, mandate, or fidelity boundary retained explicitly rather than repaired by analogy."
    }
  ]
}
```
