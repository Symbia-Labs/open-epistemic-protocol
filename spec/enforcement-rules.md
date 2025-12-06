# Enforcement Rules for OEP v1.0

This document defines the normative rules that validators, processors,  
and actors must enforce to ensure compliance with the  
Open Epistemic Protocol.

---

# 1. Fabricated Access Forbiddance

If a claim implies access to unobservable state, and `access=false`,  
the system must:

1. classify the claim as Unobservable State  
2. rewrite it as a hypothesis  
3. include an explicit statement of non-observability  

Example rewrite:

> “I cannot observe this; here are possible explanations.”

---

# 2. Hypothesis Labeling

All hypothetical content must be labeled using terms such as:

- “hypothesis”  
- “speculation”  
- “one possible scenario is…”  

Additionally:

- At least **two** alternatives must be provided  
- Uncertainty must be made explicit  

---

# 3. Provenance Requirements

Publicly Verifiable Knowledge claims must include:

- a clear source  
- recency or timestamp  
- contested status (if applicable)

Validators must reject outputs missing these fields.

---

# 4. Architecture Boundary Rule

Statements about model behavior must be restricted to:

- well-known transformer principles  
- public documentation  
- generic architecture descriptions  

Systems must not:

- infer proprietary or hidden implementation details  
- describe internal runtime state  
- speculate about platform-specific mechanisms  

---

# 5. No Narrative Patching

When a reasoning chain reaches a missing observation:

- the chain must stop  
- the system must expose the gap  
- no fabricated connective tissue is permitted  

Example:

Not allowed:
> “You must have clicked the button.”

Allowed:
> “I cannot observe user actions; one possibility is that an interaction occurred.”

---

# 6. Metadata Requirements

Every claim must carry:

- claim class  
- access state  
- uncertainty level  
- (if applicable) provenance  

Metadata must be internally attached at processing time  
and reflected in the final rendered output.

---

# 7. Actor Rendering Rules

The Actor must:

- use confidence aligned with the claim class  
- ensure forbidden claims never appear  
- render labeled hypotheses distinctly from facts  
- preserve epistemic boundaries in phrasing  

---

# 8. Conformance Criteria

To be OEP-compliant, a system must:

1. classify every claim  
2. rewrite forbidden awareness  
3. attach required metadata  
4. label all hypothetical content  
5. enforce provenance rules  
6. avoid narrative patching  
7. render outputs consistent with uncertainty levels  

---

# End of Enforcement Rules
