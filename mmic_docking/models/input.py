from mmelemental.models.proc import ProcInput
from .common import DockMol
from pydantic import Field
from typing import Optional, Tuple, Union


__all__ = ["DockInput"]

class DockInput(ProcInput):
    molecule: DockMol = Field(
        ...,
        description="Molecular mechanics molecule object(s). See the :class:``DockMol`` class. "
        "Example: mol = {'ligand': Molecule, 'receptor': Molecule, 'solvent': Molecule}.",
    )
    searchSpace: Optional[
        Union[
            Tuple[float, float],
            Tuple[float, float, float, float],
            Tuple[float, float, float, float, float, float],
        ]
    ] = Field(
        None,
        description="A search box defined by (xmin, xmax) in 1D, (xmin, xmax, ymin, ymax) in 2D and "
        "(xmin, xmax, ymin, ymax, zmin, zmax) in 3D. The search space effectively restricts where the "
        "movable atoms, including those in the flexible side chains, should lie. Default unit in Angstroms.",
    )
    searchSpace_units: Optional[str] = Field(
        "angstrom", description="Spatial units for search space box."
    )
