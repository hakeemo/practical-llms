from abc import ABC, abstractmethod
from typing import List

from langchain.schema import BaseMessage
from langchain.vectorstores.base import VectorStoreRetriever


class BaseActionPlanner(ABC):
    @abstractmethod
    def select_action(
        self,
        previous_messages: List[BaseMessage],
        memory: VectorStoreRetriever,
        **kwargs
    ) -> str:
        pass
