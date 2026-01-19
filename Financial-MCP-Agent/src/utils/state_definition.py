import operator
from typing import TypedDict, Sequence, Dict, Any, Annotated

from langchain_core.messages import BaseMessage


def merge_dicts(d1: Dict[str, Any], d2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries, d2 values overwrite d1."""
    return {**d1, **d2}


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]  # 对话消息列表：按“拼接”规则合并
    data: Annotated[Dict[str, Any], merge_dicts]  # 业务核心数据：按“字典合并”规则更新
    metadata: Annotated[Dict[str, Any], merge_dicts]   # 运行时元数据：按“字典合并”规则更新
    # Potentially add a field for the initial user query if it needs to be passed around
    # user_query: str
