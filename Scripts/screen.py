class Screen(object):
    def __init__(self,):
        self.table_play_arena = []

    def render(self):
        for i in self.table_play_arena:
            print(i)

    def update_arena(self, arena):
        self.table_play_arena = arena
