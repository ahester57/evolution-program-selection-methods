# ahester57

import numpy as np

from collections import deque
from typing import Callable

from evolution_program.chromosome import Chromosome


class Population:
    """Depicts a population of chromosomes.

    Attributes:
        members (tuple of Chromosome): Individual chromosome's values.
        _is_evaluated (bool): Whether this population has been evaluated yet.
    """
    def __init__(self, members:tuple[Chromosome]) -> None:
        """Initialize a population.

        Args:
            members (tuple of Chromosome): The population to be represented.
        """
        assert members is not None and type(members) is tuple
        self.members = members
        self._is_evaluated = False
        self._high_of = None
        self._low_of = None
        self._average_fitness = None
        self._sum_of_fitnesses = None

    def evaluate(self, fitness_function:Callable) -> None:
        """Evaluate the population with the given fitness function.

        Args:
            fitness_function (Callable): The "fitness function" or "objective function."
        """
        assert fitness_function is not None and callable(fitness_function)
        deque((c.evaluate(fitness_function) for c in self.members), maxlen=0) # execute the generator
        self._is_evaluated = True

    @property
    def high_score(self) -> Chromosome:
        if self._high_of is not None:
            return self._high_of
        assert self._is_evaluated
        high_fitness = 0
        for c in self.members:
            if c.fitness_score > high_fitness:
                high_fitness = c.fitness_score
                self._high_of = c
        return self._high_of

    @property
    def low_score(self) -> Chromosome:
        if self._low_of is not None:
            return self._low_of
        assert self._is_evaluated
        low_fitness = float('inf')
        for c in self.members:
            if c.fitness_score < low_fitness:
                low_fitness = c.fitness_score
                self._low_of = c
        return self._low_of

    @property
    def average_fitness(self) -> float:
        """\sum_{j=1}^N{f_j} / N"""
        if self._average_fitness is not None:
            return self._average_fitness
        assert self._is_evaluated and len(self.members) > 0
        self._average_fitness = self.sum_of_fitnesses / len(self.members)
        return self._average_fitness

    @property
    def sum_of_fitnesses(self) -> float:
        """\sum_{j=1}^N{f_j}"""
        if self._sum_of_fitnesses is not None:
            return self._sum_of_fitnesses
        assert self._is_evaluated
        self._sum_of_fitnesses = np.sum((c.fitness_score for c in self.members))
        return self._sum_of_fitnesses

    @property
    def is_evaluated(self) -> bool:
        return self._is_evaluated
