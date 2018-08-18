from tkinter import *
import dashboard

root=Tk()
root.wm_title("Entry Ticket")

# entry label
entryLabel= Label(root,text="Entry Price:")
entryLabel.grid(row=0,column=0,padx=10,pady=10)

entryPrice=StringVar()
entryLabel_input=Entry(root,textvariable=entryPrice)
entryLabel_input.grid(row=0,column=1,padx=10,pady=10)

# target price
targetPriceLabel=Label(root,text="Target Price:")
targetPriceLabel.grid(row=1,column=0,padx=10,pady=10)

targetPrice=StringVar()
targetLabel_input=Entry(root,textvariable=targetPrice)
targetLabel_input.grid(row=1,column=1,padx=10,pady=10)

# stop loss
stopLossLabel=Label(root,text="S/L:")
stopLossLabel.grid(row=2,column=0,padx=10,pady=10)

stopLoss=StringVar()
stopLoss_input=Entry(root,textvariable=stopLoss)
stopLoss_input.grid(row=2,column=1,padx=10,pady=10)

# Asset dropdown box
assetlabel=Label(root,text="Asset:")
assetlabel.grid(row=3,column=0,padx=10,pady=10)
Options=["one","two","three"]
optionVariable=StringVar()
optionVariable.set(Options[0])
asset=OptionMenu(root,optionVariable,*Options)
asset.grid(row=3,column=1,padx=10,pady=10,ipadx=15)
# functions to get value from dropdown box


# Qty
qtyLabel=Label(root,text="Qty:")
qtyLabel.grid(row=4,column=0,padx=10,pady=10)
qty=StringVar()
qty_input=Entry(root,textvariable=qty)
qty_input.grid(row=4,column=1,padx=10,pady=10)

# Technical Textbox
technicalLabel=Label(root,text="technical:")
technicalLabel.grid(row=5,column=0,padx=10,pady=10)
technical_input=Text(root,height=3, width=25)
technical_input.grid(row=5,column=1,columnspan=2,padx=10,pady=10)
# function to retrieve input

# fundamentals textbox
fundamentalLabel=Label(root,text="Fundamental:")
fundamentalLabel.grid(row=6,column=0,padx=10,pady=10)
fundamental_input=Text(root,height=3,width=25)
fundamental_input.grid(row=6,column=1,columnspan=2,padx=10,pady=10)

# Comments textbox
commentLabel=Label(root,text="Comment:")
commentLabel.grid(row=7,column=0,padx=10,pady=10)
comment_input=Text(root,height=3,width=25)
comment_input.grid(row=7,column=1,columnspan=2,padx=10,pady=10)

# margin entry
marginLabel= Label(root,text="Margin:")
marginLabel.grid(row=0,column=3,padx=10,pady=10)
margin=StringVar()
margin_input=Entry(root,textvariable=margin)
margin_input.grid(row=0,column=4,padx=10,pady=10)

# current price entry
currentLabel=Label(root,text="Current Price:")
currentLabel.grid(row=1,column=3,padx=10,pady=10)
current=StringVar()
current_input=Entry(root,textvariable=current)
current_input.grid(row=1,column=4,padx=10,pady=10)

# Account value entry
accountLabel=Label(root,text="Account Value:")
accountLabel.grid(row=2,column=3,padx=10,pady=10)
account=StringVar()
account_input=Entry(root,textvariable=account)
account_input.grid(row=2,column=4,padx=10,pady=10)

# spread entry
spreadLabel=Label(root,text="Spread:")
spreadLabel.grid(row=3,column=3,padx=10,pady=10)
spread=StringVar()
spread_input=Entry(root,textvariable=spread)
spread_input.grid(row=3,column=4,padx=10,pady=10)

#R.R.R risk reward ration
RrrLabel=Label(root,text="R.R Ratio:")
RrrLabel.grid(row=4,column=3,padx=10,pady=10)
Rrr=StringVar()
Rrr_input=Entry(root,textvariable=Rrr)
Rrr_input.grid(row=4,column=4,padx=10,pady=10)

# Market value
marketValLabel=Label(root,text="Market Value:")
marketValLabel.grid(row=5,column=3,padx=10,pady=10)
marketVal=StringVar()
marketVal_input=Entry(root,textvariable=marketVal)
marketVal_input.grid(row=5,column=4,padx=10,pady=10)

# Stop Loss Value
targetValLabel=Label(root,text="targetVal:")
targetValLabel.grid(row=6,column=3,padx=10,pady=10)
targetVal=StringVar()
targetVal_input=Entry(root,textvariable=targetVal)
targetVal_input.grid(row=6,column=4,padx=5,pady=5)


# creating new windows
def new_window():
    new_win= Toplevel(root)
    dashboard.create_dashboard(new_win)

# buttons
dashboard_button= Button(root,text="Dashboard",command=new_window)
dashboard_button.grid(row=8,column=1,ipadx=20,padx=10,pady=5)

entryTicket_button=Button(root,text="Entry Ticket")
entryTicket_button.grid(row=8,column=0,ipadx=20,padx=10,pady=5)

entry_button=Button(root,text="Entry")
entry_button.grid(row=7,column=4,ipadx=50,padx=5)

export_button=Button(root,text="Export")
export_button.grid(row=8,column=4,ipadx=50,padx=5)


# it's written like this to escape from a bug that occurs on OSX.
while True:
    try:
        root.mainloop()
        break
    except UnicodeDecodeError:
        pass

