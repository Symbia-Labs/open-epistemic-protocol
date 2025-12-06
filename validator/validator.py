# validator.py
"""
OEP Validator (Stub)
--------------------

Applies enforcement rules:

- forbid fabricated access
- label hypothetical inference
- require provenance for public knowledge
- prevent narrative patching
- attach metadata to claims

This file defines the Validator shell.
"""

from .classifier import ClaimClassifier, ClaimClass
from .detector import AwarenessDetector


class OEPValidator:
    def __init__(self):
        self.classifier = ClaimClassifier()
        self.detector = AwarenessDetector()

    def validate(self, text: str) -> dict:
        """
        Validate a claim and return structured metadata.

        Parameters
        ----------
        text : str

        Returns
        -------
        dict
            {
                "original": text,
                "claim_class": <ClaimClass or None>,
                "awareness_violation": <bool>,
                "metadata": {}
            }
        """
        cls = self.classifier.classify(text)
        violation = self.detector.detect(text)

        return {
            "original": text,
            "claim_class": cls,
            "awareness_violation": violation,
            "metadata": {}
        }
