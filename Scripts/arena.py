class Arena(object):
    def __init__(self, size):
        self.fields = [[0 for i in range(size)] for i in range(size)]

    def get_table(self):
        return self.fields

    def put_sign(self, sign_type, position):
        if self.fields[position[0]][position[1]] == 0 and (sign_type == 1 or sign_type == 2):
            self.fields[position[0]][position[1]] = sign_type
            return 1
        else:
            print("Invalid input")
            return 0
