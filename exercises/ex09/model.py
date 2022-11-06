"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730515426"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x: float = x
        self.y: float = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        xs: float = self.x + other.x
        ys: float = self.y + other.y
        result: Point = Point(xs, ys)
        return result

    def distance(self, other: Point) -> float:
        """Returns the distance between 2 points."""
        result: float = sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        return result


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def contract_disease(self) -> None:
        """Cell has become infected."""
        self.sickness = constants.INFECTED
        return None

    def is_vulnerable(self) -> bool:
        """Cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        return False

    def is_infected(self) -> bool:
        """Cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        return False

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_infected():
            return "red"
        elif self.is_vulnerable():
            return "gray"
        elif self.is_immune():
            return "blue"
        else:
            return "None"

    def tick(self) -> None:
        """New location after tick based on direction."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        return None

    def contact_with(self, other: Cell) -> None:
        """Determines conditions of contact."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        elif self.is_vulnerable() and other.is_infected():
            self.contract_disease()
        return None

    def immunize(self) -> None:
        """Cell becomes immune."""
        self.sickness = constants.IMMUNE
        return None

    def is_immune(self) -> bool:
        """Checks for immunity."""
        if self.sickness == constants.IMMUNE:
            return True
        return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, protected: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population: list[Cell] = []
        if infected >= cells or infected <= 0 or (protected + infected) >= cells or protected >= cells or protected < 0:
            raise ValueError("Improper starting value(s) of immune/infected cells") 
        for _ in range(protected):
            start_location1: Point = self.random_location()
            start_direction1: Point = self.random_direction(speed)
            cell_imm: Cell = Cell(start_location1, start_direction1)
            cell_imm.immunize()
            self.population.append(cell_imm)
        for _ in range(cells - (protected + infected)):
            start_location2: Point = self.random_location()
            start_direction2: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location2, start_direction2)
            self.population.append(cell)
        for _ in range(infected):
            start_location3: Point = self.random_location()
            start_direction3: Point = self.random_direction(speed)
            cell_inf: Cell = Cell(start_location3, start_direction3)
            cell_inf.contract_disease()
            self.population.append(cell_inf)
            
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()
        return None

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        result: Point = Point(start_x, start_y)
        return result

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        result: Point = Point(direction_x, direction_y)
        return result

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        elif cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        elif cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        elif cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checks contact of two cells."""
        check_list: list[Cell] = []
        for x1 in self.population:
            for x2 in self.population:
                if x1 != x2 and x1 not in check_list:
                    if x1.location.distance(x2.location) < constants.CELL_RADIUS:
                        x1.contact_with(x2)
                        check_list.append(x1)
                        check_list.append(x2)
                
    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True
