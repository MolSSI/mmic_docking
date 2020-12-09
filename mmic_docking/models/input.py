from typing import List, Optional, Tuple, Union
from mmelemental import models
from mmelemental.models.input.docking import DockingInput
from pydantic import Field

class DockingRawInput(models.base.Base):
    ligand: str = Field(
        ...,
        description="Path to ligand (e.g. drug) input file, or chemical code (e.g. smiles).",
    )
    receptor: str = Field(
        ...,
        description="Path to receptor (e.g. protein) input file, or chemical code (e.g. smiles, sequence, ...).",
    )


class DockingComputeInput(models.base.Base):
    dockingInput: DockingInput = Field(..., description="Docking input model.")
    ligand: str = Field(..., description="Ligand file string.")
    receptor: str = Field(..., description="Receptor file string.")
    cpu: Optional[int] = Field(
        1,
        description="The number of CPUs to use. The default is to try to "
        "detect the number of CPUs.",
    )
    out: Optional[str] = Field(None, description="Output models.")
    log: Optional[str] = Field(None, description="Log file output.")
