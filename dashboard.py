from tkinter import *
import tkinter.ttk as ttk
import tkinter.simpledialog
import tkinter as tk
import matplotlib
from db.DAO import Datastore
from db.instruments import Asset,Instrument
from calculationHandler import entryCalculation, portfolioMetric
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from datetime import datetime

from mainWindow import Page, MainView




class DashboardGUI(Page):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.initPieChart()

        # Setup Frame for values
        self.values_frame = Frame(self, borderwidth=1)
        self.values_frame.config(highlightbackground="black")
        self.values_frame.grid(row=0, column=1, sticky=N, pady=(60, 0), padx=(0, 50))

        # Add GUI Elements to values frame.
        self.portfolio_exposure = Label(self.values_frame, text="Portfolio Exposure: ")
        self.avg_rrr = Label(self.values_frame, text="Avg. RRR: ")
        self.num_trades = Label(self.values_frame, text="No. of Trades: ")
        self.win_rate = Label(self.values_frame, text="Win Rate: ")
        self.avg_holding_time = Label(self.values_frame, text="Avg. Holding Time: ")

        # Setup Portfolio Grid
        self.portfolio_exposure.grid(row=0, column=0, sticky=W)
        self.avg_rrr.grid(row=1, column=0, sticky=W)
        self.num_trades.grid(row=2, column=0, sticky=W)
        self.win_rate.grid(row=3, column=0, sticky=W)
        self.avg_holding_time.grid(row=4, column=0, sticky=W)

        self.exposure_value = Label(self.values_frame, text=0)
        self.rrr_value = Label(self.values_frame, text=0)
        self.trades_value = Label(self.values_frame, text=0)
        self.win_rate_value = Label(self.values_frame, text=0)
        self.aht_value = Label(self.values_frame, text=0)

        self.exposure_value.grid(row=0, column=1)
        self.rrr_value.grid(row=1, column=1)
        self.trades_value.grid(row=2, column=1)
        self.win_rate_value.grid(row=3, column=1)
        self.aht_value.grid(row=4, column=1)

        #Init Calculator
        self.calculator = entryCalculation()

        # "Exit" button
        # TODO: Confirm if this button is still necessary or not.
        # delete = Button(values_frame, text="Exit")
        # delete.grid(row=20, column=0, columnspan=2, pady=20, ipadx=20)

        """
            Table of values
        """
        self.table_frame = Frame(self)
        self.table_frame.grid(row=1, column=0, columnspan=2, sticky=W + E)

        self.tree = ttk.Treeview(self.table_frame)
        self.tree["columns"] = (1, 2, 3, 4, 5, 6, 7, 8)
        self.tree["show"] = "headings"
        self.headings = ["Date", "Ticker", "Mkt Value", "Entry Price", "Current Price", "P/L ($)", "P/L (%)", "Live Risk"]

        # index start from 1
        column_index = 1

        for heading in self.headings:
            self.tree.column(column_index, width=95)
            self.tree.heading(column_index, text=heading)
            column_index += 1

        # Updating the open position table
        populatetree = Datastore.instance
        list = populatetree.getOpenAssets()

        for data in list:
            inst = Datastore.instance.getInstrument(data['instrumentCode'])
            # Calculating the parameters
            mktValue = self.calculator.calcMarketval(data['entryPrice'], data['qty'])
            plVal = self.calculator.livePLval(data['entryPrice'], inst.currentPrice)
            plPercent = self.calculator.livePLpercent(data['entryPrice'], inst.currentPrice)

            ts = int(data['entryDate'])
            self.tree.insert("", "end", values=(
                datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M'), data['instrumentCode'], mktValue,
                data['entryPrice'],
                inst.currentPrice, plVal, plPercent))

        self.tree.pack(side=LEFT)
        self.button_frame = Frame(self)
        self.button_frame.grid(row=2, column=1)
        self.close_button = Button(self.button_frame, text="Exit", padx=10, pady=5, command=self.close)
        self.close_button.pack(side=LEFT)

        self.add_button = Button(self.button_frame, text="Add", padx=10, pady=5, command=self.click_add)
        self.add_button.pack(side=LEFT)


    def initPieChart(self):
            """
                graph canvas
                refer:
                1. https://www.youtube.com/watch?v=JQ7QP5rPvjU
                2. https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/

            """
            self.f = Figure(figsize=(6, 2), dpi=100)
            self.a = self.f.add_subplot(111)

            labels, sizes = self.get_asset_distribution()

            self.a.pie(sizes, labels=labels)
            self.a.axis('equal')

            self.graph_canvas = FigureCanvasTkAgg(self.f, self)
            self.graph_canvas.draw()
            self.graph_canvas.get_tk_widget().grid(row=0, column=0)

    def get_asset_distribution(self):
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
        return labels, sizes

    def click_add(self):
        """
            Called when "add" button is clicked.
            Opens a new window from frontend_script.py
        """
        # TODO: 1. In frontend_script.py, create function "create_window()" that takes a Toplevel() as a parameter.
        # TODO: 2. In this file, implement the code below

        self.lift()


    def close(self):
        """
            Called when "close" button is clicked.
            Shows a dialog where user can input a price and push either "cancel" or "ok"
            When price is entered and "ok" is clicked, the selected row will be deleted.
        """
        # Retrieve data from selected row
        selected_row = self.tree.focus()
        print(self.tree.item(selected_row))

        # prompt dialog
        price = tkinter.simpledialog.askinteger("Close", "Price", parent=self)

        # retrieve input from dialog
        if price is not None:  # when "ok" is clicked
            print(price)
            # delete selected row
            self.tree.delete(selected_row)
        else:  # when "cancel" is clicked
            print("cancelled")





# Initilizing the classes



#


#root = Tk()
#root.title("Dashboard")



# while True:
#     try:
#         root.mainloop()
#         break
#     except UnicodeDecodeError:
#         pass
