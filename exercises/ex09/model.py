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


    def __init__(self, x: float, y: float) -> None:
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y


    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)


    def distance(self, other: Point) -> float:
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point) -> None:
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction


    def contract_disease(self) -> None:
        """Cell has become infected."""
        self.sickness = constants.INFECTED


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
        else:
            return "blue"


    def tick(self) -> None:
        """New location after tick based on direction."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()


    def contact_with(self, other: Cell) -> None:
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        elif self.is_vulnerable() and other.is_infected():
            self.contract_disease()


    def immunize(self) -> None:
        self.sickness = constants.IMMUNE


    def is_immune(self) -> bool:
        if self.sickness == constants.IMMUNE:
            return True
        return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, protected: int = 0) -> None:
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected >= cells or infected <= 0 or (protected + infected) >= cells:
            raise ValueError("Improper starting value(s) of immune/infected cells")
        for _ in range(protected):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.immunize()
            self.population.append(cell)
        for _ in range(cells - (protected + infected)):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for _ in range(infected):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.contract_disease()
            self.population.append(cell)
        
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()


    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)


    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)


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
        check_list: list = []
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
        