"""
Unit and regression test for the mmic_docking package.
"""

# Import package, test suite, and other packages as needed
import mmic_docking
from mmelemental.models.molecule import Molecule
from mmic_docking.models import DockInput, DockOutput
from mmic_docking.components import DockComponent
from mmic.components.blueprints import TacticComponent
import pytest
import sys


def test_mmic_docking_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_docking" in sys.modules


def test_mmic_docking_input():
    receptor = Molecule.from_file("mmic_docking/data/PHIPA_C2/PHIPA_C2_apo.pdb")
    ligand = Molecule.from_data(
        "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O", dtype="smiles"
    )  # smiles code for ibuprofen

    searchSpace = [-37.807, 5.045, -2.001, 30.131, -19.633, 37.987]

    return DockInput(
        molecule={"ligand": ligand, "receptor": receptor},
        search_space=searchSpace,
        search_space_units="angstrom",
    )


def test_mmic_docking_output(dockin=None):
    dock_input = test_mmic_docking_input() if dockin == None else dockin
    ligand = dock_input.molecule.ligand
    receptor = dock_input.molecule.receptor

    return DockOutput(
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

        @classmethod
        def output(cls):
            return DockOutput

        @classmethod
        def input(cls):
            return DockInput

        def get_version(self):
            return ""

        @classmethod
        def strategy_comp(cls):
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


def test_mmic_docking_dummy_component(dockin=None):
    dock_input = test_mmic_docking_input() if dockin == None else dockin
    dockout = mmic_docking.components.DockComponent.compute(dock_input)
