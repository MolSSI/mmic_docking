from mmic_docking.models.input import DockingInput
from mmic_docking.models.output import DockingOutput
from mmic.components.base.base_component import ProgramHarness

class DockingComponent(ProgramHarness):

    @classmethod
    def input(cls):
        return DockingInput

    @classmethod
    def output(cls):
        return DockingOutput
