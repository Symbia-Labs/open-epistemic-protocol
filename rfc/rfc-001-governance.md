# RFC-0001: Governance Model for the Open Epistemic Protocol (OEP)

**Author:** Symbia Labs  
**Created:** 2025-01-XX  
**Status:** Accepted  
**Version:** 1.0  
**OEP Version Target:** v1.x

---

## 1. Summary
This RFC defines the governance model for maintaining and evolving the Open Epistemic Protocol (OEP). It establishes how changes are proposed, reviewed, approved, and versioned.

---

## 2. Principles
Governance must ensure that OEP remains:

1. **Vendor-neutral**  
2. **Technically rigorous**  
3. **Epistemically safe**  
4. **Transparent and traceable**  
5. **Extensible without fragmentation**

---

## 3. Decision-Making Structure

### 3.1 Maintainers
The maintainers are responsible for:
- reviewing RFCs  
- merging approved changes  
- managing releases  
- enforcing process discipline  

Initial maintainers: **Symbia Labs**

Future maintainers may be added by RFC.

---

### 3.2 Community Participation
Anyone may:
- submit RFCs  
- comment on RFC discussions  
- open issues  
- contribute tests or validator improvements  

---

## 4. RFC Approval Process

A proposal becomes part of OEP only if:

1. It is submitted as an RFC using `/rfc/TEMPLATE.md`  
2. It receives at least:
   - one maintainer approval  
   - one reviewer acknowledgement  
3. It is discussed publicly for a minimum of 7 days  
4. The maintainers merge it and bump the OEP version  

---

## 5. Semantic Versioning

OEP uses semantic versioning:

- **MAJOR**: breaking changes to claim classes or enforcement rules  
- **MINOR**: new optional features, metadata fields, claim extensions  
- **PATCH**: clarifications, typos, test fixes  

Example:  
`1.0.0 → 1.1.0` for new claim class  
`1.1.0 → 1.1.1` for corrections  

---

## 6. Release Process

1. Merge approved RFC  
2. Update `/spec/oep-vX.Y.md`  
3. Update validator + tests  
4. Tag release  
5. Publish release notes

---

## 7. Conflict Resolution

If maintainers disagree, the default resolution method is:

- prefer safety over convenience  
- prefer clarity over flexibility  
- prefer explicit rules over implicit heuristics  

Unresolved conflicts require a separate governance RFC.

---

## 8. Transition to a Foundation
The intent is to eventually migrate OEP stewardship to a multi-organization foundation.  
This transition will be formalized in a future RFC.

---

## 9. License
All contributions remain under Apache 2.0.
