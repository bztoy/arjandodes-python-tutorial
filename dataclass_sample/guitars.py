from dataclasses import dataclass, field
from enum import Enum, auto

class InstrumentBrand(Enum):
    FENDER = 'fender'
    GIBSON = 'Gibson'


class GuitarModel(Enum):
    STRATOCASTER = "American Professional II Stratocaster"
    TELECASTER = "American Professional II Telecaste"
    AC_STRATOCASTER = "American Acoustasonic Stratocaster"
    AC_TELECASTER = "American Acoustasonic Telecaster"


@dataclass(order=True)
class Guitar:
    # sort_index is using for sorting only (field is the keyword)
    sort_index: float = field(init=False, repr=False)
    brand: InstrumentBrand
    model: GuitarModel
    color: str
    price: float

    def __post_init__(self):
        self.sort_index = self.price


# if frozen is set, object.__setattr__ is needed to set value to sort index
@dataclass(order=True, frozen=True)
class AcusticGuitar:
    sort_index: float = field(init=False, repr=False)
    brand: InstrumentBrand
    model: GuitarModel
    color: str
    price: float

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.price)

    def __str__(self) -> str:
        return f'{self.model}, {self.color}, {self.price}'
