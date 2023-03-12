# ahester57

import random
import time

from collections import deque

from chromosome import Chromosome
from population import Population
from selection_mechanism.proportional import Proportional


class GA:
    """
    A class for a genetic algorithm (GA).

    Attributes:
        dims (int): Dimensions of chromosome vector. Defaults to 3.
        domain_lower (float): Gene value lower bound. Defaults to -7.0.
        domain_upper (float): Gene value upper bound. Defaults to 4.0.
        mutation_standard_deviation (float): Function of upper & lower bounds.
        pop_size (int): Population size. Defaults to 30.
        p_c (float): Probability of crossover. In range [0, 1]. Defaults to 0.8.
        p_m (float): Probability of mutation. In range [0, 1]. Defaults to 0.1.
        t_max (int): Maximum iterations/generations. Defaults to 50.
        rand_seed (int): Seed given to RNG calculated from parameters.
        population (Population): Collection of current generation's individual chromosomes.
        fitness_function (lambda): The "fitness function" or "objective function."
        maximize (bool): (False)[minimize]; (True)[maximize]. Default True.
    """

    def __init__(
        self,
        dims=3,
        domain_lower=-7.0,
        domain_upper=4.0,
        pop_size=30,
        p_c=0.8,
        p_m=0.1,
        t_max=50,
        rand_seed=None,
        fitness_function=lambda genes : sum([x**2 for x in genes]),
        maximize=True
    ) -> None:
        """
        Initialize the parameters for a genetic algorithm.

        Args:
            dims (int, optional): Dimensions of chromosome vector. Defaults to 3.
            domain_lower (float, optional): Gene value lower bound. Defaults to -7.0.
            domain_upper (float, optional): Gene value upper bound. Defaults to 4.0.
            pop_size (int, optional): Population size. Defaults to 30.
            p_c (float, optional): Probability of crossover. In range [0, 1]. Defaults to 0.8.
            p_m (float, optional): Probability of mutation. In range [0, 1]. Defaults to 0.1.
            t_max (int, optional): Maximum iterations/generations. Defaults to 50.
            rand_seed(int, optional): Seed for random number generator.
            fitness_function (lambda, optional): Function of \vec{x}. Returns (float).
            maximize (bool, optional): (False)[minimize]; (True)[maximize]. Default True.
        """
        assert dims > 0
        assert pop_size > 0
        assert p_c >= 0 and p_c <= 1
        assert p_m >= 0 and p_m <= 1
        assert t_max > 0
        assert fitness_function is not None and callable(fitness_function)
        assert maximize in (False, True)
        self.dims = int(dims)
        self.domain_lower = float(domain_lower)
        self.domain_upper = float(domain_upper)
        self.mutation_standard_deviation = (self.domain_upper - self.domain_lower) / 1000 # where divisor is 10**(precision wanted)
        self.pop_size = int(pop_size)
        self.p_c = float(p_c)
        self.p_m = float(p_m)
        self.t_max = int(t_max)
        self.t = 0
        self.population = None
        self.fitness_function = fitness_function
        self.maximize = maximize
        self.rand_seed = None
        self.seed_random(rand_seed)

    def simulate(self) -> None:
        """Simulate the genetic algorithm with configured parameters."""
        self.initialize_population()
        self.evaluate_population()
        deque((self.iterate() for _ in range(self.t_max)), maxlen=0) # execute generator

    def iterate(self) -> None:
        """Perform one iteration of the simulation."""
        self.t = self.t + 1
        if self.t > self.t_max:
            return
        self.population = self.create_next_population()
        self.evaluate_population()
        if self.t % 10 == 0 or self.t == self.t_max:
            self.print_stats()

    def create_next_population(self) -> Population:
        """Perform selection, crossover, and mutation on the population.

        Returns:
            Population: The proposed next generation of the population.
        """
        return Population(self.gene_wise_mutation(self.single_point_crossover(self.selection_mechanism())))

    def selection_mechanism(self) -> tuple[Chromosome]:
        """Perform selection on the population.

        Returns:
            tuple of Chromosome: A new population after a round of selection.
        """
        Chosen_Mechanism = [Proportional][0]
        mechanism = Chosen_Mechanism(tuple(c.fitness_score for c in self.population.members), self.population.sum_of_fitnesses, self.maximize)
        return tuple(self.population.members[i] for i in mechanism.next_population())

    def single_point_crossover(self, population) -> tuple[Chromosome]:
        """Perform single cut-point crossover on the population using self.p_c as probability of occurrence.

        Args:
            population (tuple of Chromosome): The population to act upon.

        Returns:
            tuple of Chromosome: A new population after a round of single cut-point crossover.
        """
        next_gen = []
        for i in range(0, self.pop_size, 2):
            p1 = population[i]
            p2 = population[i+1]
            if random.uniform(0, 1) > self.p_c:
                # no crossover, send parents to next gen
                next_gen.append(p1)
                next_gen.append(p2)
                continue
            cut_point = random.randrange(1, self.dims)
            next_gen.append(Chromosome(tuple(p1.alleles[0:cut_point] + p2.alleles[cut_point:self.dims])))
            next_gen.append(Chromosome(tuple(p2.alleles[0:cut_point] + p1.alleles[cut_point:self.dims])))
        return tuple(next_gen)

    def gene_wise_mutation(self, population) -> tuple[Chromosome]:
        """Perform gene-wise mutation on the population using self.p_m as probability of occurrence.

        Args:
            population (tuple of Chromosome): The population to act upon.

        Returns:
            tuple of Chromosome: A new population after a round of gene-wise mutation.
        """
        next_gen = []
        for c in population:
            next_chromosome = []
            for a in c.alleles:
                if random.uniform(0, 1) > self.p_m:
                    # no mutation
                    next_chromosome.append(a)
                    continue
                next_chromosome.append(a + random.normalvariate(0, self.mutation_standard_deviation**2))
            next_gen.append(Chromosome(tuple(next_chromosome)))
        return tuple(next_gen)

    def evaluate_population(self) -> None:
        """Evaluate an entire iteration/generation's population.
        
        Track fitness scores using a tuple containing (index, fitness_score).
        """
        self.population.evaluate(self.fitness_function)

    def initialize_population(self) -> None:
        """
        Initialize a population for the GA within configured parameters.
        
        This can only happen when there is no current population.
        """
        if self.population is not None:
            raise RuntimeError('Population already initialized')
        self.population = Population(
            tuple(
                Chromosome(
                    tuple(
                        random.uniform(self.domain_lower, self.domain_upper)
                        for _ in range(self.dims)
                    )
                )
                for _ in range(self.pop_size)
            )
        )

    def seed_random(self, given_seed=None) -> None:
        """
        Initialize the random seed using a made-up via hand-waving function.
        
        This can only happen when there is no current random seed.

        Args:
            given_seed (int, optional): Seed for random number generator
        """
        if self.rand_seed is not None:
            raise RuntimeError('Random already seeded')
        if given_seed is not None:
            self.rand_seed = int(given_seed)
        else:
            random.seed(time.time())
            # seed random using datetime, then export the result of that to re-seed
            self.rand_seed = random.randint(1, 123456789)
        print(f'Seeding random with {self.rand_seed}')
        random.seed(self.rand_seed)

    def print_stats(self) -> None:
        print(f'----------- Gen. {self.t} ---------------')
        print(f'High  Fitness: {self.population.high_score.fitness_score} by {self.population.high_score.alleles}')
        print(f'Low   Fitness: {self.population.low_score.fitness_score} by {self.population.low_score.alleles}')
        print(f'Avg   Fitness: {self.population.average_fitness}')

    @property
    def population(self) -> Population:
        return self._population

    @population.setter
    def population(self, value) -> None:
        assert (value is None and self.pop_size is not None) or len(value.members) == self.pop_size
        self._population = value


if __name__ == '__main__':
    GA(rand_seed=None).simulate()
