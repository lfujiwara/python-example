class Person:
    name: str
    age: int
    country: str

    def __init__(self, name: str, age: int, country: str) -> None:
        self.name = name
        self.age = age
        self.country = country
