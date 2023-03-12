# ahester57


class SelectionMechanism:
    def __init__(self) -> None:
        raise NotImplementedError

    def next_population(self) -> tuple[int]:
        raise NotImplementedError

    @property
    def parameters(self) -> dict[str, tuple]:
        raise NotImplementedError
