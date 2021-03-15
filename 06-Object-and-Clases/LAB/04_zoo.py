class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        animal_to_display = []
        if species == "mammal":
            animal_to_display = self.mammals
        elif species == "fish":
            animal_to_display = self.fishes
        elif species == "bird":
            animal_to_display = self.birds
        species = species.capitalize() + "es" if species == "fish" else species.capitalize() + "s"

        return f'{species} in {self.name}: {", ".join(animal_to_display)}\nTotal animals: {Zoo.__animals}'


zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())

for _ in range(n):
    species, animal_name = input().split()
    zoo.add_animals(species, animal_name)

required_species = input()

print(zoo.get_info(required_species))

