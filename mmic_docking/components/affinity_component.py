from mmic.models.docking.output import DockingOutput
from mmic.models.affinity.output import AffinityOutput
from mmic.base.base_component import ProgramHarness

class DockingAffinityComponent(ProgramHarness):

    @classmethod
    def input(cls):
        return DockingOutput

    @classmethod
    def output(cls):
        return AffinityOutput
