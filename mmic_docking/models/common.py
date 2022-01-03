from mmelemental.models.base import ProtoModel
from mmelemental.models import Molecule
from pydantic import Field
from typing import List, Union, Optional


class DockMol(ProtoModel):
    ligand: Union[List[Molecule], Molecule] = Field(
        ...,
        description="Ligand molecule object(s) such as a drug. See the :class:``Molecule`` class. ",
    )
    receptor: Union[List[Molecule], Molecule] = Field(
        ...,
        description="Receptor molecule object(s) such as a protein. See the :class:``Molecule`` class. ",
    )
    solvent: Optional[Union[List[Molecule], Molecule]] = Field(
        None,
        description="Solvent molecule object(s) such as water. See the :class:``Molecule`` class.",
    )
    ions: Optional[Union[List[Molecule], Molecule]] = Field(
        None,
        description="Ionic atom/molecule object(s) such as sodium chloride. See the :class:``Molecule`` class.",
    )
