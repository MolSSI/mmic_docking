from mmelemental.models.app.docking import DockOutput, AffinityOutput
from mmic.components.blueprints.generic_component import GenericComponent

__all__ = ["AffinityComponent"]


class AffinityComponent(GenericComponent):
    @classmethod
    def input(cls):
        return DockOutput

    @classmethod
    def output(cls):
        return AffinityOutput
