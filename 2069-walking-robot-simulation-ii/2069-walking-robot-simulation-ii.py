class Robot:

    def __init__(self, width: int, height: int):
        self.robot = [[0] * width for _ in range(height)]
        self.dir = ["East", "North", "West", "South"]
        self.direction = [(1,0), (0,1), (-1,0), (0,-1)] 
        self.perimeter = 2 * (width + height - 2)
        self.x, self.y = 0,0
        self.obstacle = [(width, 0), (width-1, height), (-1, height-1), (0, -1)]
        self.flag = False
        self.current = 0
        
    def step(self, num: int) -> None:
        self.flag = True
        num %= self.perimeter
        change_x, change_y = self.direction[self.current]
        for _ in range(num):
            if (self.x + change_x, self.y + change_y) in self.obstacle:
                self.current = (self.current + 1) % 4
            change_x, change_y = self.direction[self.current]
            self.x += change_x
            self.y += change_y

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        if self.flag and [self.x, self.y] == [0,0]:
            self.current = 3
        return self.dir[self.current]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()