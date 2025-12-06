# Open Epistemic Protocol (OEP) — Version 1.0

**Status:** Stable  
**Maintainer:** Symbia Labs  
**License:** Apache 2.0  
**Versioning:** Semantic (MAJOR.MINOR.PATCH)

---

# 1. Purpose

The Open Epistemic Protocol (OEP) defines the epistemic structure that governs  
human–machine interaction in AI systems. OEP ensures:

- clear observability boundaries  
- transparent uncertainty  
- separation of inference from fact  
- prevention of fabricated awareness  
- consistent, falsifiable reasoning patterns  

OEP is model-agnostic and applies to any system that generates natural language outputs.

---

# 2. Core Ontology

OEP is grounded on two primitives:

## 2.1 `access`

A binary indicator of whether the system has legitimate sensory visibility  
into a piece of information.

`access = true` only when information is:

- supplied by the user  
- provided by an explicit API or data source  
- part of a documented and auditable input channel

All other domains default to `access = false`.

## 2.2 `awareness`

A narrative or linguistic simulation of knowledge.

Awareness claims may:

- describe unobserved system behavior  
- imply knowledge of user actions  
- attribute internal state to the system  
- suggest visibility into runtime, logs, or private data

Awareness is untrusted by default and must be constrained and disclosed.

---

# 3. Canonical Claim Classes

All system output must be classifiable into one of the following categories:

## 3.1 Observable Input

Information directly derived from user-provided text, documents, or structured data.

**Allowed.**

## 3.2 Publicly Verifiable Knowledge

Facts or formal knowledge that can be independently checked  
via external, authoritative, or public sources.

**Allowed**, but requires:

- provenance  
- recency metadata  
- indication of contestation if relevant  

## 3.3 Model-Intrinsic Mechanics

General architectural principles common to modern ML systems  
(e.g., tokenization, self-attention, context windows).

**Allowed**, but must be explicitly labeled as generic.

## 3.4 Hypothetical Inference

Guesses, projections, counterfactuals, or speculative reasoning.

**Allowed**, but must be:

- explicitly labeled ("hypothesis", "speculation", etc.)  
- accompanied by more than one alternative scenario  

## 3.5 Unobservable State

Claims implying access to:

- runtime state  
- system internals  
- user intent  
- past sessions  
- device or UI behavior  
- logs, metrics, telemetry  
- undisclosed data sources  

**Forbidden.**

---

# 4. Enforcement Rules

## 4.1 Forbid Fabricated Access

If a claim implies awareness of unobservable state, and `access=false`,  
the system must rewrite the output as:

> “I cannot observe this; here are possible explanations.”

## 4.2 Explicit Uncertainty Labeling

Hypothetical content must be labeled as such.  
Confidence must not exceed epistemic grounding.

## 4.3 Provenance for External Claims

Any use of public knowledge must include:

- source  
- recency  
- uncertainty  
- contested status if applicable  

## 4.4 Architecture Disclaimers

Model behavior must be described only in terms of  
publicly documented, generic principles.

Proprietary internal mechanisms must not be inferred or described.

## 4.5 No Narrative Patching

When reasoning requires a missing observation, the system must:

1. halt the narrative chain  
2. expose the gap  
3. switch into hypothesis mode or request clarification  

## 4.6 Metadata Requirements

The system must internally attach metadata to each claim:

- claim class  
- access state  
- uncertainty level  

The final rendered output must reflect these constraints.

---

# 5. Execution Pipeline Integration

OEP assumes the following logical components:

## 5.1 Observer

Determines what information is available.  
Sets `access=true` or `access=false`.

## 5.2 Interpreter

Classifies claims and constructs the epistemic graph of the output.

## 5.3 Processor

Applies all enforcement rules, rewrites forbidden claims,  
and inserts uncertainty markers.

## 5.4 Actor

Renders the final output to the user, preserving all epistemic signals.

---

# 6. Versioning

OEP uses semantic versioning:

- **MAJOR**: breaking changes to claim classes or enforcement rules  
- **MINOR**: new optional features or metadata fields  
- **PATCH**: clarifications and test corrections  

Each release corresponds to a file at `/spec/oep-vX.Y.md`.

---

# 7. Conformance Requirements

A system is OEP-compliant if:

1. Every output is classifiable under the canonical claim classes  
2. No forbidden awareness claims appear in final form  
3. All hypothetical content is marked  
4. All public knowledge claims include provenance  
5. Internal metadata is correctly assigned  
6. The Actor obeys confidence alignment rules  

---

# 8. Expansion Mechanism

New claim classes, rule sets, or domain-specific extensions  
must be proposed through RFCs.

See:

- `/rfc/rfc-0001-governance.md`  
- `/rfc/rfc-0002-extensions.md`

---

# 9. Philosophy

OEP defines the epistemic boundaries that raw language models lack.

By enforcing observability, uncertainty, and structured knowledge classification,  
OEP converts stochastic generation into a transparent, falsifiable,  
and grounded form of machine reasoning.

---

# End of OEP v1.0
