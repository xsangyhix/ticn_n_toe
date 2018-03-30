class Arena(object):
    def __init__(self, size, win_condition):
        self.size = size
        self.fields = [[0 for i in range(size)] for i in range(size)]
        self.last_move = []
        self.win_condition = win_condition

    def get_table(self):
        return self.fields

    def put_sign(self, sign_type, position):

        check_all_checks = []

        try:
            check_empty_field = self.fields[position[0]][position[1]] == 0
            check_input_valid_value = sign_type in [1, 2]
            check_input_in_bounds = self.size > sign_type >= 0
            check_input_value_type = type(sign_type) is int

            check_all_checks.append(check_empty_field)
            check_all_checks.append(check_input_valid_value)
            check_all_checks.append(check_input_in_bounds)
            check_all_checks.append(check_input_value_type)
        except IndexError:
            check_all_checks.append(False)

        if not (False in check_all_checks):
            self.fields[position[0]][position[1]] = sign_type
            self.last_move = position
            return 1
        else:
            print("Invalid input")
            return 0

    def check_for_win(self):
        if len(self.last_move) == 0:
            print("No valid move has been played.")
            return 0
        last_input = self.fields[self.last_move[0]][self.last_move[1]]

        # check horizontally
        count = 1
        y = self.last_move[0]
        x = self.last_move[1] - 1
        while x >= 0 and self.fields[y][x] == last_input:
            count += 1
            x -= 1

        x = self.last_move[1] + 1
        while x < self.size and self.fields[y][x] == last_input:
            count += 1
            x += 1

        if count >= self.win_condition:
            return 1

        # check vertically
        count = 1
        y = self.last_move[0] - 1
        x = self.last_move[1]
        while y >= 0 and self.fields[y][x] == last_input:
            count += 1
            y -= 1

        y = self.last_move[0] + 1
        while y < self.size and self.fields[y][x] == last_input:
            count += 1
            y += 1

        if count >= self.win_condition:
            return 1

        # check the ascending diagonal
        count = 1
        y = self.last_move[0] + 1
        x = self.last_move[1] - 1
        while y < self.size and x >= 0 and self.fields[y][x] == last_input:
            count += 1
            y += 1
            x -= 1

        y = self.last_move[0] - 1
        x = self.last_move[1] + 1
        while y >= 0 and x < self.size and self.fields[y][x] == last_input:
            count += 1
            y -= 1
            x += 1

        if count >= self.win_condition:
            return 1

        # check the descending diagonal
        count = 1
        y = self.last_move[0] - 1
        x = self.last_move[1] - 1
        while y >= 0 and x >= 0 and self.fields[y][x] == last_input:
            count += 1
            y -= 1
            x -= 1

        y = self.last_move[0] + 1
        x = self.last_move[1] + 1
        while y < self.size and x < self.size and self.fields[y][x] == last_input:
            count += 1
            y += 1
            x += 1

        if count >= self.win_condition:
            return 1

        return 0
