# ahester57

from genetic_algorithm import ga

class App:
    """Simple class to be used as an entrypoint."""

    def __init__(self) -> None:
        self.ga = ga.GA()

    def start(self) -> None:
        self.ga.simulate()


if __name__ == '__main__':
    app = App()
    app.start()
