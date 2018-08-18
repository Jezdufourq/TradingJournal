from tkinter import *
import tkinter.ttk as ttk
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


def click_add():
    pass


def close():
    selected_row = tree.focus()
    print(tree.item(selected_row))

    dialog = Toplevel(root)
    dialog.title("close")

    price_label = Label(dialog, text="Price")
    price_label.grid(row=0, column=0)

    price_entry = Entry(dialog)
    price_entry.grid(row=0, column=1)

    buttons_frame = Frame(dialog)
    buttons_frame.grid(row=1, column=0, columnspan=2)

    ok_button = Button(buttons_frame, text="ok", command=close_ok)
    ok_button.pack(side=RIGHT)

    cancel_button = Button(buttons_frame, text="cancel", command=dialog.destroy)
    cancel_button.pack(side=RIGHT)


def close_ok():
    pass


root = Tk()
root.title("Dashboard")

#
# graph canvas
#
f = Figure(figsize=(6, 2), dpi=100)
a = f.add_subplot(111)
a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 3, 6, 5, 2, 1, 4, 1])

graph_canvas = FigureCanvasTkAgg(f, root)
graph_canvas.draw()
graph_canvas.get_tk_widget().grid(row=0, column=0)

#
# "values" frame & label
#
values_frame = Frame(root, borderwidth=1)
values_frame.config(highlightbackground="black")
values_frame.grid(row=0, column=1, sticky=N, pady=(60, 0), padx=(0, 50))

portfolio_exposure = Label(values_frame, text="Portfolio Exposure: ")
avg_rrr = Label(values_frame, text="Avg. RRR: ")
num_trades = Label(values_frame, text="No. of Trades: ")
win_rate = Label(values_frame, text="Win Rate: ")
avg_holding_time = Label(values_frame, text="Avg. Holding Time: ")

portfolio_exposure.grid(row=0, column=0, sticky=W)
avg_rrr.grid(row=1, column=0, sticky=W)
num_trades.grid(row=2, column=0, sticky=W)
win_rate.grid(row=3, column=0, sticky=W)
avg_holding_time.grid(row=4, column=0, sticky=W)

exposure_value = Label(values_frame, text=0)
rrr_value = Label(values_frame, text=0)
trades_value = Label(values_frame, text=0)
win_rate_value = Label(values_frame, text=0)
aht_value = Label(values_frame, text=0)

exposure_value.grid(row=0, column=1)
rrr_value.grid(row=1, column=1)
trades_value.grid(row=2, column=1)
aht_value.grid(row=4, column=1)

# delete button
delete=Button(values_frame,text="Exit")
delete.grid(row=20,column=0,columnspan=2,pady=20,ipadx=20)

#
# Table of values
#

table_frame = Frame(root)
table_frame.grid(row=1, column=0, columnspan=2, sticky=W+E)

tree = ttk.Treeview(table_frame)
tree["columns"] = (1, 2, 3, 4, 5, 6, 7, 8)
tree["show"] = "headings"
headings = ["Date", "Ticker", "Mkt Value", "Entry Price", "Current Price", "P/L ($)", "P/L (%)", "Live Risk"]

# index start from 1
column_index = 1

for heading in headings:
    tree.column(column_index, width=95)
    tree.heading(column_index, text=heading)
    column_index += 1

tree.insert("", "end", values=("2017/5/1", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/2", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/3", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/4", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/5", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/6", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/7", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/8", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/9", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/0", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/1", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/2", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/3", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/4", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/5", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/6", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/7", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))
tree.insert("", "end", values=("2017/5/8", "食費", 3500, "食費", 3500, "食費", 3500, "食費"))

tree.pack(side=LEFT)

button_frame = Frame(root)
button_frame.grid(row=2, column=1)

close_button = Button(button_frame, text="Close", padx=10, pady=5, command=close)
close_button.pack(side=LEFT)

add_button = Button(button_frame, text="Add", padx=10, pady=5, command=click_add)
add_button.pack(side=LEFT)


while True:
    try:
        root.mainloop()
        break
    except UnicodeDecodeError:
        pass

