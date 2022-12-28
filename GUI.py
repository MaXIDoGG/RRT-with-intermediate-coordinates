from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import messagebox as mbox
from algo import main

root = Tk()
root.title("RRT")
root.geometry("1000x800")
width = 600
height = 600

canvas = Canvas(bg="white", width=width, height=height)  # график
canvas.pack(side=LEFT, anchor=CENTER, expand=1)


# BUTTONS
frame_buttons = Frame(root, relief=RAISED, borderwidth=1, background="#FFF")
frame_buttons.pack(side=RIGHT, fill=BOTH, expand=True)

# saveButton = Button(frame_buttons, text="Сохранить")
# saveButton.pack(side=TOP, padx=5, pady=5)

start = []


def getStart():
    start.append(float(startX.get()))
    start.append(float(startY.get()))
    x1, y1 = (start[0] - 3), (start[1] - 3)
    x2, y2 = (start[0] + 3), (start[1] + 3)
    canvas.create_oval(x1+300, height-y1-300, x2+300,
                       height-y2-300, fill="#ff0000")
    btnStart["state"] = "disabled"


frame_start = Frame(frame_buttons, relief=RAISED,
                    borderwidth=1, background="#FFF")
frame_start.pack(side=TOP, fill=BOTH, ipadx=5, ipady=5, padx=5, pady=5)

labelStartX = ttk.Label(frame_start, text="X:", font=("Arial", 10), width=3)
labelStartX.pack(side=LEFT, padx=5, pady=5)
startX = ttk.Entry(frame_start, width=10)
startX.pack(side=LEFT, padx=5, pady=5)
labelStartY = ttk.Label(frame_start, text="Y:", font=("Arial", 10), width=3)
labelStartY.pack(side=LEFT, padx=5, pady=5)
startY = ttk.Entry(frame_start, width=10)
startY.pack(side=LEFT, padx=5, pady=5)
btnStart = ttk.Button(frame_start, text="Add Start", command=getStart)
btnStart.pack(side=LEFT, padx=5, pady=5)

end = []


def getEnd():
    end.append(float(endX.get()))
    end.append(float(endY.get()))
    x1, y1 = (end[0] - 3), (end[1] - 3)
    x2, y2 = (end[0] + 3), (end[1] + 3)
    canvas.create_oval(x1+300, height-y1-300, x2+300,
                       height-y2-300, fill="#0000ff")
    btnEnd["state"] = "disabled"


frame_end = Frame(frame_buttons, relief=RAISED,
                  borderwidth=1, background="#FFF")
frame_end.pack(side=TOP, fill=BOTH, ipadx=5, ipady=5, padx=5, pady=5)
labelEndX = ttk.Label(frame_end, text="X:", font=("Arial", 10), width=3)
labelEndX.pack(side=LEFT, padx=5, pady=5)
endX = ttk.Entry(frame_end, width=10)
endX.pack(side=LEFT, padx=5, pady=5)
labelEndY = ttk.Label(frame_end, text="Y:", font=("Arial", 10), width=3)
labelEndY.pack(side=LEFT, padx=5, pady=5)
endY = ttk.Entry(frame_end, width=10)
endY.pack(side=LEFT, padx=5, pady=5)
btnEnd = ttk.Button(frame_end, text="Add End", command=getEnd)
btnEnd.pack(side=LEFT, padx=5, pady=5)


inters = []


def getInter():
    x = float(interX.get())
    y = float(interY.get())
    x1, y1 = (x - 3), (y - 3)
    x2, y2 = (x + 3), (y + 3)
    inters.append([x, y])
    canvas.create_oval(x1+300, height-y1-300, x2+300,
                       height-y2-300, fill="#ffff00")


frame_inter = Frame(frame_buttons, relief=RAISED,
                    borderwidth=1, background="#FFF")
frame_inter.pack(side=TOP, fill=BOTH, ipadx=5, ipady=5, padx=5, pady=5)
labelInterX = ttk.Label(frame_inter, text="X:", font=("Arial", 10), width=3)
labelInterX.pack(side=LEFT, padx=5, pady=5)
interX = ttk.Entry(frame_inter, width=10)
interX.pack(side=LEFT, padx=5, pady=5)
labelInterY = ttk.Label(frame_inter, text="Y:", font=("Arial", 10), width=3)
labelInterY.pack(side=LEFT, padx=5, pady=5)
interY = ttk.Entry(frame_inter, width=10)
interY.pack(side=LEFT, padx=5, pady=5)
btnInter = ttk.Button(
    frame_inter, text="Add intermediate coord", command=getInter)
