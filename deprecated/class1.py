import json


def action_1():

    # Data é o resultado da query acima, colocamos como json para ficar mais fácil de você usar!
    data = '[{"name": "Souza", "age": 35, "country": "Mexico"}, {"name": "Andrade", "age": 35, "country": "Chile"}, {"name": "Felipe", "age": 35, "country": "Colombia"}, {"name": "Sérgio", "age": 35, "country": "Colombia"}, {"name": "Lisboa", "age": 35, "country": "Colombia"}, {"name": "Souza Lima", "age": 35, "country": "Brazil"}, {"name": "Philip", "age": 35, "country": "USA"}, {"name": "Antony", "age": 35, "country": "UK"}]'

    y = json.loads(data)
    country = {}
    for x in y:
        if x["country"] in country:
            country[x["country"]] += 1
        elif x["country"] == "Mexico" or x["country"] == "Chile" or x["country"] == "Colombia" or x["country"] == "Brazil":
            country[x["country"]] = 1

        r = {}
        for x in country:
            if country[x] == 1:
                r[x] = "Uma"
            elif country[x] == 2:
                r[x] = "Duas"

    return r
