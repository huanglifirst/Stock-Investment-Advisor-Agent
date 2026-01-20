import time
from typing import Any, Dict

from langchain_core.callbacks import BaseCallbackHandler

from src.utils.execution_logger import get_execution_logger


class ToolUsageCallbackHandler(BaseCallbackHandler):
    """将工具调用记录接入执行日志系统。"""

    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self._start_times: Dict[str, float] = {}
        self._inputs: Dict[str, Any] = {}

    def _normalize_input(self, tool_input: Any) -> Dict[str, Any]:
        if isinstance(tool_input, dict):
            return tool_input
        return {"input": tool_input}

    def on_tool_start(self, serialized: Dict[str, Any], input_str: Any, run_id: str, **kwargs: Any) -> None:
        self._start_times[run_id] = time.time()
        self._inputs[run_id] = input_str

    def on_tool_end(self, output: Any, run_id: str, **kwargs: Any) -> None:
        execution_logger = get_execution_logger()
        start_time = self._start_times.pop(run_id, time.time())
        tool_input = self._inputs.pop(run_id, {})
        tool_name = kwargs.get("name") or (kwargs.get("serialized", {}) or {}).get("name")
        execution_logger.log_tool_usage(
            agent_name=self.agent_name,
            tool_name=tool_name or "unknown_tool",
            tool_input=self._normalize_input(tool_input),
            tool_output=output,
            execution_time=time.time() - start_time,
            success=True
        )

    def on_tool_error(self, error: Exception, run_id: str, **kwargs: Any) -> None:
        execution_logger = get_execution_logger()
        start_time = self._start_times.pop(run_id, time.time())
        tool_input = self._inputs.pop(run_id, {})
        tool_name = kwargs.get("name") or (kwargs.get("serialized", {}) or {}).get("name")
        execution_logger.log_tool_usage(
            agent_name=self.agent_name,
            tool_name=tool_name or "unknown_tool",
            tool_input=self._normalize_input(tool_input),
            tool_output=str(error),
            execution_time=time.time() - start_time,
            success=False,
            error=str(error)
        )
