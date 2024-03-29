"""
Unit and regression test for the mmic_docking package.
"""

# Import package, test suite, and other packages as needed
import mmic_docking
from mmelemental.models import Molecule
from cmselemental.util.decorators import classproperty
from mmic_docking.models import InputDock, OutputDock
from mmic_docking.components import DockComponent
from mmic.components.blueprints import TacticComponent
import importlib
import pytest
import sys


tactic_comps = DockComponent.tactic_comps
avail_comps = [comp for comp in tactic_comps if importlib.util.find_spec(comp)]


def pytest_generate_tests(metafunc):
    if "comp" in metafunc.fixturenames:
        metafunc.parametrize("comp", avail_comps)


def test_mmic_docking_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_docking" in sys.modules


def test_mmic_docking_input():
    receptor = Molecule.from_file("mmic_docking/data/PHIPA_C2/PHIPA_C2_apo.pdb")
    ligand = Molecule.from_data(
        "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O", dtype="smiles"
    )  # smiles code for ibuprofen

    searchSpace = [-37.807, 5.045, -2.001, 30.131, -19.633, 37.987]

    return InputDock(
        schema_name="mmschema",
        schema_version=1,
        molecule={"ligand": ligand, "receptor": receptor},
        search_space=searchSpace,
        search_space_units="angstrom",
    )


def test_mmic_docking_output(dockin=None):
    dock_input = test_mmic_docking_input() if dockin == None else dockin
    ligand = dock_input.molecule.ligand
    receptor = dock_input.molecule.receptor

    return OutputDock(
        success=True,
        schema_name="mmschema",
        schema_version=1,
        proc_input=dock_input,
        scores=[1, 3, 6],
        scores_units="kJ/mol",
        poses={
            "ligand": [ligand, ligand, ligand],
            "receptor": [receptor, receptor, receptor],
        },
    )


def test_mmic_docking_component():
    class TestDockComponent(TacticComponent):
        @classproperty
        def output(cls):
            return OutputDock

        @classproperty
        def input(cls):
            return InputDock

        @classproperty
        def version(self):
            return ""

        @classproperty
        def strategy_comps(cls):
            return DockComponent

        def execute(
            self,
            inputs,
            extra_outfiles=None,
            extra_commands=None,
            scratch_name=None,
            timeout=None,
        ):

            return True, test_mmic_docking_output(inputs)

    inputs = test_mmic_docking_input()
    test = TestDockComponent.compute(inputs)


def test_mmic_docking_dummy_component(comp, dockin=None):
    dock_input = test_mmic_docking_input() if dockin == None else dockin
    dock_input = dock_input.dict()
    dock_input.setdefault("component", comp)
    dock_input = InputDock(**dock_input)
    dockout = mmic_docking.components.DockComponent.compute(dock_input)