btnInter.pack(side=LEFT, padx=5, pady=5)


triangles = []


def getTriangle():
    x1 = float(triangle1X.get())
    y1 = float(triangle1Y.get())
    x2 = float(triangle2X.get())
    y2 = float(triangle2Y.get())
    x3 = float(triangle3X.get())
    y3 = float(triangle3Y.get())
    triangles.append(([x1, y1], [x2, y2], [x3, y3]))
    canvas.create_polygon(x1+300, 300-y1, x2+300, 300-y2,
                          x3+300, 300-y3, fill="#80CBC4", outline="#004D40")


frame_triangles = Frame(frame_buttons, relief=RAISED,
                        borderwidth=1, background="#FFF")
frame_triangles.pack(side=TOP, fill=BOTH, ipadx=5, ipady=5, padx=5, pady=5)


labelTriangle1X = ttk.Label(
    frame_triangles, text="X1:", font=("Arial", 10), width=3)
labelTriangle1X.pack(side=TOP, padx=5, pady=5)
triangle1X = ttk.Entry(frame_triangles, width=10)
triangle1X.pack(side=TOP, padx=5, pady=5)
labelTriangle1Y = ttk.Label(frame_triangles, text="Y1:",
                            font=("Arial", 10), width=3)
labelTriangle1Y.pack(side=TOP, padx=5, pady=5)
triangle1Y = ttk.Entry(frame_triangles, width=10)
triangle1Y.pack(side=TOP, padx=5, pady=5)

labelTriangle2X = ttk.Label(
    frame_triangles, text="X2:", font=("Arial", 10), width=3)
labelTriangle2X.pack(side=TOP, padx=5, pady=5)
triangle2X = ttk.Entry(frame_triangles, width=10)
triangle2X.pack(side=TOP, padx=5, pady=5)
labelTriangle2Y = ttk.Label(frame_triangles, text="Y2:",
                            font=("Arial", 10), width=3)
labelTriangle2Y.pack(side=TOP, padx=5, pady=5)
triangle2Y = ttk.Entry(frame_triangles, width=10)
triangle2Y.pack(side=TOP, padx=5, pady=5)

labelTriangle3X = ttk.Label(
    frame_triangles, text="X3:", font=("Arial", 10), width=3)
labelTriangle3X.pack(side=TOP, padx=5, pady=5)
triangle3X = ttk.Entry(frame_triangles, width=10)
triangle3X.pack(side=TOP, padx=5, pady=5)
labelTriangle3Y = ttk.Label(frame_triangles, text="Y3:",
                            font=("Arial", 10), width=3)
labelTriangle3Y.pack(side=TOP, padx=5, pady=5)
triangle3Y = ttk.Entry(frame_triangles, width=10)
triangle3Y.pack(side=TOP, padx=5, pady=5)


def build():
    rrt = main(start, end, inters, [-300, 300], triangles)

    for node in rrt.nodeList:
        if node.parent is not None:
            canvas.create_line(
                node.x+300, 300-node.y, rrt.nodeList[node.parent].x+300, 300-rrt.nodeList[node.parent].y, fill="#000")

    if rrt.path != 'Error':
        points = [(rrt.nodeList[data].x+300, 300-rrt.nodeList[data].y)
                  for data in rrt.path]
        canvas.create_line(points, fill="#ff0000", width=2)
    else:
        print(1)
        mbox.showwarning("Ошибка", "Не удалось найти путь")


btnTriangle = ttk.Button(
    frame_triangles, text="Add Triangle", command=getTriangle)
btnTriangle.pack(side=TOP, padx=5, pady=5)

btnBuild = ttk.Button(frame_buttons, text="Build path", command=build)
btnBuild.pack(side=TOP, padx=5, pady=5)


def clear():
    canvas.delete("all")
    start.clear()
    end.clear()
    inters.clear()
    triangles.clear()
    btnStart["state"] = "normal"
    btnEnd["state"] = "normal"


btnClear = ttk.Button(frame_buttons, text="Clear all", command=clear)
btnClear.pack(side=TOP, padx=5, pady=5)


root.mainloop()
