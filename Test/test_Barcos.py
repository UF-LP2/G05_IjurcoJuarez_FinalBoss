import pytest
from src.Barcos import cShip
from src.Barcos import Cargo
from src.Barcos import Cruise
def test_is_worth_it_mayor20():
    ship= cShip(100,50)     #50*1.5=75 -> draft > 20
    assert ship.is_worth_it() == True


def test_is_worth_it_menor20():
    ship= cShip(100,60)     #60*1.5=90 -> draft < 20
    assert ship.is_worth_it() == False


def test_is_worth_it_mayor20_cargo():
    cargo= Cargo(100,1, 5000, 200)     # draft =4350 > 20
    assert cargo.is_worth_it() == True


def test_is_worth_it_menor20_cargo():
    cargo = Cargo(100, 1, 500, 200)  # draft =-150 < 20
    assert cargo.is_worth_it() == False


def test_is_worth_it_mayor20_cruise():
    cruise= Cruise(70,400, 50)     # draft =255 > 20
    assert cruise.is_worth_it() == True


def test_is_worth_it_menor20_cruise():
    cruise = Cruise(500, 655, 100)  # draft =5 < 20
    assert cruise.is_worth_it() == False


