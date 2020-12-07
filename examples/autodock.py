# Import converter component for autodock vina
from mmic_docking.components.autodock.autodock_convert_component import (
    ConvertAutoDockComponent,
)

from mmelemental.models.molecule.mm_molecule import Molecule
from mmic_docking.models.input import DockingInput

# Construct docking input
receptor = Molecule.from_file("mmic_docking/data/PHIPA_C2/PHIPA_C2_apo.pdb")
ligand = Molecule.from_data(
    "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O"
)  # smiles code for ibuprofen
dockInput = DockingInput(ligand=ligand, receptor=receptor)

# Import simulation component for autodock vina
from mmic_docking.components.autodock.autodock_component import AutoDockComponent

# Run autodock vina
dockOutput = AutoDockComponent.compute(dockInput)

# Extract output
scores, poses = dockOutput.scores, dockOutput.poses

print("Scores: ")
print("========")
print(scores)

print("Poses: ")
print("========")
print(poses)
