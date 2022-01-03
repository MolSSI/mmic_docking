from cmselemental.models import OutputProc
from .common import DockMol
from .input import InputDock
from pydantic import Field, root_validator
from typing import List, Optional

__all__ = ["OutputDock"]


class OutputDock(OutputProc):
    proc_input: InputDock = Field(..., description="Docking input model.")
    poses: DockMol = Field(
        ...,
        description="A collection of ligand and optionally receptor poses. See the :class:``Ensemble`` class. ",
    )
    scores: List[float] = Field(
        ...,
        description="A list of scores for each pose. Typically the score is the binding affinity. Length must be equal to the number of poses.",
    )
    scores_units: Optional[str] = Field(None, description="Score function unit.")

    @root_validator
    def _valid_score_len(cls, values):
        assert len(values["scores"]) == len(values["poses"].ligand)
        return values
