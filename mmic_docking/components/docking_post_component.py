from mmic.components.blueprints.generic_component import GenericComponent
from mmic_docking.models.output import DockingComputeOutput
from mmelemental.models.output.docking import DockingOutput
from typing import Any, List


class DockPostComponent(GenericComponent):
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
