import asyncio
from adapters.impl.person_persistence_adapter_stub import PersonPersistenceAdapterStub
from services.impl.person_stats_service_impl import PersonStatsServiceImpl

SA_COUNTRIES = [
    "Chile",
    "Colombia",
    "Brazil"
]


def action_1(**kwargs):
    countries = SA_COUNTRIES if kwargs.get("countryset") == "SA" else None

    persistence_adapter = PersonPersistenceAdapterStub()
    service = PersonStatsServiceImpl(persistence_adapter, countries)

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    return loop.run_until_complete(service.get_info_about_countries())
