from abc import ABC, abstractmethod
from typing import Awaitable


class PersonStatsService(ABC):

  @abstractmethod
  def get_info_about_countries(self) -> Awaitable[dict]:
    raise NotImplementedError()
