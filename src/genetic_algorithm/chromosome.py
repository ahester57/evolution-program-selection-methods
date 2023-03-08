# ahester57


class Chromosome:
    """Depicts one individual in the population.

    Attributes:
        alleles (tuple of float): Individual chromosome's values.
        fitness_score (float): The fitness score
    """

    def __init__(self, alleles=None) -> None:
        """Depicts one individual in the population.

        Args:
            alleles (tuple of float): Individual chromosome's values.
        """
        assert alleles is not None and type(alleles) is tuple
        self.alleles = alleles
        self.fitness_score = None

    def evaluate(self, fitness_function=None) -> None:
        """Perform an evaluation of this chromosome with given fitness function.

        Args:
            fitness_function (lambda): Function of \vec{x}. Returns (float).

        Returns:
            float: The fitness score.
        """
        assert fitness_function is not None and callable(fitness_function)
        self.fitness_score = fitness_function(self.alleles)

    @property
    def fitness_score(self) -> float:
        return self._fitness_score

    @fitness_score.setter
    def fitness_score(self, value) -> None:
        assert value is None or type(value) is float
        self._fitness_score = value