
from evolution_program.ga import GA
from evolution_program.selection_mechanism.proportional import Proportional
from evolution_program.selection_mechanism.ranking import LinearRanking
from evolution_program.selection_mechanism.tournament import DeterministicTournament
from evolution_program.selection_mechanism.tournament import StochasticTournament
from evolution_program.selection_mechanism.truncation import Truncation



class GAMenu(object):

    def __init__(self) -> None:
        """Concept loosely based on: https://chunkofcode.net/how-to-implement-a-dynamic-command-line-menu-in-python/"""
        pass

    def print_selection_mechanism_menu(self) -> type:
        print('''
=================================
Selection Mechanism
=================================
    1 - Proportional
    2 - Truncation
    3 - Tournament (Deterministic)
    4 - Tournament (Stochastic)
    5 - Linear Ranking
=================================
''')
        ans = -1
        while ans not in range(1, 6):
            ans = self.prompt_int('Which mechanism?', None)
        return [
            None,
            Proportional,
            Truncation,
            DeterministicTournament,
            StochasticTournament,
            LinearRanking
        ][ans]

    def prompt_int(self, name, default) -> int:
        """Prompt for an integer value.
        """
        ans = ''
        while len(ans) == 0:
            ans = input(f'{name} [{default}]: ')
            if ans == '' and default is not None:
                return default
            try:
                return int(ans)
            except ValueError:
                ans = ''

    def prompt_bool(self, name, default) -> bool:
        ans = ''
        while len(ans) == 0 or ans[0] not in 'YyNn':
            ans = input(f'{name}? [{default}]: ')
            if ans == '' and default is not None:
                ans = 'Y'
        return ans[0].upper() == 'Y'

    def configure_ga(self) -> GA:
        while True:
            try:
                return GA(
                    dims=self.prompt_int('Dimensions', 2),
                    domain_lower=-7.0,
                    domain_upper=4.0,
                    pop_size=self.prompt_int('Population Size', 30),
                    maximize=self.prompt_bool('Maximize', 'Y'),
                    selection_mechanism=self.print_selection_mechanism_menu()
                )
            except Exception as e:
                print(f'Exception {e.args} occurred in {self.__class__}.enter_menu')
