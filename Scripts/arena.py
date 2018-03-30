class Arena(object):
    def __init__(self, size):
        self.size = size
        self.fields = [[0 for i in range(size)] for i in range(size)]

    def get_table(self):
        return self.fields

    def put_sign(self, sign_type, position):
        check_empty_field = self.fields[position[0]][position[1]] == 0
        check_valid_input_value = sign_type in [1, 2]
        check_input_in_bounds = self.size > sign_type >= 0

        if self.fields[position[0]][position[1]] == 0 and (sign_type == 1 or sign_type == 2) and position[0] < self.size and position[1] < self.size:
            self.fields[position[0]][position[1]] = sign_type
            return 1
        else:
            print("Invalid input")
            return 0
