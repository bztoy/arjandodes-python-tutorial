
from abc import ABC, abstractmethod
from typing import List
from enum import Enum, auto

class KindOfLeaf(Enum):
    SIMPLE = auto()
    COMPOUND = auto()

class KindOfRoot(Enum):
    tabroot = auto()
    fibrousroot = auto()


class RequiredWaterLevel(Enum):
    LOW: str = '1 per week'
    MEDIUM: str = '2-3 times/week'
    HIGH: str = 'Everday'


class CompondSubType(Enum):
    PINNATELY: str = 'Pinnately Compound'
    DOUBLE_PINNATELY: str = 'Double Pinnately Compound'
    PALMATELY: str = 'Palmately Compound'


class NoWaterLeftError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Plant(ABC):
    name: str
    kind_of_root: KindOfRoot
    is_it_fruit_plant: bool = False
    good_health_in_water_level: RequiredWaterLevel
    humidity_level: int = 0

    def __init__(self, name: str, root_kind: KindOfRoot, has_fruit: bool, leaf_kind: KindOfLeaf) -> None:
        self.name = name
        self.kind_of_root = root_kind
        self.is_it_fruit_plant = has_fruit
        self.kind_of_leave: KindOfLeaf = leaf_kind

    def watering(self, litre_of_water: int) -> None:
        self.humidity_level += litre_of_water

    def comsume_water(self, litre_of_consume_water: int = 1) -> None:
        if self.humidity_level <= 0:
            raise NoWaterLeftError(message=f'I am {self.name} and I have no water left, please give me some water')
        else:
            self.humidity_level -= litre_of_consume_water

    @abstractmethod
    def set_preferred_water_level(self, water_level: RequiredWaterLevel) -> None:
        """ Abstract Method in Python also can be implemented """
        self.good_health_in_water_level = water_level
        """ To implement in child class"""

class SimpleLeafPlant(Plant):

    def __init__(self, name: str, root_kind: KindOfRoot, has_fruit: bool, fruit_plant) -> None:
        self.is_it_fruit_plant = fruit_plant
        super().__init__(name, root_kind, has_fruit, KindOfLeaf.SIMPLE)
    
    def set_preferred_water_level(self) -> None:
        super().set_preferred_water_level(RequiredWaterLevel.HIGH)
        print(f"The water level is {self.good_health_in_water_level.name}")


class CompoundLeafPlant(Plant):
    compond_sub_type: str

    def __init__(self, name: str, root_kind: KindOfRoot, has_fruit: bool, csubtype: CompondSubType) -> None:
        self.compond_sub_type = csubtype
        super().__init__(name, root_kind, has_fruit, KindOfLeaf.COMPOUND)

    def set_preferred_water_level(self) -> None:
        """ testing : no need to call super method """
        print("This amizing plant no need any water")


def discover_the_farm() -> None:
    """ Discovering the farm """

    basket: List[Plant] = []

    basket.append(SimpleLeafPlant('Lemon', KindOfRoot.tabroot, True, True))
    mango = SimpleLeafPlant('Mango', KindOfRoot.tabroot, True, True)
    mango.watering(2)
    basket.append(mango)
    water_melon = SimpleLeafPlant('Water Melon', KindOfRoot.fibrousroot, True, True)
    water_melon.watering(1)
    try:
        for i in range(3):
            water_melon.comsume_water(i)
    except NoWaterLeftError as no_water_err:
        print(f'Error: {no_water_err}')
        print()

    basket.append(water_melon)
    basket.append(SimpleLeafPlant('Indian Jasmine', KindOfRoot.tabroot, False, True))
    basket.append(CompoundLeafPlant('Cha-om', KindOfRoot.tabroot, False, CompondSubType.DOUBLE_PINNATELY))
    tamarind = CompoundLeafPlant('Tamarind', KindOfRoot.tabroot, True, CompondSubType.PALMATELY)
    tamarind.watering(5)
    basket.append(tamarind)
    
    for plant in basket:
        fruit_info: str = 'Yeah, it has fruit' if plant.is_it_fruit_plant == True else 'Oh no, it has no yummy fruit'
        print(f"{plant.name} has {plant.kind_of_root.name}, humidity level: {plant.humidity_level} and {fruit_info}")
