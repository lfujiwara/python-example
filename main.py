import asyncio
from adapters.impl.person_persistence_adapter_stub import PersonPersistenceAdapterStub
from deprecated.class1 import action_1
from compat.action_1 import action_1 as action_1_compat


def main():
    print("Refactored result:", action_1_compat())
    print("Old result       :", action_1())

    print("")
    print("Refactored result (SA Countries):",
          action_1_compat(countryset="SA"))


if __name__ == "__main__":
    main()
