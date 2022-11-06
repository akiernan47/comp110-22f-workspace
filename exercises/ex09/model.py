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


    def tick(self) -> None:
        """New location after tick based on direction."""
        self.location = self.location.add(self.direction)

    
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
        if self.sickness == constants.INFECTED:
            return True
        return False


    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_infected() == True:
            return "red"
        else:
            return "gray"


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int) -> None:
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected >= cells or infected <= 0:
            raise ValueError("Improper starting infected value")
        for _ in range(infected, cells):
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


    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False