from mmic.components.blueprints import GenericComponent
from mmic_docking.models import DockInput, DockOutput
from typing import Set, Dict, Any


__all__ = ["DockComponent"]


class DockComponent(GenericComponent):
    @classmethod
    def input(cls) -> Dict[str, Any]:
        return DockInput

    @classmethod
    def output(cls) -> Dict[str, Any]:
        return DockOutput

    @property
    def supported_comps(self) -> Set[str]:
        """Returns the supported components e.g. set(['mmic_mda',...]).
        Returns
        -------
        Set[str]
        """
        return set()
