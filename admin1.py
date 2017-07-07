from Tkinter import* 
import random
import time
import json
import ttk

#print('hekii')
root=Tk()
root.geometry("1600x800+0+0")
root.title("Billing system")

Tops = Frame(root,width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
Item={}
with open('string.txt','r') as wf:
 q=wf.read()
 Item=json.loads(q)
 #print(Item)
####time###
localtime=time.asctime(time.localtime(time.time()))

###########info##
lb1 = Label(Tops , font=('arial',30,'bold'), text='Entry Product System', fg='Steel Blue' , bd=10 , anchor='w')
lb1.grid(row=0,column=0)
lb2 = Label(Tops , font=('arial',20,'bold'), text=localtime, fg='Steel Blue' , bd=10 , anchor='w')
lb2.grid(row=1,column=0)

def Reset():
 pid.set("")
 name.set("")
 department_no.set("")
 rate1.set("")
 rate2.set("")
 tax_rate.set("")

 open_rate.set("")
 opening_stock.set("")
 receipts.set("")
 sale.set("")
 issues.set("")
 monthly_sale.set("")
 amt_monthly_sale.set("")
 txtpid.focus()
def Enter(p,name,department_no,open_rate,rate1,rate2,tax_rate,opening_stock,receipts,sale,issues,amt_monthly_sale):
 Item[p]={}
 Item[p]['name']=name
 Item[p]['department_no']=department_no
 Item[p]['open_rate']=open_rate
 Item[p]['rate1']=rate1
 Item[p]['rate2']=rate2
 Item[p]['tax_rate']=tax_rate
 Item[p]['opening_stock']=opening_stock
 Item[p]['receipts']=receipts
 Item[p]['sale']=sale
 Item[p]['issues']=issues
 Item[p]['amt_monthly_sale']=0
 Item[p]['current_stock']=((float)(opening_stock)+(float)(receipts))-((float)(sale)+(float)(issues))
 

 with open('string.txt','w') as wtf:
  txt=json.dumps(Item)
  wtf.write(txt)
 


 

  
pid = StringVar()
name = StringVar()
cost = IntVar()
x = StringVar()
department_no= StringVar()
opening_stock= StringVar()
rate1= StringVar()
rate2= StringVar()
tax_rate= StringVar()
open_rate= StringVar()
receipts= StringVar()
sale= StringVar()
issues= StringVar()
#monthly_sale= StringVar()
amt_monthly_sale= StringVar()

#############---enter & escape event---############
def escape_pid(event):
 widget=event.widget
 pid.set("")
def escape_name(event):
 widget=event.widget
 name.set("")
def escape_department_no(event):
 widget=event.widget
 department_no.set("")
def escape_rate1(event):
 widget=event.widget
 rate1.set("")
def escape_rate2(event):
 widget=event.widget
 rate2.set("")
def escape_tax_rate(event):
 widget=event.widget
 tax_rate.set("")
def escape_open_rate(event):
 widget=event.widget
 open_rate.set("")
def escape_opening_stock(event):
 widget=event.widget
 opening_stock.set("")
def escape_receipts(event):
 widget=event.widget
 receipts.set("")
def escape_sale(event):
 widget=event.widget
 sale.set("")
def escape_issues(event):
 widget=event.widget
 issues.set("")
def escape_amt_monthly_sale(event):
 widget=event.widget
 amt_monthly_sale.set("")

def enter_pid(event): 
 widget = event.widget
 g=widget.get()
 if ((str)(g) in Item):
  name.set(Item[g]['name'])
  department_no.set(Item[g]['department_no'])
  rate1.set(Item[g]['rate1'])
  rate2.set(Item[g]['rate2'])
  tax_rate.set(Item[g]['tax_rate'])

  open_rate.set(Item[g]['open_rate'])
  opening_stock.set(Item[g]['opening_stock'])
  receipts.set(Item[g]['receipts'])
  sale.set(Item[g]['sale'])
  issues.set(Item[g]['issues'])
  amt_monthly_sale.set(Item[g]['amt_monthly_sale'])

 txtpnm.focus()
def enter_name(event): 


 widget = event.widget
 txtdepartment_no.focus()
def enter_department_no(event): 
 widget = event.widget
 txtrate1.focus()
def enter_rate1(event): 
 widget= event.widget
 txtrate2.focus()
def enter_rate2(event): 
 widget = event.widget
 txttax_rate.focus()
def enter_tax_rate(event): 
 widget = event.widget
 combo.focus()
def enter_open_rate(event): 
 widget = event.widget
 txtopening_stock.focus()
def enter_opening_stock(event): 
 widget = event.widget
 txtreceipts.focus()
def enter_receipts(event): 
 widget = event.widget
 txtsale.focus()
def enter_sale(event): 
 widget = event.widget
 txtissues.focus()
def enter_issues(event): 
 widget = event.widget
 txtamt_monthly_sale.focus()
def enter_amt_monthly_sale(event): 
 widget = event.widget
 Enter(pid.get(),name.get(),department_no.get(),open_rate.get(),rate1.get(),rate2.get(),tax_rate.get(),opening_stock.get(),receipts.get(),sale.get(),issues.get(),amt_monthly_sale.get())
 pid.set("")
 name.set("")
 department_no.set("")
 rate1.set("")
 rate2.set("")
 tax_rate.set("")

 open_rate.set("")
 opening_stock.set("")
 receipts.set("")
 sale.set("")
 issues.set("")
 amt_monthly_sale.set("")
 txtpid.focus()
 




p =StringVar()

 
lblpid = Label(f1 , font=('arial',16,'bold'),text='product_id',bd=16,anchor='w')
lblpid.grid(row=0,column=0)
txtpid=Entry(f1,font=('arial',16,'bold'),textvariable=pid, bd=10 ,insertwidth=4,bg='powder blue' , justify ='right' )
txtpid.grid(row=0,column=1) 
txtpid.focus()
txtpid.bind('<Return>', enter_pid)
txtpid.bind('<Escape>', escape_pid)
 
lblpnm = Label(f1 , font=('arial',16,'bold'),text='Name',bd=16,anchor='w')
lblpnm.grid(row=1,column=0)
txtpnm=Entry(f1,font=('arial',16,'bold'),textvariable=name, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txtpnm.grid(row=1,column=1)
txtpnm.bind('<Return>', enter_name)
txtpnm.bind('<Escape>', escape_name)

lbldepartment_no = Label(f1 , font=('arial',16,'bold'),text='department_no',bd=16,anchor='w')
lbldepartment_no.grid(row=2,column=0)
txtdepartment_no=Entry(f1,font=('arial',16,'bold'),textvariable=department_no, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txtdepartment_no.grid(row=2,column=1)
txtdepartment_no.bind('<Return>', enter_department_no)
txtdepartment_no.bind('<Escape>', escape_department_no)

lblrate1 = Label(f1 , font=('arial',16,'bold'),text='rate1',bd=16,anchor='w')
lblrate1.grid(row=3,column=0)
txtrate1=Entry(f1,font=('arial',16,'bold'),textvariable=rate1, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txtrate1.grid(row=3,column=1)
txtrate1.bind('<Return>', enter_rate1)
txtrate1.bind('<Escape>', escape_rate1)

lblrate2= Label(f1 , font=('arial',16,'bold'),text='rate2',bd=16,anchor='w')
lblrate2.grid(row=4,column=0)
txtrate2=Entry(f1,font=('arial',16,'bold'),textvariable=rate2, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txtrate2.grid(row=4,column=1)
txtrate2.bind('<Return>', enter_rate2)
txtrate2.bind('<Escape>', escape_rate2)

lbltax_rate = Label(f1 , font=('arial',16,'bold'),text='tax_rate',bd=16,anchor='w')
lbltax_rate.grid(row=5,column=0)
txttax_rate=Entry(f1,font=('arial',16,'bold'),textvariable=tax_rate, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txttax_rate.grid(row=5,column=1)
txttax_rate.bind('<Return>', enter_tax_rate)
txttax_rate.bind('<Escape>', escape_tax_rate)

lblopen_rate = Label(f1 , font=('arial',16,'bold'),text='open_rate',bd=16,anchor='w')
lblopen_rate.grid(row=0,column=2)
#txtopen_rate=Entry(f1,font=('arial',16,'bold'),textvariable=open_rate, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
#txtopen_rate.grid(row=0,column=3)
combo=ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=open_rate,justify='right')
combo.grid(row=0,column=3)
combo.config(values=("Yes","No"))
combo.bind('<Return>', enter_open_rate)
combo.bind('<Escape>', escape_open_rate)
f1.option_add("*TCombobox*Background", 'powder blue')

lblopening_stock = Label(f1 , font=('arial',16,'bold'),text='opening_stock',bd=16,anchor='w')
lblopening_stock.grid(row=1,column=2)
txtopening_stock=Entry(f1,font=('arial',16,'bold'),textvariable=opening_stock, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txtopening_stock.grid(row=1,column=3)
txtopening_stock.bind('<Return>', enter_opening_stock)
txtopening_stock.bind('<Escape>', escape_opening_stock)

lblreceipts = Label(f1 , font=('arial',16,'bold'),text='receipts',bd=16,anchor='w')
lblreceipts.grid(row=2,column=2)
txtreceipts=Entry(f1,font=('arial',16,'bold'),textvariable=receipts, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txtreceipts.grid(row=2,column=3)
txtreceipts.bind('<Return>', enter_receipts)
txtreceipts.bind('<Escape>', escape_receipts)

lblsale = Label(f1 , font=('arial',16,'bold'),text='sale',bd=16,anchor='w')
lblsale.grid(row=3,column=2)
txtsale=Entry(f1,font=('arial',16,'bold'),textvariable=sale, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txtsale.grid(row=3,column=3)
txtsale.bind('<Return>', enter_sale)
txtsale.bind('<Escape>', escape_sale)

lblissues = Label(f1 , font=('arial',16,'bold'),text='issues',bd=16,anchor='w')
lblissues.grid(row=4,column=2)
txtissues=Entry(f1,font=('arial',16,'bold'),textvariable=issues, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txtissues.grid(row=4,column=3)
txtissues.bind('<Return>', enter_issues)
txtissues.bind('<Escape>', escape_issues)

'''lblpnm = Label(f1 , font=('arial',16,'bold'),text='monthly_sale',bd=16,anchor='w')
lblpnm.grid(row=6,column=2)
txtpnm=Entry(f1,font=('arial',16,'bold'),textvariable=monthly_sale, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txtpnm.grid(row=6,column=3)'''

lblamt_monthly_sale = Label(f1 , font=('arial',16,'bold'),text='amt_monthly_sale',bd=16,anchor='w')
lblamt_monthly_sale.grid(row=5,column=2)
txtamt_monthly_sale=Entry(f1,font=('arial',16,'bold'),textvariable=amt_monthly_sale, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txtamt_monthly_sale.grid(row=5,column=3)
txtamt_monthly_sale.bind('<Return>', enter_amt_monthly_sale)
txtamt_monthly_sale.bind('<Escape>', escape_amt_monthly_sale)









'''
lblcost = Label(f1 , font=('arial',16,'bold'),text='cost',bd=16,anchor='w')
lblcost.grid(row=2,column=0)
txtcost=Entry(f1,font=('arial',16,'bold'),textvariable=cost, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txtcost.grid(row=2,column=1)
#Item[pid]['cost']=cost.get()

'''
###
btnReset=Button(f1,font=('arial',12,'bold'),bd=10,width=10,text='clear',bg='powder blue',command=Reset ).grid(row=9,column=2)
btnEnter=Button(f1,font=('arial',12,'bold'),bd=10,width=10,text='Enter',bg='powder blue',command=lambda :Enter(pid.get(),name.get(),department_no.get(),open_rate.get(),rate1.get(),rate2.get(),tax_rate.get(),opening_stock.get(),receipts.get(),sale.get(),issues.get(),amt_monthly_sale.get()) ).grid(row=9,column=1)

#btnDoit=Button(f1,font=('arial',12,'bold'),bd=10,width=10,text='print',bg='powder blue',command=Doit).grid(row=7,column=3)


root.mainloop()