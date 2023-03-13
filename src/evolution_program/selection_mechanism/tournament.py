# ahester57

import random

from collections import deque

from evolution_program.selection_mechanism.mechanism import SelectionMechanism


class DeterministicTournament(SelectionMechanism):
    """Facilitates deterministic tournament selection.

    Attributes:
        population_fitnesses (tuple of float): The population fitness scores, in order.
        sum_of_fitnesses (float): The sum of the populations' fitness scores.
        maximize (bool): (False)[minimize]; (True)[maximize]. Default True.
        pop_size (int): The size of the population.
    """
    def __init__(self, population_fitnesses:tuple[float], sum_of_fitnesses:float=None, maximize:bool=True, **kwargs) -> None:
        """
        Initialize the parameters for deterministic tournament selection.

        Args:
            population_fitnesses (tuple of float): The population fitness scores, in order.
            sum_of_fitnesses (float): The sum of the populations' fitness scores.
            maximize (bool): (False)[minimize]; (True)[maximize]. Default True.
        """
        assert population_fitnesses is not None
        self.population_fitnesses = population_fitnesses
        self.sum_of_fitnesses = sum_of_fitnesses
        self.maximize = maximize
        if self.sum_of_fitnesses is None:
            self.sum_of_fitnesses = sum(population_fitnesses)
        self.pop_size = len(self.population_fitnesses)

    def next_population(self) -> tuple[int]:
        """Perform deterministic tournament selection on the population.

        Returns:
            tuple of int: An index-defined population after a round of deterministic tournament selection.
        """
        next_pop = []
        deque((next_pop.append(self._compete(self._choice(), self._choice())) for i in range(self.pop_size)), maxlen=0)
        return tuple(next_pop)

    def _choice(self) -> int:
        """Generate a random number representing the index of the chosen individual."""
        return random.choice(range(self.pop_size))

    def _compete(self, one:int, two:int) -> int:
        """Head-to-head combat between two individuals.

        Args:
            one (int): Index of first contender.
            one (int): Index of second contender.

        Returns:
            int: Index of winner.
        """
        result = self.population_fitnesses[one] > self.population_fitnesses[two]
        if self.maximize:
            return result
        return not result

    @staticmethod
    def parameters() -> dict[str, tuple]:
        return {}


class StochasticTournament(SelectionMechanism):
    """Facilitates stochastic tournament selection.

    Attributes:
        population_fitnesses (tuple of float): The population fitness scores, in order.
        sum_of_fitnesses (float): The sum of the populations' fitness scores.
        maximize (bool): (False)[minimize]; (True)[maximize]. Default True.
        pop_size (int): The size of the population.
        prob (float): The probability that the fittest individual wins the round.
    """
    def __init__(self, population_fitnesses:tuple[float], sum_of_fitnesses:float=None, maximize:bool=True, **kwargs) -> None:
        """
        Initialize the parameters for stochastic tournament selection.

        Args:
            population_fitnesses (tuple of float): The population fitness scores, in order.
            sum_of_fitnesses (float): The sum of the populations' fitness scores.
            maximize (bool): (False)[minimize]; (True)[maximize]. Default True.
            prob (float): The probability that the fittest individual wins the round.
        """
        assert population_fitnesses is not None
        assert 'prob' in kwargs.keys() and kwargs['prob'] > 0 and kwargs['prob'] < 1
        self.population_fitnesses = population_fitnesses
        self.sum_of_fitnesses = sum_of_fitnesses
        self.maximize = maximize
        self.prob = kwargs['prob']
        if self.sum_of_fitnesses is None:
            self.sum_of_fitnesses = sum(population_fitnesses)
        self.pop_size = len(self.population_fitnesses)

    def next_population(self) -> tuple[int]:
        """Perform deterministic tournament selection on the population.

        Returns:
            tuple of int: An index-defined population after a round of deterministic tournament selection.
        """
        next_pop = []
        deque((next_pop.append(self._compete(self._choice(), self._choice())) for i in range(self.pop_size)), maxlen=0)
        return tuple(next_pop)

    def _choice(self) -> int:
        """Generate a random number representing the index of the chosen individual."""
        return random.choice(range(self.pop_size))

    def _compete(self, one:int, two:int) -> int:
        """Head-to-head combat between two individuals.

        Args:
            one (int): Index of first contender.
            one (int): Index of second contender.

        Returns:
            int: Index of winner.
        """
        result = self.population_fitnesses[one] > self.population_fitnesses[two]
        if random.uniform(0, 1) > self.prob:
            result = not result
        if self.maximize:
            return result
        return not result

    @staticmethod
    def parameters() -> dict[str, tuple]:
        return {'prob': ('Enter Probability of Fittest Winner', 0.9)}
