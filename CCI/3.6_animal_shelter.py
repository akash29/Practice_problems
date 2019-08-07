class AnimalShelter:
    def __init__(self):
        self.stack_any=[]
        self.queue_any = []
        self.stack_dog=[]
        self.queue_dog=[]
        self.stack_cat=[]
        self.queue_cat=[]

    def enqueue(self, animal_type, val):
        animal_obj = self.object(animal_type,val)
        self.stack_any.append(animal_obj)
        if animal_type.lower() == "dog":
            self.stack_dog.append(animal_obj)
        elif animal_type.lower() == "cat":
            self.stack_cat.append(animal_obj)
        else:
            raise Exception("Unsupported animal type")

    def dequeueAny(self):
        while self.stack_any:
            self.queue_any.append(self.stack_any.pop())
        while self.stack_dog:
            self.queue_dog.append(self.stack_dog.pop())
        while self.stack_cat:
            self.queue_cat.append(self.stack_cat.pop())

        if self.queue_any:
            item = self.queue_any.pop()
            if item.type.lower() == "dog":
                self.queue_dog.pop()
            elif item.type.lower() == "cat":
                self.queue_cat.pop()
            return item.type, item.val

        return None

    def dequeueDog(self):
        while self.stack_dog:
            self.queue_dog.append(self.stack_dog.pop())

        if self.queue_dog:
            item = self.queue_dog.pop()
            return item.type,item.val
        return None

    def dequeueCat(self):
        while self.stack_cat:
            self.queue_cat.append(self.stack_cat.pop())

        if self.stack_cat:
            item = self.stack_cat.pop()
            return item.type, item.val

        return None

    class object:
        def __init__(self, animal_type,val):
            self.type = animal_type
            self.val = val


animals = AnimalShelter()
animals.enqueue("Dog",1)
animals.enqueue("Cat",2)
animals.enqueue("Dog",3)
animals.enqueue("Dog",4)
animals.enqueue("Dog",5)
animals.enqueue("Cat",1)
animals.enqueue("Cat",8)
animals.enqueue("rat",100)
print(animals.dequeueAny())
print(animals.dequeueAny())
print(animals.dequeueDog())
print(animals.dequeueCat())