# ahester57

import random
import time

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

    def selection_mechanism_menu(self) -> type:
        print('''
=================================
Selection Mechanisms
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
        """Prompt for an integer value."""
        ans = ''
        while len(ans) == 0:
            ans = input(f'''=================================
{name} [{default}]: ''')
            if ans == '' and default is not None:
                return default
            try:
                return int(ans)
            except ValueError:
                ans = ''

    def prompt_float(self, name, default) -> float:
        """Prompt for an integer value."""
        ans = ''
        while len(ans) == 0:
            ans = input(f'''=================================
{name} [{default}]: ''')
            if ans == '' and default is not None:
                return default
            try:
                return float(ans)
            except ValueError:
                ans = ''

    def prompt_bool(self, name, default) -> bool:
        ans = ''
        while len(ans) == 0 or ans[0] not in 'YyNn':
            ans = input(f'''=================================
{name}? [{default}]: ''')
            if ans == '' and default is not None:
                ans = 'Y'
        return ans[0].upper() == 'Y'

    def configure_ga(self) -> GA:
        while True:
            try:
                random.seed(time.time())
                Select_Mechanism = self.selection_mechanism_menu()
                selection_parameters = {}
                for k, v in Select_Mechanism.parameters().items():
                    selection_parameters.update({k: self.prompt_float(v[0], v[1])})
                return GA(
                    dims=self.prompt_int('Dimensions', 2),
                    domain_lower=self.prompt_float('Domain Lower Bound', -7.0),
                    domain_upper=self.prompt_float('Domain Upper Bound', 4.0),
                    pop_size=self.prompt_int('Population Size', 30),
                    rand_seed=self.prompt_int('Random Seed', random.randint(1, 123456789)),
                    maximize=self.prompt_bool('Maximize', 'Y'),
                    Select_Mechanism=Select_Mechanism,
                    selection_parameters=selection_parameters
                )
            except Exception as e:
                print(f'Exception {e.args} occurred in {self.__class__}.enter_menu')


if __name__ == '__main__':
    try:
        ga = GAMenu().configure_ga()
        ga.simulate()
    except EOFError:
        print('^D')
    except KeyboardInterrupt:
        print('^C')
