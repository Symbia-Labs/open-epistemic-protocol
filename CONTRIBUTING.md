# Contributing to the Open Epistemic Protocol (OEP)

OEP is an open, model-agnostic standard for epistemically safe human–machine
interaction. Contributions are welcome, but the protocol evolves through a
structured, transparent process.

This document describes how to propose changes, submit RFCs, and participate in
the development of OEP.

---

## 1. Principles

All contributions must align with the core goals of OEP:

1. Establish clear epistemic boundaries for AI systems.
2. Prevent fabricated awareness and ungrounded inference.
3. Ensure transparency, falsifiability, and observability in machine output.
4. Maintain vendor neutrality and long-term governance independence.
5. Provide a stable, versioned specification for global adoption.

---

## 2. How OEP Evolves

OEP does not accept direct edits to the primary specification (`/spec/oep-v1.0.md`)
without an approved RFC.

The change process is:

1. Open an issue describing the problem or proposed enhancement.
2. Draft a Request for Comments (RFC) document under `/rfc/` using the template in
   `/rfc/TEMPLATE.md`.
3. Submit a pull request containing the RFC.
4. The maintainers and community review the RFC.
5. If approved, the RFC is merged and the spec is updated accordingly.
6. The change is versioned under semantic versioning (e.g., v1.0.1, v1.1.0).

---

## 3. Filing Issues

Use GitHub Issues for:

- Clarifications
- Spec ambiguities
- Suggestions for new claim classes
- Enforcement rule adjustments
- Validator improvements
- Test suite additions

Issues should be concise and technically grounded.

---

## 4. Pull Requests

PRs should:

- Reference an issue or approved RFC.
- Include tests where appropriate.
- Avoid modifying the core spec unless the RFC process is complete.
- Maintain consistency with terminology and definitions in `/spec`.

---

## 5. RFC Process

RFCs are the only mechanism for changing OEP's core principles, claim classes,
enforcement rules, or metadata schema.

An RFC must include:

- Motivation  
- Problem definition  
- Proposed change  
- Impact analysis  
- Backwards compatibility notes  
- Test implications  
- Alternatives considered  

The maintainers will merge an RFC only after community discussion and agreement
on its necessity and correctness.

---

## 6. Governance

Until a formal foundation exists, OEP is stewarded by Symbia Labs. Governance
may transition to a multi-organization body in a future RFC.

---

## 7. Code of Conduct

Be concise, technical, respectful, and epistemically rigorous. Discussions
should focus on correctness, clarity, and safety, not persuasion or rhetoric.

---

## 8. License

All contributions are licensed under the Apache License 2.0.
