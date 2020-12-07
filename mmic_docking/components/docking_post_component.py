from mmic.components.base.base_component import ProgramHarness
from mmic_docking.models.output import DockingOutput, DockingComputeOutput
from typing import Any, List


class DockPostComponent(ProgramHarness):
    """ Postprocessing component for docking. """

    @classmethod
    def input(cls):
        return DockingComputeOutput

    @classmethod
    def output(cls):
        return DockingOutput

    # helper functions
    def get_scores(self, output: Any) -> List[float]:
        raise NotImplementedError(
            "get_scores is not implemented for {}.", self.__class__
        )
