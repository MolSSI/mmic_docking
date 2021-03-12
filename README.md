[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MolSSI/mmic_docking/workflows/CI/badge.svg)](https://github.com/MolSSI/mmic_docking/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/MolSSI/mmic_docking/branch/master/graph/badge.svg)](https://codecov.io/gh/MolSSI/mmic_docking/branch/master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MolSSI/mmic_docking.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MolSSI/mmic_mda/context:python)

# What is Docking?
Docking is a computational technique used to determine the optimal binding modes of a ligand-receptor system. A ligand is typically a small (e.g. drug) molecule that binds to a macromolecular receptor such as a protein. A docking simulation estimates the strength of the binding (or a quantitative "score") in the vicinity of the receptor's binding site. Each score corresponds to the 3D conformation and orientation of the ligand relative to the receptor (or the "pose").

<p align="center">
<img src="mmic_docking/data/imgs/docking-sys-removebg.png" width="500">
</p>
    
Applications of docking include:

- Virtual screening (hit identification)
- Drug discovery (lead optimization)
- Binding site identification (blind docking)
- Protein-protein interactions
- Enzymatic reaction mechanisms
- Protein engineering

# Docking Component
## Preparing Input

```python
# Import MM molecule data model
from mmelemental.models.molecule import Molecule

# Construct MM molecules
receptor_data   = Molecule.from_file(pdb_file)
ligand_data     = Molecule.from_data(smiles_code)

# Import docking data model compliant with MMSchema
from mmic_docking.models import DockInput

# Construct docking input data from MMSchema molecules
dock_input = DockInput(
    ligand=ligand_data, 
    receptor=receptor_data, 
    engine="autodock_vina",
)

```

## Running Docking with AutoDock Vina component

```python
# Import docking simulation component for autodock vina
from mmic_docking.components import DockComponent

# Run autodock vina
dock_output = DockComponent.compute(dock_input)

# Extract output
scores, ligands = dock_output.observables.score, dock_output.poses.ligand
```

### Copyright

Copyright (c) 2021, MolSSI


#### Acknowledgements

Project based on the
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.1.
