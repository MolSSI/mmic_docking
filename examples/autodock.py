import sys
import os

# Import converter component for autodock vina 
from mmcomponents_docking.components.autodock.autodock_convert_component import ConvertAutoDockComponent

from mmelemental.models.molecule.mm_molecule import MMolecule
from mmcomponents_docking.models.input import DockingInput
# Construct docking input
receptor = MMolecule.from_file('mmcomponents_docking/data/PHIPA_C2/PHIPA_C2_apo.pdb')
ligand = MMolecule.from_data('CC(C)CC1=CC=C(C=C1)C(C)C(=O)O') # smiles code for ibuprofen
dockInput = DockingInput(ligand=ligand, receptor=receptor)

# Import simulation component for autodock vina 
from mmcomponents_docking.components.autodock.autodock_component import AutoDockComponent

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
