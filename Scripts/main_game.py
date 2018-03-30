import Scripts.screen as scrn
import Scripts.arena as arena


screen = scrn.Screen()
play_arena = arena.Arena(5, 3)

# screen.update_arena(play_arena.get_table())
# screen.render()

play_arena.put_sign(1, [1, 0])
play_arena.put_sign(1, [2, 0])
play_arena.put_sign(1, [1, 1])
play_arena.put_sign(1, [1, 2])

print(play_arena.check_for_win())

screen.update_arena(play_arena.get_table())
screen.render()
