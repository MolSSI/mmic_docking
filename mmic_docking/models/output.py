from mmelemental.models.app.base import SimOutput
from mmelemental.models.base import ProtoModel
from mmelemental.models.molecule import Molecule
from .common import DockMol
from .input import DockInput
from pydantic import Field, root_validator
from typing import List, Optional


class DockObserv(ProtoModel):
    score: List[float] = Field(
        ...,
        description="Score for each pose. Typically the score is the binding affinity. Length must be equal to the number of poses.",
    )


class DockObservUnits(ProtoModel):
    score: Optional[str] = Field(None, description="Score function unit.")


class DockOutput(SimOutput):
    simInput: DockInput = Field(..., description="Docking input model.")
    poses: DockMol = Field(
        ...,
        description="A collection of ligand and optionally receptor poses. See the :class:``Ensemble`` class. ",
    )
    observables: Optional[DockObserv] = Field(
        None,
        description="Physical observables for each pose. E.g. observables={'RMSD':[...]}.",
    )
    observables_units: Optional[DockObservUnits] = Field(
        None,
        description="Physical observables units. E.g. observables_units={'RMSD':'angstrom'}.",
    )

    @root_validator
    def _valid_score_len(cls, values):
        assert len(values.get("observables").score) == len(values["poses"].ligand)
        return values
