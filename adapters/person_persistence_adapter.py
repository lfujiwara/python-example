from abc import ABC, abstractmethod
from typing import Awaitable, Iterable

from models.person import Person


class PersonPersistenceAdapter(ABC):

    @abstractmethod
    def get(self) -> Awaitable[Iterable[Person]]:
        raise NotImplementedError()
