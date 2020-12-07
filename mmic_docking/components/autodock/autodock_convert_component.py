from mmelemental.components.constructor_component import MolConstructorComponent
from typing import Any, Dict, List, Optional, Tuple
import os

from mmic_docking.models.input import DockingInput, DockingRawInput
from mmelemental.models.molecule.mm_molecule import Molecule
from mmelemental.models.util.input import FileInput
from mmelemental.models.chem.codes import ChemCode


class ConvertAutoDockComponent(MolConstructorComponent):
    @classmethod
    def input(cls):
        return DockingRawInput

    @classmethod
    def output(cls):
        return DockingInput

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        if os.path.isfile(inputs.ligand):
            ligand = FileInput(path=inputs.ligand)
        else:  # had better be a valid chem code
            ligand = ChemCode(code=inputs.ligand)
        ligand = self.constructor(ligand)

        if os.path.isfile(inputs.receptor):
            receptor = FileInput(path=inputs.receptor)
        else:  # had better be a valid chem code
            receptor = ChemCode(code=inputs.receptor)
        receptor = self.constructor(receptor)

        return True, DockingInput(ligand=ligand, receptor=receptor)
