from mmic.components.blueprints import StrategyComponent
from mmic_docking.models import DockInput, DockOutput
from typing import Set, Dict, List, Tuple, Any, Optional


__all__ = ["DockComponent"]


class DockComponent(StrategyComponent):
    @classmethod
    def input(cls) -> Dict[str, Any]:
        return DockInput

    @classmethod
    def output(cls) -> Dict[str, Any]:
        return DockOutput

    @property
    def tactic_comps(self) -> Set[str]:
        """Returns the supported components e.g. set(['mmic_mda',...]).
        Returns
        -------
        Set[str]
        """
        return set()

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
            raise NotImplementedError
        else:
            import mmic_autodock_vina

            RunComponent = mmic_autodock_vina.RunComponent
            inputs = inputs.dict()
            inputs["component"] = "mmic_autodock_vina"

        dockOutput = RunComponent.compute(inputs)
        return True, dockOutput
