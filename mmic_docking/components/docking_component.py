from mmelemental.models.app.docking import DockInput
from mmelemental.models.app.docking import DockOutput
from mmic.components.blueprints.generic_component import GenericComponent
from typing import Dict, List, Tuple, Optional, Any


__all__ = ["DockComponent"]


class DockComponent(GenericComponent):
    @classmethod
    def input(cls):
        return DockInput

    @classmethod
    def output(cls):
        return DockOutput

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        pass
