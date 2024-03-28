class House:
    def __init__(self, first_name, last_name, apartment_number, has_dog=False):
        self.first_name = first_name
        self.last_name = last_name
        self.apartment_number = apartment_number
        self.has_dog = has_dog

object_one = House("Ivan", "Shopov", 15)

print(object_one.first_name)
print(object_one.last_name)
print(object_one.apartment_number)
print(object_one.has_dog)