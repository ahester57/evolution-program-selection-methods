# ahester57


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

    @staticmethod
    def parameters() -> dict[str, tuple]:
        return {'prob': ('Enter Probability of Fittest Winner', 0.9)}
