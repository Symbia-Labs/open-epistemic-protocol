# classifier.py
"""
OEP Claim Classifier (Stub)
---------------------------

Responsible for classifying textual claims into one of the canonical
OEP claim classes:

1. observable_input
2. public_knowledge
3. model_intrinsic
4. hypothetical
5. unobservable_state

This is a structural placeholder. Full implementation to follow.
"""

from enum import Enum


class ClaimClass(Enum):
    OBSERVABLE_INPUT = "observable_input"
    PUBLIC_KNOWLEDGE = "public_knowledge"
    MODEL_INTRINSIC = "model_intrinsic"
    HYPOTHETICAL = "hypothetical"
    UNOBSERVABLE_STATE = "unobservable_state"


class ClaimClassifier:
    def classify(self, text: str) -> ClaimClass:
        """
        Stub classifier. Returns None; logic to be implemented.

        Parameters
        ----------
        text : str
            The claim to classify.

        Returns
        -------
        ClaimClass
            The predicted claim class.

        Notes
        -----
        Real classification requires:
        - lexical pattern detection
        - provenance recognition
        - hypothesis markers
        - forbidden awareness cues
        """
        return None
