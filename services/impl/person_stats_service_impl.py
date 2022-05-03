from re import A
from typing import Awaitable
from adapters.person_persistence_adapter import PersonPersistenceAdapter
from services.person_stats_service import PersonStatsService


class PersonStatsServiceImpl(PersonStatsService):
  _persistence: PersonPersistenceAdapter
  _allowed_countries = {
    "Mexico",
    "Chile",
    "Colombia",
    "Brazil"
  }

  def __init__(self, persistence: PersonPersistenceAdapter, allowed_countries: set[str] | None = None):
    self._persistence = persistence
    self._allowed_countries = allowed_countries if allowed_countries is not None else self._allowed_countries

  async def get_info_about_countries(self) -> Awaitable[dict]:
    persons = await self._persistence.get()
    persons_countries = map(lambda person: person.country, persons)

    country_to_occurrences = dict()
    country_to_equivalence_class = dict()

    for country in persons_countries:
      if country not in self._allowed_countries: continue
      country_to_occurrences[country] = country_to_occurrences.get(country, 0) + 1
    
    for country, occurrences in country_to_occurrences.items():
      if occurrences == 1: country_to_equivalence_class[country] = "Uma"
      elif occurrences == 2: country_to_equivalence_class[country] = "Duas"
    
    return country_to_equivalence_class
