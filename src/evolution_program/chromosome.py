# ahester57

import numpy as np

from typing import Callable


class Chromosome:
    """Depicts one individual in the population.

    Attributes:
        alleles (tuple of float): Individual chromosome's values.
        fitness_score (float): The fitness score
    """

    def __init__(self, alleles:np.ndarray[np.float64]) -> None:
        """Depicts one individual in the population.

        Args:
            alleles (tuple of float): Individual chromosome's values.
        """
        assert alleles is not None and type(alleles) is np.ndarray
        self.alleles = alleles
        self.fitness_score = None

    def evaluate(self, fitness_function:Callable) -> None:
        """Perform an evaluation of this chromosome with given fitness function.

        Args:
            fitness_function (Callable): Function of \vec{x}. Returns (float).

        Returns:
            float: The fitness score.
        """
        assert fitness_function is not None and callable(fitness_function)
        self.fitness_score = fitness_function(self.alleles)

    @property
    def fitness_score(self) -> np.float64:
        return self._fitness_score

    @fitness_score.setter
    def fitness_score(self, value:np.float64) -> None:
        assert value is None or type(value) is np.float64
        self._fitness_score = value

    @property
    def is_evaluated(self) -> bool:
        return self.fitness_score is not None
