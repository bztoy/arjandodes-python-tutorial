
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto

class PrintUtil(Enum):
    LEADING_INDENT: str = ' - '

class Manufacturer(Enum):
    HONDA: str = 'Honda'
    YAMAHA: str = 'Yamaha'
    SUZUKI: str = 'Suzuki'
    APRILIA: str = 'Aprilia'
    DUCATI: str = 'Ducati'
    KTM: str = 'KTM'

class BikeModel(Enum):
    RC213V = auto()
    YZRM1 = auto()
    GSXRR = auto()
    RSGP = auto()
    DESMOCEDICI = auto()
    RC16 = auto()

class Nation(Enum):
    ESP: str = 'Spain'
    ITA: str = 'Italia'
    JPN: str = 'Japan'
    GBR: str = 'United Kingdom'
    FRN: str = 'France'
    MCO: str = 'Monaco'
    MYS: str = 'Malaysia'
    AUT: str = 'Austria'
    AUS: str = 'Australia'
    ZAF: str = 'South Africa'
    PRT: str = 'Portugal'


class TeamStatus(Enum):
    FACTORY: str = 'Factory'
    INDEPENDENT: str = 'Independent'


class EngineType(Enum):
    V4 = auto()
    I4 = auto()


@dataclass
class Bike():
    model: BikeModel
    engine_config: EngineType


@dataclass
class Factory():
    manuf: Manufacturer
    bike: Bike


@dataclass
class Team():
    name: str
    status: TeamStatus
    nation: Nation
    bike: Bike


@dataclass
class Rider():
    name: str
    racing_number: str
    nation: Nation
    team: Team


@dataclass
class FullTimeRider(Rider):
    total_allocated_engine: int = 7
    total_allocated_tyre: int = 200


@dataclass
class TestRider(Rider):
    total_allocated_engine: int = 99
    total_allocated_tyre: int = 50


class MotoGP():
    season: int
    factories: Dict = {}

    def __init__(self, season) -> None:
        self.season = season
        self.teams: List[Team] = []
        self.riders: List[Rider] = []
        self.init_factory()

    def init_factory(self) -> None:
        self.factories[Manufacturer.HONDA.value] = Factory(Manufacturer.HONDA, Bike(BikeModel.RC213V, EngineType.V4))
        self.factories[Manufacturer.DUCATI.value] = Factory(Manufacturer.DUCATI, Bike(BikeModel.DESMOCEDICI, EngineType.V4))
        self.factories[Manufacturer.APRILIA.value] = Factory(Manufacturer.APRILIA, Bike(BikeModel.RSGP, EngineType.V4))
        self.factories[Manufacturer.KTM.value] = Factory(Manufacturer.KTM, Bike(BikeModel.RC16, EngineType.V4))
        self.factories[Manufacturer.SUZUKI.value] = Factory(Manufacturer.SUZUKI, Bike(BikeModel.GSXRR, EngineType.I4))
        self.factories[Manufacturer.YAMAHA.value] = Factory(Manufacturer.YAMAHA, Bike(BikeModel.YZRM1, EngineType.I4))

    def _list_team_by_status(self, status: TeamStatus) -> List[Team]:
        """ Return a list of team by its status"""
        return [team for team in self.teams if team.status is status]

    def add_team(self, team: Team) -> None:
        """ Add a team """
        self.teams.append(team)

    def add_rider(self, rider: Rider) -> None:
        """ Add a rider"""
        self.riders.append(rider)

    def start_broadcast(self) -> None:
        print(f"Welcome to MotoGP {self.season} season")
        print()

    def show_team_info(self) -> None:
        """Show Teams Infographic"""

        print(f"There are {len(self.teams)} is copeting in the MotoGP class this year")
        for team in self.teams:
            print(PrintUtil.LEADING_INDENT.value, team.name)
        print()

    def show_rider_info(self) -> None:
        """Show Rider Infographic"""

        print(f"There are {len(self.riders)} is copeting in the MotoGP class this year")
        for rider in self.riders:
            print(PrintUtil.LEADING_INDENT.value, rider.name, rider.racing_number)
        print()

    def list_factory_team(self) -> None:
        print("Factory teams are including")
        teams = self._list_team_by_status(TeamStatus.FACTORY)
        for team in teams:
            print(PrintUtil.LEADING_INDENT.value, team.name, '\t', team.nation)
        print()

def run_code_smell() -> None:
    motogp = MotoGP(2021)

    # create teams
    motogp.add_team(Team('Repsol Honda', TeamStatus.FACTORY, Nation.JPN, motogp.factories[Manufacturer.HONDA.value].bike ))
    motogp.add_team(Team('LCR Honda', TeamStatus.INDEPENDENT, Nation.MCO, motogp.factories[Manufacturer.HONDA.value].bike))
    motogp.add_team(Team('Monster Yamaha Factory', TeamStatus.FACTORY, Nation.JPN, motogp.factories[Manufacturer.YAMAHA.value].bike))
    motogp.add_team(Team('Petronas Yamaha SRT', TeamStatus.INDEPENDENT, Nation.JPN, motogp.factories[Manufacturer.YAMAHA.value].bike))
    motogp.add_team(Team('Suzuki Ecstar', TeamStatus.FACTORY, Nation.JPN, motogp.factories[Manufacturer.SUZUKI.value].bike))

    # create riders
    motogp.add_rider(FullTimeRider("Joan Mir", '36', Nation.ESP, motogp.factories[Manufacturer.SUZUKI.value]))
    motogp.add_rider(FullTimeRider("Alex Rins", '42', Nation.ESP, motogp.factories[Manufacturer.SUZUKI.value]))
    
    # broadcasting
    motogp.start_broadcast()
    motogp.show_team_info()
    motogp.show_rider_info()
    motogp.list_factory_team()
