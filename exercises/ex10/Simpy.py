"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730515426"


class Simpy:
    """Simpy :p."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Simpy constructor."""
        self.values = values

    def __repr__(self) -> str:
        """String representation of class object."""
        return f"Simpy({self.values})"

    def fill(self, new_num: float, instances: int): 
        """Generates list of new numbers with a certain # of instances."""
        self.values = []
        i: int = 0
        while i < instances and len(self.values) != instances:
            self.values.append(new_num)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0):
        """Generates range by step given start and end point."""
        assert step != 0.0
        current_num: float = start
        if step > 0.0:
            while current_num < stop:
                self.values.append(current_num)
                current_num += step
        elif step < 0.0:
            while current_num > stop:
                self.values.append(current_num)
                current_num += step

    def sum(self) -> float:
        """Returns sum."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Addition operation override."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            simpy_track: list[float] = []
            i: int = 0
            while i < len(self.values):
                simpy_track.append(self.values[i] + rhs.values[i])
                i += 1
            result1: Simpy = Simpy(simpy_track)
            return result1
        elif isinstance(rhs, float):
            float_track: list[float] = []
            j: int = 0
            while j < len(self.values):
                float_track.append(self.values[j] + rhs)
                j += 1
            result2: Simpy = Simpy(float_track)
            return result2

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Exponentiation operation override."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            simpy_track: list[float] = []
            i: int = 0
            while i < len(self.values):
                simpy_track.append((self.values[i]) ** (rhs.values[i]))
                i += 1
            result1: Simpy = Simpy(simpy_track)
            return result1
        elif isinstance(rhs, float):
            float_track: list[float] = []
            j: int = 0
            while j < len(self.values):
                float_track.append((self.values[j]) ** (rhs))
                j += 1
            result2: Simpy = Simpy(float_track)
            return result2

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Equality operation override."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            simpy_eq: list[bool] = []
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    simpy_eq.append(True)
                    i += 1
                else:
                    simpy_eq.append(False)
                    i += 1
            return simpy_eq
        elif isinstance(rhs, float):
            float_eq: list[bool] = []
            j: int = 0
            while j < len(self.values):
                if self.values[j] == rhs:
                    float_eq.append(True)
                    j += 1
                float_eq.append(False)
                j += 1
            return float_eq

