from dataclass_sample.guitars import Guitar
from dataclasses import dataclass
from enum import Enum, auto
from .guitars import Guitar, GuitarModel
from typing import Type, Optional

class ShopStatus(Enum):
    OPEN: True
    CLOSED: False
class InstrumentBrand(Enum):
    FENDER = 'fender'
    GIBSON = 'Gibson'


class AmplifierType(Enum):
    ANALOG: auto
    DIGITAL: auto


class Applifier:
    brand: str
    model: str
    system_type: AmplifierType
    
    def __init__(self, brand, model, system_type) -> None:
        self.brand = brand
        self.model = model
        self.system_type = system_type


class MusicShop():
    name: str
    location: str
    status: ShopStatus


    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location

    
    def open(self) -> None:
        self.status = ShopStatus.OPEN

    
    def close(self) -> None:
        self.status = ShopStatus.CLOSED

    
    def show_shelf_list(self) -> None:
        print("Shelf is empty now")


def music_shop() -> None:

    fstrat_darknight = Guitar(InstrumentBrand.FENDER, GuitarModel.STRATOCASTER, 'Dark Night', 500)
    ftele_blue = Guitar(InstrumentBrand.FENDER, GuitarModel.TELECASTER, 'Miami Blue', 400)
    ftele_mercury1 = Guitar(InstrumentBrand.FENDER, GuitarModel.TELECASTER, 'Mercury', 400)
    ftele_mercury2 = Guitar(InstrumentBrand.FENDER, GuitarModel.TELECASTER, 'Mercury', 401)
    ftele_sunburst = Guitar(InstrumentBrand.FENDER, GuitarModel.TELECASTER, 'Sienna Sunburst', 450)
    print(fstrat_darknight.model.value, repr(fstrat_darknight.model))

    print(fstrat_darknight == ftele_blue)
    print(ftele_mercury1 == ftele_mercury2 )
    print(ftele_sunburst > ftele_blue)
    ftele_blue.price = 600
    print(ftele_sunburst > ftele_blue)
    print(fstrat_darknight)
    