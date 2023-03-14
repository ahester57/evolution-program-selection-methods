# ahester57

import numpy as np
import random

from evolution_program.selection_mechanism.mechanism import SelectionMechanism


class Proportional(SelectionMechanism):
    """Facilitates proportional selection with replacement.

    Attributes:
        population_fitnesses (tuple of float): The population fitness scores, in order.
        sum_of_fitnesses (float): The sum of the populations' fitness scores.
        maximize (bool): (False)[minimize]; (True)[maximize]. Default True.
        pop_size (int): The size of the population.
    """
    def __init__(self, population_fitnesses:tuple[float], sum_of_fitnesses:float=None, maximize:bool=True, **kwargs) -> None:
        """
        Initialize the parameters for proportional selection with replacement.

        Args:
            population_fitnesses (tuple of float): The population fitness scores, in order.
            sum_of_fitnesses (float, optional): The sum of the populations' fitness scores.
            maximize (bool, optional): (False)[minimize]; (True)[maximize]. Default True.
        """
        assert population_fitnesses is not None
        self.population_fitnesses = population_fitnesses
        self.sum_of_fitnesses = sum_of_fitnesses
        self.maximize = maximize
        if self.sum_of_fitnesses is None:
            self.sum_of_fitnesses = np.sum(population_fitnesses)
        self.pop_size = len(self.population_fitnesses)

    def next_population(self) -> tuple[int]:
        """Perform proportional selection with replacement on the population using fitness scores for weights.

        Returns:
            tuple of int: An index-defined population after a round of proportional selection.
        """
        return self._sample_from_pmf(self._generate_pmf())

    def _generate_pmf(self) -> tuple[float]:
        """Generate a probability mass function for given fitnesses.

        Returns:
            tuple of float: A population-sized list containing respective probablities of selection.
        """
        assert self.sum_of_fitnesses > 0
        pmf = tuple(f / self.sum_of_fitnesses for f in self.population_fitnesses)
        if not self.maximize:
            # Minimizing, invert the weights
            inv_pmf = [1.0 / w for w in pmf]
            sum_inv_pmf = np.sum(inv_pmf)
            pmf = tuple(tw / sum_inv_pmf for tw in inv_pmf)
        return pmf

    def _sample_from_pmf(self, pmf:tuple[float]) -> tuple[int]:
        """Generate a new index-defined population by stochastic choice based on the given pmf.

        Args:
            pmf (tuple of float): Probability Mass Function of population's fitness scores.

        Returns:
            tuple of int: A population-sized list containing indices of chosen individuals.
        """
        # de-tuple-fy
        return tuple(np.random.choice(np.arange(self.pop_size), size=self.pop_size, replace=True, p=pmf))

    @staticmethod
    def parameters() -> dict[str, tuple]:
        return {}
