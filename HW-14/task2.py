
class Country():
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        new_country = Country(
            self.name + ' ' + other_country.name,
            self.population + other_country.population)
        return new_country


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.name)
print(bosnia_herzegovina.population)
