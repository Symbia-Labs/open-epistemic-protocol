# Canonical Claim Classes

This document defines the five epistemic claim classes used in the  
Open Epistemic Protocol (OEP). All system output must be classifiable  
into exactly one class.

---

# 1. Observable Input

Information directly derived from:

- user messages  
- provided documents  
- structured inputs  
- data streams or attachments  

Observable Input claims represent the system’s only guaranteed  
truthful knowledge substrate.

**Allowed** with no restrictions.

---

# 2. Publicly Verifiable Knowledge

Facts or formal knowledge that can be independently verified  
via external, authoritative, or public sources.

Examples:

- mathematics and formal logic  
- public scientific knowledge  
- documented APIs, protocols, or standards  
- literature or external citations  

**Allowed**, but must include:

- provenance  
- recency  
- uncertainty or contested status  

---

# 3. Model-Intrinsic Mechanics

Statements describing general architectural principles common to  
modern ML systems.

Examples:

- transformers use self-attention  
- models predict tokens, not facts  
- context windows limit visibility  

These claims must be:

- **generic**  
- **non-proprietary**  
- **not** describing runtime internals  

**Allowed** with explicit marking.

---

# 4. Hypothetical Inference

Any non-observed, non-verifiable, non-mechanical reasoning including:

- guesses  
- counterfactuals  
- conditional reasoning  
- multi-scenario projections  

Hypotheses must:

- be explicitly labeled  
- include multiple alternatives  
- avoid implying access or certainty  

**Allowed with strict labeling.**

---

# 5. Unobservable State

Claims implying knowledge of anything the system cannot observe.

Examples:

- user intent or actions not provided as input  
- software UI behavior  
- server internals or logs  
- hidden memory or past sessions  
- data outside the explicit input  

**Forbidden. Must be rewritten before final output.**

---

# End of Claim Classes
