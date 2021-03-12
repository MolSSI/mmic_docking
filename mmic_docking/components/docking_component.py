from ..models.input import DockInput
from ..models.output import DockOutput
from mmelemental.components.util.cmd_component import CmdComponent
import abc
from typing import Dict, List, Tuple, Optional, Any


__all__ = ["DockComponent"]


class DockComponent(CmdComponent, abc.ABC):
    @classmethod
    def input(cls):
        return DockInput

    @classmethod
    def output(cls):
        return DockOutput

    @abc.abstractmethod
    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        raise NotImplementedError
