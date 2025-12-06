# OEP Terminology

This document defines the core vocabulary used throughout the  
Open Epistemic Protocol (OEP). All specifications, validators,  
and extensions must rely on these definitions.

---

## 1. access

A binary indicator of whether the system has legitimate, authorized,  
auditable visibility into a piece of information.

`access = true` only when information is:

- directly supplied by the user  
- fetched through an explicit and documented API or data source  
- contained within a validated, recorded input channel  

All other domains default to `access = false`.

---

## 2. awareness

A narrative or linguistic simulation of knowledge.  
Awareness may appear observational but is not grounded in actual visibility.

Examples include:

- describing internal system behavior  
- inferring user intent as fact  
- implying access to logs, telemetry, or history  
- stating causes not visible to the system  

Awareness is constrained and must be labeled or rewritten based on claim class.

---

## 3. claim

A discrete unit of information produced by a system,  
including statements, explanations, assertions, or reasoning steps.

Every claim must be classified under one of the canonical claim classes.

---

## 4. claim graph

An internal representation of all claims in a system output,  
including relationships, dependencies, and their associated metadata.

Used by validators and actors to enforce epistemic compliance.

---

## 5. hypothetical

Any inference or projection not grounded in observable input  
or externally verifiable knowledge.

Hypotheses must be explicitly labeled and include  
multiple alternative scenarios.

---

## 6. provenance

Source information and recency metadata attached to externally  
verifiable claims.

Includes:

- citation or origin  
- timestamp or recency  
- indication of contestation  

---

## 7. metadata

Internal fields attached to each claim, including:

- claim class  
- access state  
- certainty/uncertainty level  
- provenance (if applicable)  

Metadata informs how the Actor renders the final output.

---

## 8. forbidden claim

Any claim that implies access to unobservable state or contradicts  
OEP's core epistemic boundaries.

Forbidden claims must be rewritten, not rendered.

---

## 9. observability boundary

The conceptual barrier defining what the system is allowed to  
treat as known vs unknown.

OEP enforces a strict separation between observable input  
and all other information channels.

---

## 10. narrative patching

The process by which a model fills reasoning gaps with fabricated details.  
This behavior is prohibited under OEP and must be intercepted by validators.

---

# End of Terminology
