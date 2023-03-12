# ahester57

from collections import deque

from evolution_program.chromosome import Chromosome


class Population:
    """Depicts a population of chromosomes.

    Attributes:
        members (tuple of Chromosome): Individual chromosome's values.
        evaluated (bool): Whether this population has been evaluated yet.
    """
    def __init__(self, members) -> None:
        """Initialize a population.

        Args:
            members (tuple of Chromosome): The population to be represented.
        """
        self.members = members
        self.evaluated = False
        self._high_of = None
        self._low_of = None
        self._average_fitness = None
        self._sum_of_fitnesses = None

    def evaluate(self, fitness_function) -> None:
        """Evaluate the population with the given fitness function.

        Args:
            fitness_function (lambda): The "fitness function" or "objective function."
        """
        deque((c.evaluate(fitness_function) for c in self.members), maxlen=0) # execute the generator
        self.evaluated = True

    @property
    def high_score(self) -> Chromosome:
        if self._high_of is not None:
            return self._high_of
        assert self.evaluated
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
        assert self.evaluated
        low_fitness = float('inf')
        for c in self.members:
            if c.fitness_score < low_fitness:
                low_fitness = c.fitness_score
                self._low_of = c
        return self._low_of

    @property
    def average_fitness(self) -> float:
        if self._average_fitness is not None:
            return self._average_fitness
        assert self.evaluated
        self._average_fitness = self.sum_of_fitnesses / len(self.members)
        return self._average_fitness

    @property
    def sum_of_fitnesses(self) -> float:
        """\sum_{j=1}^N{f_j}"""
        if self._sum_of_fitnesses is not None:
            return self._sum_of_fitnesses
        assert self.evaluated
        self._sum_of_fitnesses = sum(c.fitness_score for c in self.members)
        return self._sum_of_fitnesses
