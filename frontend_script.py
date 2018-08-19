import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import tkinter.simpledialog
from calculationHandler import entryCalculation
from db.DAO import Datastore
from db.instruments import Asset,Instrument

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import time
from datetime import datetime

class Page(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

    def show(self):
        self.lift()


class AddAssetGUI(Page):
    def __init__(self, parent):
        Page.__init__(self, parent)
        # init calculator
        self.calculator = entryCalculation()

        # asset frame
        self.asset_frame = LabelFrame(self, text="Instruments:")
        self.asset_frame.grid(row=0, column=0, columnspan=4, rowspan=9, padx=5, pady=10)

        self.tree = ttk.Treeview(self.asset_frame)
        self.tree["columns"] = (1, 2, 3, 4)
        self.tree["show"] = "headings"
        self.headings = ["Instrument", "Bid", "Spread", "ASK"]

        column_index=1

        for heading in self.headings:
            self.tree.column(column_index,width=95)
            self.tree.heading(column_index,text=heading)
            column_index+=1

        # populateTree=Datastore.instance.getInstruments()
        populatetree= Datastore.instance
        list=populatetree.getInstruments()
        for data in list:
            self.tree.insert("","end",values=(data['code'],data['bid'],data['spread'],data['currentPrice']))

        self.tree.grid(row=0,column=0,columnspan=3,rowspan=5,padx=10,pady=10,ipady=10)

        # Input variables
        self.instrumentCode = StringVar()
        self.entryDate = StringVar()
        self.entryPrice = StringVar()
        self.targetPrice = StringVar()
        self.stopLoss = StringVar()
        self.qty = StringVar()
        self.technicalInput = StringVar()
        self.fundamentalInput = StringVar()
        self.commentInput = StringVar()
        self.marginRate = StringVar()
        self.exitDate = StringVar()
        self.exitPrice = StringVar()
        self.type = StringVar()

        # Output variables
        self.margin = StringVar()
        self.Rrr = StringVar()
        self.marketVal = StringVar()
        self.targetVal = StringVar()
        self.tpercentVal = StringVar()
        self.stoplossVal = StringVar()
        self.percentVal = StringVar()

        # entry frame
        self.entry_frame=LabelFrame(self,text="Please enter the values:")
        self.entry_frame.grid(row=0,column=4,rowspan=9,columnspan=2,ipady=20,padx=10)

        # entry label
        self.entryLabel= Label(self.entry_frame,text="Entry Price:")
        self.entryLabel.grid(row=1,column=4,padx=10,pady=10)
        self.entryLabel_input=Entry(self.entry_frame,textvariable=self.entryPrice)
        self.entryLabel_input.grid(row=1,column=5,padx=10,pady=10)

        # target price
        self.targetPriceLabel=Label(self.entry_frame,text="Target Price:")
        self.targetPriceLabel.grid(row=2,column=4,padx=10,pady=10)
        self.targetLabel_input=Entry(self.entry_frame,textvariable=self.targetPrice)
        self.targetLabel_input.grid(row=2,column=5,padx=10,pady=10)

        # stop loss
        self.stopLossLabel=Label(self.entry_frame,text="S/L:")
        self.stopLossLabel.grid(row=3,column=4,padx=10,pady=10)
        self.stopLoss_input=Entry(self.entry_frame,textvariable=self.stopLoss)
        self.stopLoss_input.grid(row=3,column=5,padx=10,pady=10)

        # Qty
        self.qtyLabel=Label(self.entry_frame,text="Qty:")
        self.qtyLabel.grid(row=4,column=4,padx=10,pady=10)
        self.qty_input=Entry(self.entry_frame,textvariable=self.qty)
        self.qty_input.grid(row=4,column=5,padx=10,pady=10)

        # Technical Textbox
        self.technicalLabel=Label(self.entry_frame,text="technical:")
        self.technicalLabel.grid(row=5,column=4,padx=10,pady=10)
        self.technical_input=Text(self.entry_frame,height=3, width=25)
        self.technical_input.grid(row=5,column=5,columnspan=2,padx=10,pady=10)
        # function to retrieve input

        # fundamentals textbox
        self.fundamentalLabel=Label(self.entry_frame,text="Fundamental:")
        self.fundamentalLabel.grid(row=6,column=4,padx=10,pady=10)
        self.fundamental_input=Text(self.entry_frame,height=3,width=25)
        self.fundamental_input.grid(row=6,column=5,columnspan=2,padx=10,pady=10)

        # Comments textbox
        self.commentLabel=Label(self.entry_frame,text="Comment:")
        self.commentLabel.grid(row=7,column=4,padx=10,pady=10)
        self.comment_input=Text(self.entry_frame,height=3,width=25)
        self.comment_input.grid(row=7,column=5,columnspan=2,padx=10,pady=10)

        # calculation frame
        self.calculation_frame=LabelFrame(self,text="Calculation Output")
        self.calculation_frame.grid(row=0,column=7,rowspan=5,columnspan=2,ipady=10,padx=5)

        # margin rate entry
        self.marginRateLabel=Label(self.calculation_frame,text="Margin rate:")
        self.marginRateLabel.grid(row=0,column=7,padx=10,pady=10)
        self.marginRate_input=Entry(self.calculation_frame,textvariable=self.marginRate)
        self.marginRate_input.grid(row=0,column=8,padx=10,pady=10)
        self.marginRate_input.configure(state="disable")

        # margin entry
        self.marginLabel= Label(self.calculation_frame,text="Margin:")
        self.marginLabel.grid(row=1,column=7,padx=10,pady=10)
        self.margin_input=Entry(self.calculation_frame,textvariable=self.margin)
        self.margin_input.grid(row=1,column=8,padx=10,pady=10)
        self.margin_input.configure(state="disable")

        #R.R.R risk reward ratio
        self.RrrLabel=Label(self.calculation_frame,text="R.R Ratio:")
        self.RrrLabel.grid(row=2,column=7,padx=10,pady=10)
        self.Rrr_input=Entry(self.calculation_frame,textvariable=self.Rrr)
        self.Rrr_input.grid(row=2,column=8,padx=10,pady=10)
        self.Rrr_input.configure(state="disable")

        # Market value
        self.marketValLabel=Label(self.calculation_frame,text="Market Value:")
        self.marketValLabel.grid(row=3,column=7,padx=10,pady=10)
        self.marketVal_input=Entry(self.calculation_frame,textvariable=self.marketVal)
        self.marketVal_input.grid(row=3,column=8,padx=10,pady=10)
        self.marketVal_input.configure(state="disable")

        # target Value
        self.targetValLabel=Label(self.calculation_frame,text="targetVal:")
        self.targetValLabel.grid(row=4,column=7,padx=10,pady=10)
        self.targetVal_input=Entry(self.calculation_frame,textvariable=self.targetVal)
        self.targetVal_input.grid(row=4,column=8,padx=5,pady=5)

        self.percentLabel=Label(self.calculation_frame,text="%")
        self.percentLabel.grid(row=4,column=9)
        self.tpercentVal_input=Entry(self.calculation_frame,textvariable=self.tpercentVal)
        self.tpercentVal_input.grid(row=4,column=10,ipadx=5,padx=5)
        self.tpercentVal_input.configure(state="disable")
        self.targetVal_input.configure(state="disable")

        # stop loss value
        self.stoplossValLabel=Label(self.calculation_frame,text="Stop Loss Value:")
        self.stoplossValLabel.grid(row=5,column=7,padx=10,pady=10)
        self.stoplossVal_input=Entry(self.calculation_frame,textvariable=self.stoplossVal)
        self.stoplossVal_input.grid(row=5,column=8,padx=5,pady=5)

        self.percentLabel2=Label(self.calculation_frame,text="%")
        self.percentLabel2.grid(row=5,column=9)

        self.percentVal_input=Entry(self.calculation_frame,textvariable=self.percentVal)
        self.percentVal_input.grid(row=5,column=10,ipadx=5,padx=5)

        self.stoplossVal_input.configure(state="disable")
        self.percentVal_input.configure(state="disable")

        # buttons
        self.add_button = Button(self, text="Add", command=self.add_button_click)
        self.add_button.grid(row=5, column=6, ipadx=75, padx=5, pady=5, columnspan=2)
        self.add_button.configure(state="disable")

        # entryTicket_button=Button(root,text="Entry Ticket")
        # entryTicket_button.grid(row=8,column=0,ipadx=20,padx=10,pady=5)

        self.entry_button = Button(self.entry_frame, text="Calculate", command=self.enable_calcwidget)
        self.entry_button.grid(row=8, column=4, ipadx=80, padx=20, pady=15, columnspan=2)

        self.cancel_button = Button(self, text="Cancel", command=self.destroy_window)
        self.cancel_button.grid(row=5, column=8, ipadx=70, padx=5, columnspan=2, pady=5)

    def enable_calcwidget(self):
        #testing
        try:
            entrystr=float(self.entryPrice.get())
            targetstr=float(self.targetPrice.get())
            slstr=float(self.stopLoss.get())
            qtystr=float(self.qty.get())
            # assetstr=float(optionVariable.get())

        except ValueError:
            messagebox.showinfo("Error", "Please enter a float/integer")
        else:
            for child in self.calculation_frame.winfo_children():
                child.configure(state="normal")
            self.Rrr_input.delete(0, END)
            self.Rrr_input.insert(0, self.calculator.calcRRR(entrystr, targetstr, slstr))

            self.margin_input.delete(0,END)
            # TODO list:assetMargin is 0.3 for placeholder.change
            self.margin_input.insert(0,self.calculator.calcMargin(entrystr,0.3,qtystr))

            self.marketVal_input.delete(0,END)
            self.marketVal_input.insert(0,self.calculator.calcMarketval(entrystr,qtystr))

            self.stoplossVal_input.delete(0,END)
            self.stoplossVal_input.insert(0,self.calculator.stoplossVal(entrystr,slstr,qtystr))

            self.percentVal_input.delete(0,END)
            self.percentVal_input.insert(0,self.calculator.stoplossPercent(entrystr,slstr,qtystr))

            self.targetVal_input.delete(0,END)
            self.targetVal_input.insert(0,self.calculator.targetVal(entrystr,targetstr,qtystr))

            self.tpercentVal_input.delete(0,END)
            self.tpercentVal_input.insert(0,self.calculator.targetPercent(entrystr,targetstr,qtystr))


            self.add_button.configure(state="normal")
            self.get_instrument()

            instru=Datastore.instance.getInstrument(self.get_instrument())
            rate=instru.marginRate
            print(rate)
            self.marginRate_input.insert(0,rate)


    def destroy_window(self):
        self.destroy()

    def get_instrument(self):
        try:
            selected_row=self.tree.focus()
            return self.tree.item(selected_row)['values'][0]
        except IndexError:
            messagebox.showerror("ERROR", "Please select an Instrument")


    def add_button_click(self):
        # Defining variables to store the data
        self.instrumentVar = self.get_instrument()
        self.entryDate = time.time()
        # entrystr = entryPrice.get()
        self.entryPriceVar  = self.entryPrice.get()
        self.targetPriceVar = self.targetPrice.get()
        self.stopLossVar    = self.stopLoss.get()
        self.qtyVar         = self.qty.get()
        self.technicalInputVar   = self.technical_input.get("1.0",END)
        self.fundamentalInputVar = self.fundamental_input.get("1.0",END)
        self.commentInputVar = self.comment_input.get("1.0",END)
        self.marginRateVar   = self.marginRate.get()
        # print(type(entrystr))

        # Adding to the database
        newAsset = Asset({"instrumentCode":self.instrumentVar,
                          "entryDate":self.entryDate,
                          "entryPrice":self.entryPriceVar,
                          "targetPrice":self.targetPriceVar,
                          "stopLossPrice":self.stopLossVar,
                          "qty":self.qtyVar,
                          "technicals":self.technicalInputVar,
                          "fundamentals":self.fundamentalInputVar,
                          "commons":self.commentInputVar,
                          "marginRate":self.marginRateVar
                          })

        # print(instrumentVar)
        # Deleting from the window
        # self.margin_input.delete(0, END)
        # self.marketVal_input.delete(0,END)
        # self.targetVal_input.delete(0,END)
        # self.percentVal_input.delete(0,END)
        # self.stoplossVal_input.delete(0,END)
        # self.tpercentVal_input.delete(0,END)
        # self.marginRate_input.delete(0, END)
        # self.Rrr_input.delete(0,END)
        # self.entryLabel_input.delete(0, END)
        # self.targetLabel_input.delete(0, END)
        # self.stopLoss_input.delete(0, END)
        # self.qty_input.delete(0, END)
        # self.technical_input.delete(1.0, END)
        # self.fundamental_input.delete(1.0, END)
        # self.comment_input.delete(1.0, END)
        #super(MainView, self).displayDash()




class DashboardGUI(Page):
    def __init__(self, parent):
        Page.__init__(self, parent)

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
        self.reloadAssets()

        self.button_frame = Frame(self)
        self.button_frame.grid(row=2, column=1)
        self.close_button = Button(self.button_frame, text="Exit", padx=10, pady=5, command=self.close)
        self.close_button.pack(side=LEFT)

        self.add_button = Button(self.button_frame, text="Add", padx=10, pady=5, command=self.click_add)
        self.add_button.pack(side=LEFT)

    def reloadAssets(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

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





class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.addPage = AddAssetGUI(self)
        self.dashBoardPage = DashboardGUI(self)

        self.buttonframe = tk.Frame(self)
        self.container = tk.Frame(self)
        self.buttonframe.pack(side="top", fill="x", expand=False)
        self.container.pack(side="top", fill="both", expand=True)

        self.addPage.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.dashBoardPage.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)

        self.b1 = tk.Button(self.buttonframe, text="add", command=self.displayAdd)
        self.b2 = tk.Button(self.buttonframe, text="dash", command=self.displayDash)

        self.b1.pack(side="left")
        self.b2.pack(side="left")

        self.displayDash()

    def displayAdd(self):
        print("Display add")
        self.dashBoardPage.lift()
        self.addPage.show()

    def displayDash(self):
        print("Display Dash")
        self.addPage.lift()
        self.dashBoardPage.reloadAssets()
        self.dashBoardPage.show()


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

