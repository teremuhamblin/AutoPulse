"""
AutoPulse Control
Moteur d’automatisme minimal.
"""

__version__ = "1.0.0"

from .state_machine import Machine
from .sequence_engine import SequenceEngine
from .io import IO

__all__ = ["Machine", "SequenceEngine", "IO"]
