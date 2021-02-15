from mmelemental.models.molecule.mm_mol import Mol
from mmelemental.models.app.docking import DockInput

# Construct docking input
receptor = Mol.from_file("mmic_docking/data/PHIPA_C2/PHIPA_C2_apo.pdb")
ligand = Mol.from_data(
    "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O"
)  # smiles code for ibuprofen
dockInput = DockInput(ligand=ligand, receptor=receptor)

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
