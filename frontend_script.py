from tkinter import *
import dashboard
# import dummy
import tkinter.ttk as ttk
from tkinter import messagebox
from calculationHandler import entryCalculation
from db.DAO import Datastore
from db.instruments import Asset,Instrument
import time

root=Tk()
root.wm_title("Entry Ticket")
calculator= entryCalculation()

# asset frame
asset_frame=LabelFrame(root,text="Instruments:")
asset_frame.grid(row=0,column=0,columnspan=4,rowspan=9,padx=5,pady=10)

tree= ttk.Treeview(asset_frame)
tree["columns"]=(1,2,3,4)
tree["show"]="headings"
headings=["Instrument","Bid","Spread","ASK"]

column_index=1

for heading in headings:
    tree.column(column_index,width=95)
    tree.heading(column_index,text=heading)
    column_index+=1

# populateTree=Datastore.instance.getInstruments()
populatetree= Datastore.instance
list=populatetree.getInstruments()
print(list)
for data in list:
    print(data)
    tree.insert("","end",values=(data['code'],data['bid'],data['spread'],data['currentPrice']))


tree.grid(row=0,column=0,columnspan=3,rowspan=5,padx=10,pady=10,ipady=10)

# Input variables
instrumentCode = StringVar()
entryDate = StringVar()
entryPrice = StringVar()
targetPrice = StringVar()
stopLoss = StringVar()
qty = StringVar()
technicalInput = StringVar()
fundamentalInput = StringVar()
commentInput = StringVar()
marginRate = StringVar()
exitDate = StringVar()
exitPrice = StringVar()
type = StringVar()

# Output variables
margin = StringVar()
Rrr = StringVar()
marketVal = StringVar()
targetVal = StringVar()
tpercentVal = StringVar()
stoplossVal = StringVar()
percentVal = StringVar()

# entry frame
entry_frame=LabelFrame(root,text="Please enter the values:")
entry_frame.grid(row=0,column=4,rowspan=9,columnspan=2,ipady=20,padx=10)

# entry label
entryLabel= Label(entry_frame,text="Entry Price:")
entryLabel.grid(row=1,column=4,padx=10,pady=10)
entryLabel_input=Entry(entry_frame,textvariable=entryPrice)
entryLabel_input.grid(row=1,column=5,padx=10,pady=10)

# target price
targetPriceLabel=Label(entry_frame,text="Target Price:")
targetPriceLabel.grid(row=2,column=4,padx=10,pady=10)
targetLabel_input=Entry(entry_frame,textvariable=targetPrice)
targetLabel_input.grid(row=2,column=5,padx=10,pady=10)

# stop loss
stopLossLabel=Label(entry_frame,text="S/L:")
stopLossLabel.grid(row=3,column=4,padx=10,pady=10)
stopLoss_input=Entry(entry_frame,textvariable=stopLoss)
stopLoss_input.grid(row=3,column=5,padx=10,pady=10)

# Qty
qtyLabel=Label(entry_frame,text="Qty:")
qtyLabel.grid(row=4,column=4,padx=10,pady=10)
qty_input=Entry(entry_frame,textvariable=qty)
qty_input.grid(row=4,column=5,padx=10,pady=10)

# Technical Textbox
technicalLabel=Label(entry_frame,text="technical:")
technicalLabel.grid(row=5,column=4,padx=10,pady=10)
technical_input=Text(entry_frame,height=3, width=25)
technical_input.grid(row=5,column=5,columnspan=2,padx=10,pady=10)
# function to retrieve input

# fundamentals textbox
fundamentalLabel=Label(entry_frame,text="Fundamental:")
fundamentalLabel.grid(row=6,column=4,padx=10,pady=10)
fundamental_input=Text(entry_frame,height=3,width=25)
fundamental_input.grid(row=6,column=5,columnspan=2,padx=10,pady=10)

# Comments textbox
commentLabel=Label(entry_frame,text="Comment:")
commentLabel.grid(row=7,column=4,padx=10,pady=10)
comment_input=Text(entry_frame,height=3,width=25)
comment_input.grid(row=7,column=5,columnspan=2,padx=10,pady=10)

# calculation frame
calculation_frame=LabelFrame(root,text="Calculation Output")
calculation_frame.grid(row=0,column=7,rowspan=5,columnspan=2,ipady=10,padx=5)

# margin rate entry
marginRateLabel=Label(calculation_frame,text="Margin rate:")
marginRateLabel.grid(row=0,column=7,padx=10,pady=10)
marginRate_input=Entry(calculation_frame,textvariable=marginRate)
marginRate_input.grid(row=0,column=8,padx=10,pady=10)
marginRate_input.configure(state="disable")

# margin entry
marginLabel= Label(calculation_frame,text="Margin:")
marginLabel.grid(row=1,column=7,padx=10,pady=10)
margin_input=Entry(calculation_frame,textvariable=margin)
margin_input.grid(row=1,column=8,padx=10,pady=10)
margin_input.configure(state="disable")

#R.R.R risk reward ratio
RrrLabel=Label(calculation_frame,text="R.R Ratio:")
RrrLabel.grid(row=2,column=7,padx=10,pady=10)
Rrr_input=Entry(calculation_frame,textvariable=Rrr)
Rrr_input.grid(row=2,column=8,padx=10,pady=10)
Rrr_input.configure(state="disable")

# Market value
marketValLabel=Label(calculation_frame,text="Market Value:")
marketValLabel.grid(row=3,column=7,padx=10,pady=10)
marketVal_input=Entry(calculation_frame,textvariable=marketVal)
marketVal_input.grid(row=3,column=8,padx=10,pady=10)
marketVal_input.configure(state="disable")

