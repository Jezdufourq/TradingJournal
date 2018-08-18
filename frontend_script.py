from tkinter import *
import dashboard
# import dummy
from tkinter import messagebox
from calculationHandler import entryCalculation


root=Tk()
root.wm_title("Entry Ticket")
calculator= entryCalculation()


# entry frame
entry_frame=LabelFrame(root,text="Please enter the values:")
entry_frame.grid(row=0,column=0,rowspan=7,columnspan=2,ipady=20,padx=10)

# entry label
entryLabel= Label(entry_frame,text="Entry Price:")
entryLabel.grid(row=1,column=0,padx=10,pady=10)

entryPrice=StringVar()
entryLabel_input=Entry(entry_frame,textvariable=entryPrice)
entryLabel_input.grid(row=1,column=1,padx=10,pady=10)

# target price
targetPriceLabel=Label(entry_frame,text="Target Price:")
targetPriceLabel.grid(row=2,column=0,padx=10,pady=10)

targetPrice=StringVar()
targetLabel_input=Entry(entry_frame,textvariable=targetPrice)
targetLabel_input.grid(row=2,column=1,padx=10,pady=10)

# stop loss
stopLossLabel=Label(entry_frame,text="S/L:")
stopLossLabel.grid(row=3,column=0,padx=10,pady=10)

stopLoss=StringVar()
stopLoss_input=Entry(entry_frame,textvariable=stopLoss)
stopLoss_input.grid(row=3,column=1,padx=10,pady=10)

# Asset dropdown box
assetlabel=Label(entry_frame,text="Asset:")
assetlabel.grid(row=4,column=0,padx=10,pady=10)
Options=["1","2","3","4","5","6","7","8","9","10"]
optionVariable=StringVar()
optionVariable.set(Options[0])
asset=OptionMenu(entry_frame,optionVariable,*Options)
asset.grid(row=4,column=1,padx=10,pady=10,ipadx=15)
# functions to get value from dropdown box


# Qty
qtyLabel=Label(entry_frame,text="Qty:")
qtyLabel.grid(row=5,column=0,padx=10,pady=10)
qty=StringVar()
qty_input=Entry(entry_frame,textvariable=qty)
qty_input.grid(row=5,column=1,padx=10,pady=10)

# Technical Textbox
technicalLabel=Label(entry_frame,text="technical:")
technicalLabel.grid(row=6,column=0,padx=10,pady=10)
technical_input=Text(entry_frame,height=3, width=25)
technical_input.grid(row=6,column=1,columnspan=2,padx=10,pady=10)
# function to retrieve input

# fundamentals textbox
fundamentalLabel=Label(entry_frame,text="Fundamental:")
fundamentalLabel.grid(row=7,column=0,padx=10,pady=10)
fundamental_input=Text(entry_frame,height=3,width=25)
fundamental_input.grid(row=7,column=1,columnspan=2,padx=10,pady=10)

# Comments textbox
commentLabel=Label(entry_frame,text="Comment:")
commentLabel.grid(row=8,column=0,padx=10,pady=10)
comment_input=Text(entry_frame,height=3,width=25)
comment_input.grid(row=8,column=1,columnspan=2,padx=10,pady=10)

# calculation frame
calculation_frame=LabelFrame(root,text="Calculation Output")
calculation_frame.grid(row=0,column=3,rowspan=8,columnspan=2,ipady=20,padx=5)


# margin entry
marginLabel= Label(calculation_frame,text="Margin:")
marginLabel.grid(row=1,column=3,padx=10,pady=10)
margin=StringVar()
margin_input=Entry(calculation_frame,textvariable=margin)
margin_input.grid(row=1,column=4,padx=10,pady=10)
margin_input.configure(state="disable")


# current price entry
currentLabel=Label(calculation_frame,text="Current Price:")
currentLabel.grid(row=2,column=3,padx=10,pady=10)
current=StringVar()
current_input=Entry(calculation_frame,textvariable=current)
current_input.grid(row=2,column=4,padx=10,pady=10)
current_input.configure(state="disable")


# Account value entry
accountLabel=Label(calculation_frame,text="Account Value:")
accountLabel.grid(row=3,column=3,padx=10,pady=10)
account=StringVar()
account_input=Entry(calculation_frame,textvariable=account)
account_input.grid(row=3,column=4,padx=10,pady=10)
account_input.configure(state="disable")


