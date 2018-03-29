import Scripts.screen as scrn
import Scripts.arena as arena


screen = scrn.Screen()
play_arena = arena.Arena(6)

# screen.update_arena(play_arena.get_table())
# screen.render()

play_arena.put_sign(1, [1, 0])

screen.update_arena(play_arena.get_table())
screen.render()
