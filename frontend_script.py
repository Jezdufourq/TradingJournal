from tkinter import *
import dashboard
# import dummy
import tkinter.ttk as ttk
from tkinter import messagebox
from calculationHandler import entryCalculation
import db.DAO as DAO
import db.instruments as instru

root=Tk()
root.wm_title("Entry Ticket")
calculator= entryCalculation()

# asset frame
asset_frame=LabelFrame(root,text="Instruments:")
asset_frame.grid(row=0,column=0,columnspan=4)
# # label
# example=Label(asset_frame,text="example")
# example.grid(row=0,column=0)

tree= ttk.Treeview(asset_frame)
tree["columns"]=(1,2,3,4)
tree["show"]="headings"
headings=["Instrument","Bid","Spread","ASK"]

column_index=1

for heading in headings:
    tree.column(column_index,width=95)
    tree.heading(column_index,text=heading)
    column_index+=1

tree.insert("", "end", values=("Blah blah",100, 3500,32))
tree.insert("", "end", values=("Blah blah",101, 3500,35))
tree.insert("", "end", values=("Blah blah",102, 3500,20))
tree.insert("", "end", values=("Blah blah",103, 3500,31))
tree.insert("", "end", values=("Blah blah",104, 3500,37))
tree.insert("", "end", values=("Blah blah",105, 3500,39))
tree.insert("", "end", values=("Blah blah",106, 3500,30))

tree.grid(row=0,column=0,columnspan=3)

# TODO list: grabbing the value from the dictionary and displaying it in console log
# TODO list: populate the treeviw with a list of dictionaries sample
# TODO list: take the value of the table selected and display it 

# Defining the input variables
instrumentCode = StringVar()
entryPrice = StringVar()
targetPrice = StringVar()
stopLoss = StringVar()
qty = StringVar()
technicalInput = StringVar()
fundamentalInput = StringVar()
commentInput = StringVar()
marginRate = StringVar()

# Defining the calculation variables
margin=StringVar()
Rrr=StringVar()
marketVal=StringVar()
targetVal=StringVar()
stoplossVal=StringVar()
percentVal=StringVar()
tpercentVal=StringVar()

# entry frame
entry_frame=LabelFrame(root,text="Please enter the values:")
entry_frame.grid(row=0,column=4,rowspan=9,columnspan=2,ipady=20,padx=10)

# ENTRY LABEL

# Defining the entry price
entryLabel= Label(entry_frame,text="Entry Price:")
entryLabel.grid(row=1,column=4,padx=10,pady=10)
entryLabel_input=Entry(entry_frame,textvariable=entryPrice)
entryLabel_input.grid(row=1,column=5,padx=10,pady=10)

# defining the target price
targetPriceLabel=Label(entry_frame,text="Target Price:")
targetPriceLabel.grid(row=2,column=4,padx=10,pady=10)
targetLabel_input=Entry(entry_frame,textvariable=targetPrice)
targetLabel_input.grid(row=2,column=5,padx=10,pady=10)

# Defining the stop loss
stopLossLabel=Label(entry_frame,text="S/L:")
stopLossLabel.grid(row=3,column=4,padx=10,pady=10)
stopLoss_input=Entry(entry_frame,textvariable=stopLoss)
stopLoss_input.grid(row=3,column=5,padx=10,pady=10)

# Defining the qty
qtyLabel=Label(entry_frame,text="Qty:")
qtyLabel.grid(row=4,column=4,padx=10,pady=10)
qty_input=Entry(entry_frame,textvariable=qty)
qty_input.grid(row=4,column=5,padx=10,pady=10)

# Defining the technical input
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

#R.R.R risk reward ration
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

def enable_addwidget():
    try:
        instrumentStr = float()
        entryStr=float(entryPrice.get())
        targetStr=float(targetPrice.get())
        stoplossStr=float(stopLoss.get())
        qtyStr=float(qty.get())
        techStr = float()
        fundStr = float()
        comsStr = float()
        marginStr = float()

    except ValueError:
        messagebox.showinfo("Error", "Please enter a float/integer")

    # Grabbing the data and putting it into the database



def destroy_window():
    root.destroy()


# buttons
add_button= Button(root,text="Add")
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

