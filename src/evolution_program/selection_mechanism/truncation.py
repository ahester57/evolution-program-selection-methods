# ahester57

import numpy as np

from evolution_program.selection_mechanism.mechanism import SelectionMechanism


class Truncation(SelectionMechanism):
    """Facilitates truncation selection with replacement.

    Attributes:
        population_fitnesses (tuple of float): The population fitness scores, in order.
        sum_of_fitnesses (float): The sum of the populations' fitness scores.
        maximize (bool): (False)[minimize]; (True)[maximize]. Default True.
        pop_size (int): The size of the population.
    """
    def __init__(self, population_fitnesses:tuple[float], sum_of_fitnesses:float=None, maximize:bool=True, **kwargs) -> None:
        """Initialize the parameters for truncation selection with replacement.

        Args:
            population_fitnesses (tuple of float): The population fitness scores, in order.
            sum_of_fitnesses (float): The sum of the populations' fitness scores.
            maximize (bool): (False)[minimize]; (True)[maximize]. Default True.
            tao (float): The cut-line. i.e., Select only from top tao%. 
        """
        assert population_fitnesses is not None
        assert 'tao' in kwargs.keys() and type(kwargs['tao']) is float and kwargs['tao'] > 0 and kwargs['tao'] < 1
        self.population_fitnesses = population_fitnesses
        self.sum_of_fitnesses = sum_of_fitnesses
        self.maximize = maximize
        self.tao = kwargs['tao']
        if self.sum_of_fitnesses is None:
            self.sum_of_fitnesses = sum(population_fitnesses)
        self.pop_size = len(self.population_fitnesses)

    def next_population(self) -> tuple[int]:
        """Perform truncation selection on the population.

        Returns:
            tuple of int: An index-defined population after a round of truncation selection.
        """
        return self._sample_from_top_tao(self._generate_top_tao())

    def _generate_top_tao(self) -> list[tuple]:
        """Generate a pool of members for reproduction based on top tao% fitness scores.

        Returns:
            list of tuple: A non-population-sized list containing respective indices and fitness scores.
        """
        # TODO: numpy-ify this
        assert self.sum_of_fitnesses > 0
        sorted_keep_indices = [(i, f) for i, f in enumerate(self.population_fitnesses)]
        sorted_keep_indices.sort(key=lambda x:x[1], reverse=self.maximize)
        return [tt[0] for tt in sorted_keep_indices[:int(self.pop_size * self.tao)]]

    def _sample_from_top_tao(self, top_tao:list[tuple]) -> tuple[int]:
        """Generate a new index-defined population by stochastic choice based on the given members.

        Args:
            top_tao (list of tuple): Pool of members available for sampling.

        Returns:
            tuple of int: A population-sized list containing indices of chosen individuals.
        """
        return np.random.choice(top_tao, size=self.pop_size, replace=True)

    @staticmethod
    def parameters() -> dict[str, tuple]:
        return {'tao': ('Enter Tao (top percent cut-line)', 0.4)}