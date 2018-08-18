from tkinter import *
import tkinter.ttk as ttk
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


root = Tk()

#
# graph canvas
#
f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)
a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 3, 6, 5, 2, 1, 4, 1])

graph_canvas = FigureCanvasTkAgg(f, root)
graph_canvas.draw()
graph_canvas.get_tk_widget().grid(row=0, column=0)

#
# "current - " frame & label
#
current_frame = Frame(root, bd=1, bg="black")
current_frame.grid(row=0, column=1, sticky=N, pady=(60, 0), padx=(0, 50))

current_exposure = Label(current_frame, text="Current Exposure: ")
current_portfolio_value = Label(current_frame, text="Current Portfolio Value: ")
current_risk = Label(current_frame, text="Current Risk: ")

current_exposure.grid(row=0, column=0, sticky=W+E)
current_portfolio_value.grid(row=1, column=0, sticky=W+E)
current_risk.grid(row=2, column=0, sticky=W+E)

exposure_value = Label(current_frame, text=0)
portfolio_value = Label(current_frame, text=0)
risk_value = Label(current_frame, text=0)

exposure_value.grid(row=0, column=1)
portfolio_value.grid(row=1, column=1)
risk_value.grid(row=2, column=1)


#
# Table of values
#
tree = ttk.Treeview(root)

tree["columns"] = (1,2,3,4,5,6,7)
tree["show"] = "headings"

tree.column(1, width=30)
tree.column(2, width=30)
tree.column(3, width=30)
tree.column(4, width=30)
tree.column(5, width=30)
tree.column(6, width=30)
tree.column(7, width=30)

tree.heading(1, text="blah")
tree.heading(2, text="bleh")
tree.heading(3, text="meh")
tree.heading(4, text="blah")
tree.heading(5, text="bleh")
tree.heading(6, text="meh")
tree.heading(7, text="blah")

tree.grid(row=1, column=0, columnspan=2, sticky=W+E)

#
# mainloop
#
while True:
    try:
        root.mainloop()
        break
    except UnicodeDecodeError:
        pass
