from typing import List, Optional, Tuple, Union
from qcelemental import models
from mmelemental.models.molecule.mm_molecule import MMolecule
from mmelemental.models.chem.codes import ChemCode
from mmelemental.models.util.input import FileInput
from pydantic import Field

class DockingInput(models.ProtoModel):
    ligand: MMolecule = Field(
        ..., 
        description = "Molecule model for candidate ligand (e.g. drug)."
    )
    receptor: MMolecule = Field(
        ..., 
        description = "Molecule model for receptor (e.g. protein)."
    )
    searchSpace: Optional[List[Tuple[float, float, float, float, float, float]]] = Field(
        None, 
        description = "A 3D box defined by (xmin, xmax, ymin, ymax, zmin, zmax)."
        "The search space effectively restricts where the movable atoms, including those in the flexible side chains, should lie."
    )

class DockingRawInput(models.ProtoModel):
    ligand: str = Field(
        ..., 
        description = "Path to ligand (e.g. drug) input file, or chemical code (e.g. smiles)."
    )
    receptor: str = Field(
        ..., 
        description = "Path to receptor (e.g. protein) input file, or chemical code (e.g. smiles, sequence, ...)."
    )

class DockingComputeInput(models.ProtoModel):
    dockingInput: DockingInput = Field(
        ..., 
        description = "Docking input model."
    )
    ligand: str = Field(
        ..., 
        description = "Ligand file string."
    )
    receptor: str = Field(
        ..., 
        description = "Receptor file string."
    )
    cpu: Optional[int] = Field(
        1, 
        description = "The number of CPUs to use. The default is to try to "
        "detect the number of CPUs."
    )
    out: Optional[str] = Field(
        None, 
        description = "Output models."
    )
    log: Optional[str] = Field(
        None, 
        description = "Log file output."
    )
