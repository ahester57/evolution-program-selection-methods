# ahester57

from evolution_program.selection_mechanism.mechanism import SelectionMechanism


class LinearRanking(SelectionMechanism):
    """Facilitates linear ranking selection with replacement.

    Attributes:
        population_fitnesses (tuple of float): The population fitness scores, in order.
        sum_of_fitnesses (float): The sum of the populations' fitness scores.
        maximize (bool): (False)[minimize]; (True)[maximize]. Default True.
        pop_size (int): The size of the population.
        max (float): The expected number of copies of the fittest individual in the next generation.
    """
    def __init__(self, population_fitnesses, sum_of_fitnesses=None, maximize=True, **kwargs) -> None:
        """
        Initialize the parameters for linear ranking selection with replacement.

        Args:
            population_fitnesses (tuple of float): The population fitness scores, in order.
            sum_of_fitnesses (float): The sum of the populations' fitness scores.
            maximize (bool): (False)[minimize]; (True)[maximize]. Default True.
            pop_size (int): The size of the population. 
            max (float): The expected number of the most fit individual in the next generation. [1, 2] - Extinctive.
        """
        assert population_fitnesses is not None
        assert 'max' in kwargs.keys() and type(kwargs['max']) is float and kwargs['max'] >= 1 and kwargs['max'] <= 2
        self.population_fitnesses = population_fitnesses
        self.sum_of_fitnesses = sum_of_fitnesses
        self.maximize = maximize
        self.max = kwargs['max']
        if self.sum_of_fitnesses is None:
            self.sum_of_fitnesses = sum(population_fitnesses)
        self.pop_size = len(self.population_fitnesses)

    @staticmethod
    def parameters() -> dict[str:tuple]:
        return {'max': ('Enter Max (from 1 to 2)', 1.2)}
