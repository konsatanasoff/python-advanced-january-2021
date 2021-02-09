countries = input().split(", ")
capitals = input().split(", ")

result = {country: capital for country, capital in zip(countries, capitals)}

[print(f"{country} -> {capital}") for country, capital in result.items()]