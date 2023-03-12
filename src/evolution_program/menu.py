import sys

from evolution_program.ga import GA


class GAMenu(object):

    def __init__(self) -> None:
        """Concept loosely based on: https://chunkofcode.net/how-to-implement-a-dynamic-command-line-menu-in-python/"""
        pass

    def do_0(self) -> None:
        """Quit

        Raises:
            SystemExit: always
        """
        sys.exit(0)

    def do_1(self) -> int:
        """Login
        """
        print('''
---------------
Logging in...
---------------
''')
        print('''
=================================
Login Menu (name | uuid)
=================================''')
        for i, m in enumerate(self.library_service.get_library_members()):
            print(f'    {i + 1} - {m.get_name()} | {m.get_uuid()}')
        print('''
    0 - Quit
=================================

Make a choice.
''')
        return 1

    def do_2(self) -> int:
        """Look at books
        """
        print('''
---------------
Looking at Books.
---------------
''')
        print('''
=================================
Book Menu (title | author | year)
=================================''')
        for i, b in enumerate(self.library_service.get_library_books()):
            print(f'    {i + 1} - {b.get_title()} | {b.get_author()} | {b.get_year_of_publication()}')
        print('''
    0 - Quit
=================================

Make a choice.
''')
        return 2

    def do_3(self) -> int:
        """Look at journals
        """
        print('''
---------------
Looking at Journals.
---------------
''')
        print('''
=================================
Journal Menu (title | author | year)
=================================''')
        for i, j in enumerate(self.library_service.get_library_journals()):
            print(f'    {i + 1} - {j.get_title()} | {j.get_author()} | {j.get_year_of_publication()}')
        print('''
    0 - Quit
=================================

Make a choice.
''')
        return 3


    def do_a_thing(self, thing: int) -> int:
        do_name = f'do_{thing}'
        try:
            do_func = self.__getattribute__(do_name)
        except AttributeError:
            do_func = lambda x = thing : x
        return do_func()

    def print_library_menu(self) -> None:
        print('''
=================================
Library Menu
=================================
    1 - Login
    2 - Look at Books
    3 - Look at Journals
    4 - Make a Return
    0 - Quit
=================================

Make a choice.
''')
        
    def prompt_maximize(self) -> bool:
        ans = ''
        while len(ans) == 0 or ans[0] not in 'YyNn':
            ans = input("Maximize [Y/n]: ")
            if ans == '':
                ans = 'Y'
        return ans[0].upper() == 'Y'

    def configure_ga(self) -> GA:
        while True:
            try:
                l = GA(
                    dims=2,
                    domain_lower=-7.0,
                    domain_upper=4.0,
                    pop_size=30,
                    maximize=self.prompt_maximize()
                )
                return l
            except Exception as e:
                print(f'Exception {e.args} occurred in {self.__class__}.enter_menu')
