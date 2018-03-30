import Scripts.screen as scrn
import Scripts.arena as arena
import Scripts.player as player


screen = scrn.Screen()

arena_size = int(input('Please enter the size of the play arena: '))
win_condition = int(input('Please enter the required sequence length to win: '))

play_arena = arena.Arena(arena_size, win_condition)
win = False

p1 = player.Player(input('Player 1 please enter your name: '), 1)
p2 = player.Player(input('Player 2 please enter your name: '), 2)

# p1 = player.Player('p1', 1)
# p2 = player.Player('p2', 2)

screen.update_arena(play_arena.get_table())
screen.render()

next_player = p1

while not win:
    print('Player ' + next_player.name + ' please enter your move:')

    try:
        mx = int(input('Column: ')) - 1
        my = int(input('Row: ')) - 1
    except ValueError:
        my = -1
        mx = -1

    while play_arena.put_sign(next_player.number, [my, mx]) == 0:
        try:
            mx = int(input('Column: ')) - 1
            my = int(input('Row: ')) - 1
        except ValueError:
            my = -1
            mx = -1

    screen.update_arena(play_arena.get_table())
    screen.render()

    win_check = play_arena.check_for_win()

    if win_check == 1:
        win = True
        print('Player ' + next_player.name + ' won the game!')
    elif win_check == 2:
        win = True
        print("DRAW!")

    if next_player is p1:
        next_player = p2
    else:
        next_player = p1

# screen.update_arena(play_arena.get_table())
# screen.render()