# spread entry
spreadLabel=Label(calculation_frame,text="Spread:")
spreadLabel.grid(row=4,column=3,padx=10,pady=10)
spread=StringVar()
spread_input=Entry(calculation_frame,textvariable=spread)
spread_input.grid(row=4,column=4,padx=10,pady=10)
spread_input.configure(state="disable")


#R.R.R risk reward ration
RrrLabel=Label(calculation_frame,text="R.R Ratio:")
RrrLabel.grid(row=5,column=3,padx=10,pady=10)
Rrr=StringVar()
Rrr_input=Entry(calculation_frame,textvariable=Rrr)
Rrr_input.grid(row=5,column=4,padx=10,pady=10)
Rrr_input.configure(state="disable")


# Market value
marketValLabel=Label(calculation_frame,text="Market Value:")
marketValLabel.grid(row=6,column=3,padx=10,pady=10)
marketVal=StringVar()
marketVal_input=Entry(calculation_frame,textvariable=marketVal)
marketVal_input.grid(row=6,column=4,padx=10,pady=10)
marketVal_input.configure(state="disable")

# target Value
targetValLabel=Label(calculation_frame,text="targetVal:")
targetValLabel.grid(row=7,column=3,padx=10,pady=10)
targetVal=StringVar()
targetVal_input=Entry(calculation_frame,textvariable=targetVal)
targetVal_input.grid(row=7,column=4,padx=5,pady=5)

percentLabel=Label(calculation_frame,text="%")
percentLabel.grid(row=7,column=5)

tpercentVal=StringVar()
tpercentVal_input=Entry(calculation_frame,textvariable=tpercentVal)
tpercentVal_input.grid(row=7,column=6,ipadx=5,padx=5)
tpercentVal_input.configure(state="disable")
targetVal_input.configure(state="disable")

# stop loss value
stoplossValLabel=Label(calculation_frame,text="Stop Loss Value:")
stoplossValLabel.grid(row=8,column=3,padx=10,pady=10)
stoplossVal=StringVar()
percentVal=StringVar()
stoplossVal_input=Entry(calculation_frame,textvariable=stoplossVal)
stoplossVal_input.grid(row=8,column=4,padx=5,pady=5)

percentLabel2=Label(calculation_frame,text="%")
percentLabel2.grid(row=8,column=5)

percentVal_input=Entry(calculation_frame,textvariable=percentVal)
percentVal_input.grid(row=8,column=6,ipadx=5,padx=5)

stoplossVal_input.configure(state="disable")
percentVal_input.configure(state="disable")

# Testing and manipulating inputs
# a=entryPrice.get()
# b=targetPrice.get()
# print(dummy.sum(a,b))

# creating new windows
def new_window():
    new_win= Toplevel(root)
    dashboard.create_dashboard(new_win)

# enabling frame
def enable_calcwidget():
    #testing
    try:
        entrystr=float(entryPrice.get())
        targetstr=float(targetPrice.get())
        slstr=float(stopLoss.get())
        qtystr=float(qty.get())
        assetstr=float(optionVariable.get())

    except ValueError:
        messagebox.showinfo("Error", "Please enter a float/integer")
    else:
        for child in calculation_frame.winfo_children():
            child.configure(state="normal")
        Rrr_input.delete(0, END)
        Rrr_input.insert(0,calculator.calcRRR(entrystr,targetstr,slstr))
        margin_input.delete(0,END)
        margin_input.insert(0,calculator.calcMargin())
        print(type(entrystr))
        print(type(targetstr))
        print(type(slstr))
        print(type(qtystr))


# buttons
dashboard_button= Button(root,text="Dashboard",command=new_window)
dashboard_button.grid(row=8,column=0,ipadx=20,padx=10,pady=5,columnspan=2)

# entryTicket_button=Button(root,text="Entry Ticket")
# entryTicket_button.grid(row=8,column=0,ipadx=20,padx=10,pady=5)

entry_button=Button(root,text="Entry",command=enable_calcwidget)
entry_button.grid(row=7,column=3,ipadx=100,padx=5,pady=15,columnspan=2)

export_button=Button(root,text="Export")
export_button.grid(row=8,column=3,ipadx=100,padx=5,columnspan=2)


# print(dummy.sum(1,3))
# it's written like this to escape from a bug that occurs on OSX.
while True:
    try:
        root.mainloop()
        break
    except UnicodeDecodeError:
        pass

