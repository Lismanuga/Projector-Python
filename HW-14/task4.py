class Robot:
    def __init__(self):
        self.orientation = "Up"
        self.position_x = 0
        self.position_y = 0

    def move(self, step):
        if self.orientation == "Up":
            self.position_y += step
        elif self.orientation == "Down":
            self.position_y -= step
        elif self.orientation == "Left":
            self.position_x -= step
        elif self.orientation == "Right":
            self.position_x += step

    def turn(self, direction):
        if direction not in ["Left", "Right"]:
            raise ValueError("Invalid direction. Must be 'Left' or 'Right'.")

        if self.orientation == "Up":
            self.orientation = "Left" if direction == "Left" else "Right"
        elif self.orientation == "Down":
            self.orientation = "Right" if direction == "Left" else "Left"
        elif self.orientation == "Left":
            self.orientation = "Down" if direction == "Left" else "Up"
        elif self.orientation == "Right":
            self.orientation = "Up" if direction == "Left" else "Down"

    def display_position(self):
        print(f"Position: ({self.position_x}, {self.position_y}), Orientation: {self.orientation}")


my_robot = Robot()
my_robot.display_position()
my_robot.turn("Right")
my_robot.move(5)
my_robot.turn("Left")
my_robot.move(3)
my_robot.turn("Left")
my_robot.display_position()
