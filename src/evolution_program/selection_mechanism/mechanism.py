# ahester57


class SelectionMechanism:
    def __init__(self, population_fitnesses:tuple[float], sum_of_fitnesses:float=None, maximize:bool=True, **kwargs) -> None:
        raise NotImplementedError

    def next_population(self) -> tuple[int]:
        raise NotImplementedError

    @property
    def parameters(self) -> dict[str, tuple]:
        raise NotImplementedError
