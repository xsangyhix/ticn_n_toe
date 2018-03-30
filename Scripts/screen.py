class Screen(object):
    def __init__(self,):
        self.table_play_arena = []

    def render(self):
        print('\n\n\n')
        for i in self.table_play_arena:
            line = '| '
            for item in i:
                if item == 0:
                    line += ' - '
                elif item == 1:
                    line += ' X '
                elif item == 2:
                    line += ' O '
            line += ' |'
            print(line)
        print('\n')

    def update_arena(self, arena):
        self.table_play_arena = arena
