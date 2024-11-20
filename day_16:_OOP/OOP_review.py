class Dog():
    def __init__(self,name):
        self.name = name
        print(f"{self.name} has been instantiated.")
    bark = "woof"
    def poodleFurz(self,floof):
        print(f"My floof is {floof}. ")

reverie = Dog("Reverie")

print(reverie.bark)

reverie.poodleFurz("gray")