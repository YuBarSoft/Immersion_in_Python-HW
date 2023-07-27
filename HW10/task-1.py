# Задача 1. Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Animals:
    def __init__(self, name, tail):
        self.name = name
        self.tail = tail

    def name_animal(self):
        return self.name


class Fish(Animals):
    def __init__(self, fresh_water, deep, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fresh_water = fresh_water
        self.deep = deep

    def specific(self):
        if self.fresh_water:
            return True
        return False

    def check_deep(self):
        if self.deep <= 3:
            return f"Мелководное до {self.deep} метров"
        elif 3 < self.deep < 20:
            return f"Среднеглубинное до {self.deep} метров"
        return f"Глубоководное глубже {self.deep} метров"


class Birds(Animals):

    def __init__(self, wingspan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wingspan = wingspan

    def specific(self):
        wing_lengh = self.wingspan * 0, 45
        return wing_lengh


class Mammals(Animals):

    def __init__(self, hibernate, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hibernate = hibernate

    def specific(self):
        if self.hibernate:
            return True
        return False


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == "Fish":
            return Fish(**kwargs)
        elif animal_type == "Birds":
            return Birds(**kwargs)
        elif animal_type == "Mammals":
            return Mammals(**kwargs)
        else:
            raise ValueError("Invalid animal type")


fish_params = {"name": "Salmon", "tail": True, "fresh_water": True, "deep": 5}
fish = AnimalFactory.create_animal("Fish", **fish_params)

bird_params = {"name": "Eagle", "tail": False, "wingspan": 2.5}
bird = AnimalFactory.create_animal("Birds", **bird_params)

mammal_params = {"name": "Bear", "tail": True, "hibernate": True}
mammal = AnimalFactory.create_animal("Mammals", **mammal_params)

