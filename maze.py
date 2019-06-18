class maze:
    def __init__(self):
        self.paths = []
    
    def add_path(self,x1,y1,x2,y2):
        self.paths.append([x1,y1,x2,y2])

    def get_paths(self):
        return self.paths
    
    def get_range(self):
        min_x, max_x, min_y, max_y = [None, None, None, None]
        for path in self.get_paths():
            if not min_x or path[0] < min_x:
                min_x = path[0]
            if not min_y or path[1] < min_y:
                min_y = path[1]
            if not max_x or path[2] > max_x:
                max_x = path[2]
            if not max_y or path[3] > max_y:
                max_y = path[3]
        return [min_x, max_x+1, min_y, max_y+1]
        
    def make_grid(self):
        range_size = self.get_range()
        num_rows = range_size[3]
        num_cols = range_size[1]
        empty_row = "." * num_cols
        self.grid = [empty_row] * num_rows
        for path in self.get_paths():
            line_info = self.get_path_start_and_dir(path)
            print("LINE_INFO:{}".format(line_info))
            self.update_grid_with_line(line_info)

    def update_grid_with_line(self, line_info):
        xy, dirn, length = line_info
        print("{},{}".format(xy[0],xy[1]))
        self.set_grid_point(xy[0], xy[1])
        for num in range(length):
            if dirn == "x":
                xy[0] += 1
            else:
                xy[1] += 1
            self.set_grid_point(xy[0], xy[1])
        
    def get_path_start_and_dir(self, path):
        if path[0] == path[2]:
            direction = "y"
        elif path[1] == path[3]:
            direction = "x"
        else:
            raise Exception("path is not perpendicular:{}".format(path))
        if direction == "y":
            other = path[0]
            if path[1] < path[3]:
                start = path[1]
            else:
                start = path[3]
            length = int(math.fabs(path[1] - path[3]))
            return [[other, start], direction, length]
        else:
            other = path[1]
            if path[0] < path[2]:
                start = path[0]
            else:
                start = path[2]
            length = int(math.fabs(path[0] - path[2]))
            return [[start, other], direction, length]
        
    def set_grid_point(self,x,y,symbol="*"):
        if y >= len(self.grid):
            print("cannot find y={} in {}".format(y, self.grid))
            return
        row = self.grid[y]
        row = row[:x-1] + symbol + row [x:]
        self.grid[y] = row

my_maze = maze()
my_maze.add_path(1,1,4,1)
my_maze.add_path(4,1,4,3)

print("{}".format(my_maze.get_paths()))
print("{}".format(my_maze.get_range()))
my_maze.make_grid()
# my_maze.set_grid_point(1,2,"=")
# my_maze.set_grid_point(2,2,"B")
# my_maze.set_grid_point(3,2,"a")
# my_maze.set_grid_point(4,2,"z")
print("\n".join(my_maze.grid))
