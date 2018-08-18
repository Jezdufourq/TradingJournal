from tkinter import *
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


def on_frame_configure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))


def create_dashboard(root):

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
    current_frame = Frame(root, borderwidth=1)
    current_frame.config(highlightbackground="black")
    current_frame.grid(row=0, column=1, sticky=N, pady=(60, 0), padx=(0, 50))

    current_exposure = Label(current_frame, text="Current Exposure: ")
    current_portfolio_value = Label(current_frame, text="Current Portfolio Value: ")
    current_risk = Label(current_frame, text="Current Risk: ")
    sharp_ratio = Label(current_frame, text="Sharp Ratio: ")
    unrealized_pl_dollar = Label(current_frame, text="Unrealized P/L ($): ")
    unrealized_pl_percent = Label(current_frame, text="Unrealized P/L (%): ")

    current_exposure.grid(row=0, column=0, sticky=W)
    current_portfolio_value.grid(row=1, column=0, sticky=W)
    current_risk.grid(row=2, column=0, sticky=W)
    sharp_ratio.grid(row=3, column=0, sticky=W)
    unrealized_pl_dollar.grid(row=4, column=0, sticky=W)
    unrealized_pl_percent.grid(row=5, column=0, sticky=W)

    exposure_value = Label(current_frame, text=0)
    portfolio_value = Label(current_frame, text=0)
    risk_value = Label(current_frame, text=0)
    sharp_ratio_value = Label(current_frame, text=0)
    upd_value = Label(current_frame, text=0)
    upp_value = Label(current_frame, text=0)

    exposure_value.grid(row=0, column=1)
    portfolio_value.grid(row=1, column=1)
    risk_value.grid(row=2, column=1)
    sharp_ratio_value.grid(row=3, column=1)
    upd_value.grid(row=4, column=1)
    upp_value.grid(row=5, column=1)

    # delete button
    delete=Button(current_frame,text="Exit")
    delete.grid(row=20,column=0,columnspan=2,pady=20,ipadx=20)

    #
    # Table of values
    #

    canvas_frame = Frame(root)
    canvas_frame.grid(row=1, column=0, columnspan=2, sticky=W+E)

    canvas = Canvas(canvas_frame, width=830)
    table_frame = Frame(canvas)
    scrollbar = Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=RIGHT, fill="y")
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    canvas.create_window((0, 0), window=table_frame, anchor=NW)

    table_frame.bind("<Configure>", lambda event, canvas=canvas: on_frame_configure(canvas))

    headings = ["Date", "Ticker", "Mkt Value", "Entry Price", "Current Price", "P/L ($)", "P/L (%)", "Live Risk"]

    column_count = 0

    for heading in headings:
        column = Entry(table_frame, width=10, relief="groove")
        column.insert(END, heading)
        column.config(state="readonly")
        column.grid(row=0, column=column_count, padx=0, pady=0)
        column_count += 1

    for j in range(20):
        for i in range(len(headings)):
            entry = Entry(table_frame, width=10, relief="groove")
            entry.grid(row=j+1, column=i, padx=0, pady=0)

    # TODO: use for loop to insert values to the table from sql queries?