# target Value
targetValLabel=Label(calculation_frame,text="targetVal:")
targetValLabel.grid(row=4,column=7,padx=10,pady=10)
targetVal_input=Entry(calculation_frame,textvariable=targetVal)
targetVal_input.grid(row=4,column=8,padx=5,pady=5)

percentLabel=Label(calculation_frame,text="%")
percentLabel.grid(row=4,column=9)
tpercentVal_input=Entry(calculation_frame,textvariable=tpercentVal)
tpercentVal_input.grid(row=4,column=10,ipadx=5,padx=5)
tpercentVal_input.configure(state="disable")
targetVal_input.configure(state="disable")

# stop loss value
stoplossValLabel=Label(calculation_frame,text="Stop Loss Value:")
stoplossValLabel.grid(row=5,column=7,padx=10,pady=10)
stoplossVal_input=Entry(calculation_frame,textvariable=stoplossVal)
stoplossVal_input.grid(row=5,column=8,padx=5,pady=5)

percentLabel2=Label(calculation_frame,text="%")
percentLabel2.grid(row=5,column=9)

percentVal_input=Entry(calculation_frame,textvariable=percentVal)
percentVal_input.grid(row=5,column=10,ipadx=5,padx=5)

stoplossVal_input.configure(state="disable")
percentVal_input.configure(state="disable")


# enabling frame
def enable_calcwidget():
    #testing
    try:
        entrystr=float(entryPrice.get())
        targetstr=float(targetPrice.get())
        slstr=float(stopLoss.get())
        qtystr=float(qty.get())
        # assetstr=float(optionVariable.get())

    except ValueError:
        messagebox.showinfo("Error", "Please enter a float/integer")
    else:
        for child in calculation_frame.winfo_children():
            child.configure(state="normal")
        Rrr_input.delete(0, END)
        Rrr_input.insert(0,calculator.calcRRR(entrystr,targetstr,slstr))

        margin_input.delete(0,END)
        # TODO list:assetMargin is 0.3 for placeholder.change
        margin_input.insert(0,calculator.calcMargin(entrystr,0.3,qtystr))

        marketVal_input.delete(0,END)
        marketVal_input.insert(0,calculator.calcMarketval(entrystr,qtystr))

        stoplossVal_input.delete(0,END)
        stoplossVal_input.insert(0,calculator.stoplossVal(entrystr,slstr,qtystr))

        percentVal_input.delete(0,END)
        percentVal_input.insert(0,calculator.stoplossPercent(entrystr,slstr,qtystr))

        targetVal_input.delete(0,END)
        targetVal_input.insert(0,calculator.targetVal(entrystr,targetstr,qtystr))

        tpercentVal_input.delete(0,END)
        tpercentVal_input.insert(0,calculator.targetPercent(entrystr,targetstr,qtystr))

        entryLabel_input.delete(0,END)
        targetLabel_input.delete(0,END)
        stopLoss_input.delete(0,END)
        qty_input.delete(0,END)

        add_button.configure(state="normal")
        get_instrument()

def destroy_window():
    root.destroy()

def get_instrument():
    selected_row=tree.focus()
    return tree.item(selected_row)['values'][0]
    # print(tree.item(selected_row)['values'][0])

def add_button():
    # Defining variables to store the data
    instrumentVar = get_instrument()
    entryDate = time.time()
    entryPriceVar = entryLabel_input.get()
    targetPriceVar = targetLabel_input.get()
    stopLossVar = stopLoss_input.get()
    qtyVar = qty_input.get()
    technicalInputVar = technical_input.get("1.0",END)
    fundamentalInputVar = fundamental_input.get("1.0",END)
    commentInputVar = comment_input.get("1.0",END)
    marginRateVar = marginRate_input.get()

    # Adding to the database
    newAsset = Asset({"instrumentCode":instrumentVar,
                      "entryDate":entryDate,
                      "entryPrice":entryPriceVar,
                      "targetPrice":targetPriceVar,
                      "stopLossPrice":stopLossVar,
                      "qty":qtyVar,
                      "technicals":technicalInputVar,
                      "fundamentals":fundamentalInputVar,
                      "commons":commentInputVar,
                      "marginRate":marginRateVar
                      })
    print(newAsset)

    # Deleting from the window
    entryLabel_input.delete(0, END)
    targetLabel_input.delete(0, END)
    stopLoss_input.delete(0, END)
    qty_input.delete(0, END)
    technical_input.delete(1.0, END)
    fundamental_input.delete(1.0, END)
    comment_input.delete(1.0, END)
    marginRate_input.delete(0, END)


# buttons
add_button= Button(root,text="Add",command=add_button)
add_button.grid(row=5,column=6,ipadx=75,padx=5,pady=5,columnspan=2)
add_button.configure(state="disable")

# entryTicket_button=Button(root,text="Entry Ticket")
# entryTicket_button.grid(row=8,column=0,ipadx=20,padx=10,pady=5)

entry_button=Button(entry_frame,text="Calculate",command=enable_calcwidget)
entry_button.grid(row=8,column=4,ipadx=80,padx=20,pady=15,columnspan=2)

cancel_button=Button(root,text="Cancel",command=destroy_window)
cancel_button.grid(row=5,column=8,ipadx=70,padx=5,columnspan=2,pady=5)


# print(dummy.sum(1,3))
# it's written like this to escape from a bug that occurs on OSX.
while True:
    try:
        root.mainloop()
        break
    except UnicodeDecodeError:
        pass
