# detector.py
"""
OEP Awareness Violation Detector (Stub)
---------------------------------------

Detects claims that imply fabricated awareness or access to unobservable state.
"""

class AwarenessDetector:
    def detect(self, text: str) -> bool:
        """
        Returns True if the text appears to imply unobservable access or awareness.

        Parameters
        ----------
        text : str
            The claim to analyze.

        Returns
        -------
        bool
            True if awareness violation detected; False otherwise.

        Notes
        -----
        Awareness examples include:
        - references to UI behavior
        - speculation about user intent
        - claims about internal system state
        """
        return False
