# This is for my pet class.

# This time I'm instantiating a pet class with __init__ method.
# It has five parameters assigned attributes.
class Pets:
    def __init__(self, id, animal_type, owner, name, age):
        self.id = id
        self.animal_type = animal_type
        self.owner = owner
        self.name = name
        self.age = age

    # This used to generate description of a pet's details,
    # It will help to display information about pets in your program.
    def get_info(self):
        return f"You have chosen {self.name}, the {self.animal_type}. {self.name} is {self.age} years old and {self.name}'s owner is {self.owner}."
