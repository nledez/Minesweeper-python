class Minesweeper():
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.grid = []
        x_array = []
        for x in range(size_x):
            x_array.append('.')

        for y in range(size_y):
            self.grid.append(x_array.copy())

    def add_mine(self, x, y):
        self.grid[y][x] = '*'

    def compute(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.grid[y][x] != '*':
                    self.grid[y][x] = self.compute_coord(x, y)

    def compute_coord(self, x, y):
        flat_grid = []
        x_min = x - 1
        x_max = x + 2
        if x_min < 0:
            x_min = 0
        if x_max > self.size_x:
            x_max = self.size_x

        if y >= 1:
            flat_grid.extend(self.grid[y-1][x_min:x_max])
        flat_grid.extend(self.grid[y][x_min:x_max])
        if y < self.size_y - 1:
            flat_grid.extend(self.grid[y+1][x_min:x_max])
        return flat_grid.count('*')