from graphics import *

def draw_room(win, name, x1, y1, x2, y2, color):
    room = Rectangle(Point(x1, y1), Point(x2, y2))
    room.setFill(color)
    room.setOutline("black")
    room.setWidth(2)
    room.draw(win)

    label = Text(Point((x1 + x2) / 2, (y1 + y2) / 2), name)
    label.setSize(10)
    label.draw(win)

def draw_door_arc(win, direction, x, y, radius=20):
    arc = Oval(Point(x - radius, y - radius), Point(x + radius, y + radius))
    arc.setOutline("red")
    arc.setWidth(2)
    arc.setFill("white") 
    arc.draw(win)

def main():
    win = GraphWin("Floor Plan Layout", 800, 650)
    win.setBackground("white")

    # Draw Rooms
    draw_room(win, "Bedroom", 50, 50, 250, 300, "lightblue")
    draw_room(win, "Living Room", 250, 50, 750, 300, "lightgray")
    draw_room(win, "Bathroom", 50, 300, 300, 420, "beige")
    draw_room(win, "Dining", 300, 300, 500, 420, "lightgreen")
    draw_room(win, "Kitchen", 500, 300, 750, 420, "lightpink")

    # Draw Door Arcs
    draw_door_arc(win, "horizontal", 250, 170)  # Bedroom ↔ Living Room
    draw_door_arc(win, "vertical", 150, 300)    # Bedroom ↔ Bathroom
    draw_door_arc(win, "vertical", 400, 300)    # Living Room ↔ Dining
    draw_door_arc(win, "vertical", 620, 300)    # Living Room ↔ Kitchen
    draw_door_arc(win, "horizontal", 500, 360)  # Dining ↔ Kitchen


    win.getMouse()
    win.close()

main()