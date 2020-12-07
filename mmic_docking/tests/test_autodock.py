# Import models
from mmic_docking.models.input import DockingRawInput
from mmelemental.models.util.input import FileInput
from mmelemental.models.chem.codes import ChemCode

# Construct docking input
dockRawInput = DockingRawInput(
    ligand="CCC", receptor="mmic_docking/data/dialanine/dialanine.pdb"
)

# Import components
from mmic_docking.components.autodock.autodock_convert_component import (
    ConvertAutoDockComponent,
)
from mmic_docking.components.autodock.autodock_component import AutoDockComponent

# Test for AutoDock Vina
dockInput = ConvertAutoDockComponent.compute(dockRawInput)
dockOutput = AutoDockComponent.compute(dockInput)

print("Scores: ")
print("========")
print(dockOutput.scores)

print("Poses: ")
print("========")
print(dockOutput.poses)
