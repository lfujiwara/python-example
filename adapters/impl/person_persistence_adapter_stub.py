from json import loads
from typing import Awaitable, Iterable
from models.person import Person
from adapters.person_persistence_adapter import PersonPersistenceAdapter


data = '[{"name": "Souza", "age": 35, "country": "Mexico"}, {"name": "Andrade", "age": 35, "country": "Chile"}, {"name": "Felipe", "age": 35, "country": "Colombia"}, {"name": "Sérgio", "age": 35, "country": "Colombia"}, {"name": "Lisboa", "age": 35, "country": "Colombia"}, {"name": "Souza Lima", "age": 35, "country": "Brazil"}, {"name": "Philip", "age": 35, "country": "USA"}, {"name": "Antony", "age": 35, "country": "UK"}]'
mapped_data = list(
    map(
        lambda p: Person(str(p["name"]), int(p["age"]), str(p["country"])),
        loads(data)))


class PersonPersistenceAdapterStub(PersonPersistenceAdapter):
    async def get(self) -> Awaitable[Iterable[Person]]:
        return mapped_data
