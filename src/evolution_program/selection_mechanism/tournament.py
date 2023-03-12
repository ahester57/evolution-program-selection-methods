# ahester57


class DeterministicTournament:
    """Facilitates deterministic tournament selection."""
    def __init__(self, population_fitnesses, sum_of_fitnesses=None, maximize=True) -> None:
        """
        Initialize the parameters for deterministic tournament selection.
        """
        raise NotImplementedError


class StochasticTournament:
    """Facilitates stochastic tournament selection."""
    def __init__(self, population_fitnesses, sum_of_fitnesses=None, maximize=True) -> None:
        """
        Initialize the parameters for stochastic tournament selection.
        """
        raise NotImplementedError
