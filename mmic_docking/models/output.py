from typing import List, Optional
from mmelemental.models.input.docking import DockingInput
from mmelemental.models.util.output import ComputeOutput
from pydantic import Field


class DockingComputeOutput(ComputeOutput):
    dockingInput: DockingInput = Field(..., description="Docking input model.")
    scores: List[float] = Field(
        None,
        description="A metric for evaluating a particular pose. Length of scores must be equal to length of poses.",
    )
    poses: Optional[List[str]] = Field(
        None,
        description="List of file strings defining the conformation and orientation of the candidate ligand relative to the receptor.",
    )
    flexible: Optional[List[str]] = Field(
        None,
        description="List of file strings defining the conformation and orientation of the flexible side chains in the receptor "
        "relative to the ligand.",
    )
    system: Optional[str] = Field(
        None,
        description="Input file string storing the ligand poses with (optionally) the flexible receptor side-chains.",
    )
