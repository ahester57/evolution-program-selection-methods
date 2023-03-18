# ahester57

from evolution_program.menu import GAMenu


class App:
    """Simple class to be used as an entrypoint."""
    def __init__(self) -> None:
        pass

    def start(self) -> None:
        ga = GAMenu().configure_ga()
        ga.simulate()


if __name__ == '__main__':
    app = App()
    try:
        app.start()
    except EOFError:
        print('^D')
    except KeyboardInterrupt:
        print('^C')
