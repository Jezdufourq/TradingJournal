from tkinter import *
import tkinter.ttk as ttk
import tkinter.simpledialog
import matplotlib
import frontend_script
from db.DAO import Datastore

from db.instruments import Asset,Instrument
from calculationHandler import entryCalculation, portfolioMetric

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from datetime import datetime


# Initilizing the classes
calculator = entryCalculation()

def click_add():
    """
        Called when "add" button is clicked.
        Opens a new window from frontend_script.py
    """
    # TODO: 1. In frontend_script.py, create function "create_window()" that takes a Toplevel() as a parameter.
    # TODO: 2. In this file, implement the code below
    # new_window = Toplevel(root)
    # frontend_script.create_window(new_window)


def close():
    """
        Called when "close" button is clicked.
        Shows a dialog where user can input a price and push either "cancel" or "ok"
        When price is entered and "ok" is clicked, the selected row will be deleted.
    """
    # Retrieve data from selected row
    selected_row = tree.focus()
    print(tree.item(selected_row))

    # prompt dialog
    price = tkinter.simpledialog.askinteger("Close", "Price", parent=root)

    # retrieve input from dialog
    if price is not None:  # when "ok" is clicked
        print(price)
        # delete selected row
        tree.delete(selected_row)
    else:  # when "cancel" is clicked
        print("cancelled")

def get_asset_distribution():
    db = Datastore.instance
    open_assets = db.getOpenAssets()

    labels = []
    sizes = []

    for asset in open_assets:
        code = asset['instrumentCode']
        instrument = db.getInstrument(code)
        
        found = False

        for i in range(len(labels)):
            if labels[i] == instrument.type:
                found = True
                sizes[i] = sizes[i] + 1

        if not found:
            labels.append(instrument.type)
            sizes.append(1)

    return (labels, sizes)

root = Tk()
root.title("Dashboard")

"""
    graph canvas
    refer: 
    1. https://www.youtube.com/watch?v=JQ7QP5rPvjU
    2. https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/
    
"""
f = Figure(figsize=(6, 2), dpi=100)
a = f.add_subplot(111)
#a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 3, 6, 5, 2, 1, 4, 1])

labels, sizes = get_asset_distribution()

a.pie(sizes, labels = labels)
a.axis('equal')

graph_canvas = FigureCanvasTkAgg(f, root)
graph_canvas.draw()
graph_canvas.get_tk_widget().grid(row=0, column=0)

"""
    "values" frame & label
"""
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
win_rate_value.grid(row=3, column=1)
aht_value.grid(row=4, column=1)

"""
    Calculating the portfolio
"""
portfolio = Datastore.instance
list = portfolio.getClosedAssets()

short = 0
long = 0

for data in list:
    if (data['stopLoss']> data['entryPrice']):
    # This is a short position
        short += 1
    elif(data['stopLoss']< data['entryPrice']):
        # This is a long position
        long += 1
    else:
        pass

portfolioExp = long - short
portfolio_exposure['text'] = portfolioExp
short = 0
long = 0




"""
    Table of values
"""
table_frame = Frame(root)
table_frame.grid(row=1, column=0, columnspan=2, sticky=W + E)

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

# Updating the open position table
populatetree = Datastore.instance
list = populatetree.getOpenAssets()

for data in list:
    if (data['qty'] is None):
        pass
    else:
        inst = Datastore.instance.getInstrument(data['instrumentCode'])
        # Calculating the parameters
        mktValue = calculator.calcMarketval(data['entryPrice'], data['qty'])
        plVal = calculator.livePLval(data['entryPrice'], inst.currentPrice)
        plPercent = calculator.livePLpercent(data['entryPrice'], inst.currentPrice)

        ts = int(data['entryDate'])
        tree.insert("","end",values=(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M'),data['instrumentCode'], mktValue, data['entryPrice'],
                                     inst.currentPrice,plVal, plPercent))

tree.pack(side=LEFT)
button_frame = Frame(root)
button_frame.grid(row=2, column=1)
close_button = Button(button_frame, text="Exit", padx=10, pady=5, command=close)
close_button.pack(side=LEFT)

add_button = Button(button_frame, text="Add", padx=10, pady=5, command=click_add)
add_button.pack(side=LEFT)

# while True:
#     try:
#         root.mainloop()
#         break
#     except UnicodeDecodeError:
#         pass
