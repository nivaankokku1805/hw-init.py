class Dog:
    # Class variable
    species = "Canis lupus familiaris"

    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    def display_details(self):
        # Method to display dog details
        print(f"Name: {self.name}, Breed: {self.breed}, Species: {Dog.species}")


# Creating two instances of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Displaying details of the dogs
dog1.display_details()
dog2.display_details()
