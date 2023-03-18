# ahester57

import random
import time

from evolution_program.ga import GA
from evolution_program.selection_mechanism.mechanism import SelectionMechanism
from evolution_program.selection_mechanism.proportional import Proportional
from evolution_program.selection_mechanism.ranking import LinearRanking
from evolution_program.selection_mechanism.tournament import DeterministicTournament, StochasticTournament
from evolution_program.selection_mechanism.truncation import Truncation


class GAMenu(object):

    def __init__(self) -> None:
        """Concept loosely based on: https://chunkofcode.net/how-to-implement-a-dynamic-command-line-menu-in-python/"""
        pass

    def selection_mechanism_menu(self) -> SelectionMechanism:
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

    def input_display(self, name:str, default=None) -> str:
        """Generate the string to be displayed in an prompt.

        Args:
            name (str): The prompt name.
            default (str, optional): The default value if no answer provided.

        Returns:
            str: The string to be used in an input prompt.
        """
        if default is not None:
            return f'''=================================
{name} [{default}]: '''
        else:
            return f'''=================================
{name}: '''

    def prompt_int(self, name:str, default:int=None) -> int:
        """Prompt for an integer value.
        
        Args:
            name (str): The prompt name.
            default (int, optional): The default value if no answer provided.

        Returns:
            int: The user-provided input.
        """
        assert default is None or type(default) is int
        ans = ''
        while len(ans) == 0:
            ans = input(self.input_display(name, default))
            if ans == '' and default is not None:
                return default
            try:
                return int(ans)
            except ValueError:
                ans = ''

    def prompt_float(self, name:str, default:float=None) -> float:
        """Prompt for a float value.
        
        Args:
            name (str): The prompt name.
            default (float, optional): The default value if no answer provided.

        Returns:
            float: The user-provided input.
        """
        assert default is None or type(default) is float
        ans = ''
        while len(ans) == 0:
            ans = input(self.input_display(name, default))
            if ans == '' and default is not None:
                return default
            try:
                return float(ans)
            except ValueError:
                ans = ''

    def prompt_bool(self, name:str, default:bool=None) -> bool:
        """Prompt for a bool value.
        
        Args:
            name (str): The prompt name.
            default (bool, optional): The default value if no answer provided.

        Returns:
            bool: The user-provided input.
        """
        assert default is None or type(default) is bool
        ans = ''
        while len(ans) == 0 or ans[0] not in 'YyNn':
            default_display = 'Y/n'
            if not default:
                default_display = 'y/N'
            ans = input(self.input_display(name, default_display))
            if ans == '' and default is not None:
                return default
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
                    domain_lower=self.prompt_float('Domain Lower Bound', -65.536),
                    domain_upper=self.prompt_float('Domain Upper Bound', 65.536),
                    pop_size=self.prompt_int('Population Size', 30),
                    rand_seed=self.prompt_int('Random Seed', random.randint(1, 123456789)),
                    maximize=self.prompt_bool('Maximize', False),
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
