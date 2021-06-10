from mmic.components.blueprints import StrategyComponent
from mmic_docking.models import DockInput, DockOutput
from typing import Set, Dict, List, Tuple, Any, Optional
import importlib

__all__ = ["DockComponent"]


class DockComponent(StrategyComponent):
    @classmethod
    def input(cls) -> Dict[str, Any]:
        return DockInput

    @classmethod
    def output(cls) -> Dict[str, Any]:
        return DockOutput

    @classmethod
    def tactic_comps(cls) -> Set[str]:
        """Returns the supported components e.g. set(['mmic_autodock_vina',...]).
        Returns
        -------
        Set[str]
        """
        return set(["mmic_autodock_vina"])

    def get_version(self):
        return ""

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
        config: Optional["TaskConfig"] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        if isinstance(inputs, dict):
            inputs = self.input()(**inputs)

        if inputs.component:
            tactic_comp = importlib.import_module(inputs.component)
        else:
            tactic_comp = importlib.import_module("mmic_autodock_vina")

        dockOutput = tactic_comp.components.RunComponent.compute(inputs)

        return True, dockOutput
