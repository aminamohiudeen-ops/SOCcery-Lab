def normal_log_activity():
    pass

normal_log_activity()

class Cat:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def meow(self):
        return f"{self.name} says meow!"

cat_1 = Cat("Bean", "Bipolar")

print(cat_1.name)
print(cat_1.meow())
