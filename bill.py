from Tkinter import* 
import random
import time
import json
import tkMessageBox
import  math

root=Tk()
root.geometry("1400x800+0+0")
root.title("Billing system")

Tops = Frame(root,width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=600,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width=400,height=700,relief=SUNKEN)
f2.pack(side=LEFT)

f3 = Frame(root,width=400,height=700,relief=SUNKEN)
f3.pack(side=RIGHT)

 
####time###
localtime=time.asctime(time.localtime(time.time()))

###########info##
lb1 = Label(Tops , font=('arial',30,'bold'), text='Billing System', fg='Steel Blue' , bd=10 , anchor='w')
lb1.grid(row=0,column=0)
lb2 = Label(Tops , font=('arial',20,'bold'), text=localtime, fg='Steel Blue' , bd=10 , anchor='w')
lb2.grid(row=1,column=0)

##############
def Reset():
 wyw.set("")
 hm.set("")
def qExit():
 qExit= tkMessageBox.showinfo("Quit System","Do you want to quit?")
 if (qExit == 'ok') :
  root.destroy()
  #return
Bill_No={} #createc dictionary Bill_No to store the bill number
temp={} # to store the values of list of items along with quantity, temporarily to print
Bill={} # to store the bill details permanently
with open('bill.txt','r') as b:
 q1=b.read()
 Bill=json.loads(q1)
Item={} # it keep the record of all items available in our record
with open('string.txt','r') as wf:
 q=wf.read()
 Item=json.loads(q)
# print(Item)
 def print_detail(a): # to print the deatils of item asked in detail box(txtinfo)
  txtinfo.delete("1.0",END)
  txtinfo.insert(END,'\tName:'+Item[a]['name']+'\n\tRate:'+Item[a]['rate1']+'\n\tAvailable :'+(str)(Item[a]['current_stock']))
 def Total(a,b): # calculating total cost and printing the list in printbox(txtRec)
  if(Item[a]["open_rate"]=="No"):
   x=(float)(Item[a]["rate1"]) 
  else: 
   x=open_rate.get()
  y=x*b 
  global z
  z=z+y ## remaining work here is to take a total variable which will hold the total amount of shopping
  if(b>Item[a]['current_stock']):
   txtinfo.insert(END,"not available \ncurrent stock :"+(str)(Item[a]['current_stock']))
  else:  
   txtRec.insert(END,''+str(Item[a]['name'])+'\t\t\t'+str(b)+'\t\t'+str(x)+'\t'+str(round(y,2))+"  "+str(z)+"\n")
 # def FloatInputCheck(a): # to check if submitted values are float are not
 #  f=True
 #  while(f==True):
 #   if(type(a)==float):
 #    f=False
 #   else: 
 #    hm.set("")
 #    txtinfo.insert(END,"!!!\n\n\t Please insert float value only !!!!")   
 def enter_hm(event): # activity that happens when enter is pressed in Quantity entry box
  try: # to confirm that entered value is float.. as hm.get() is called that value is accesed and it gives error bcz hm is defined as float,, so if u enter any other data type it gives error
   widget=event.widget
   global count_iteration 
   txtinfo.delete("1.0",END)
   a=wyw.get()
   
  #p=(float)(widget.get())
  #FloatInputCheck(hm.get());
   
   Total(wyw.get(),hm.get()) # passing the item code and quantity to total() 
  ### to store item and quantity in temp{} dictionary so that we can print it together
   temp[count_iteration]={} # to count number of items are purchased 
   temp[count_iteration]['pid']=wyw.get()
   temp[count_iteration]['quantity']=hm.get()
   temp[count_iteration]['rate']=open_rate.get()
   count_iteration=count_iteration+1
   #########
   wyw.set("")
   hm.set("")
   open_rate.set("")
  # txtRec.delete((int)(END)-4,END)
   txtwyw.focus()
  except ValueError: 
  	hm.set("")
  	txtinfo.delete("1.0",END)
  	txtinfo.insert(END,"\n\nEnter Numeric value only")
  	txthm.focus()
  
 def enter_wyw(event): #.........activity that happens whe enter key is pressed in item code box
  try:
   widget = event.widget
   p=widget.get()
   print_detail(p)
   #print(Item[p]['open_rate'])
   if(Item[p]['open_rate'] == 'No'):
    open_rate.set(Item[p]['rate1'])
    txtor['state']='readonly'
    txthm.focus()  
   if(Item[p]['open_rate'] == 'Yes'):
    open_rate.set(Item[p]['rate1'])
    txtor['state']='normal' 
    txtor.focus() 
  except KeyError:
   wyw.set("")
   txtinfo.delete("1.0",END)
   txtinfo.insert(END,"Item code does not exists")
   txtwyw.focus()
  

 with open('billno.txt','r') as wf:
   q=wf.read()
   Bill_No=json.loads(q)
  
 #print(Bill_No)


def escape_wyw(event): # when escape pressed it generates the bill 
  widget=event.widget
  global count_iteration
  global bn
  global z
  global ta
  global tt
  global us
  global ucs
  global ab
  global ma
  #print(z)
  #print(Bill_No)
  bn=(int)(Bill_No['no'])
  global j
  #print(temp)
  Bill[bn]={}
  Bill[bn]['Date']=localtime
  Bill[bn]['Products']={}
  Bill[bn]['Total_Tax']={}
  Bill[bn]['Total_Amount']={}
  Bill[bn]['Final_Amount']={}
  #print j
  #print(count_iteration)
  for j in range(0,count_iteration): ## to store the bill .. by copying the list of item purchased from temp{}
   Bill[bn]['Products'][j]={}
   Bill[bn]['Products'][j]['productId']=(temp[j]['pid'])
   ab=(str)(temp[j]['pid'])
   us=(float)(Item[ab]['sale'])
   #ab=(float)(temp[j]['pid'])
   print(ab)
   print(type(us))
   print(type(temp[j]['quantity']))
   Bill[bn]['Products'][j]['quantity']=temp[j]['quantity']
   us=(float)(Item[ab]['sale'])+(float)(temp[j]['quantity'])
   ma=(float)(temp[j]['quantity'])*(float)(temp[j]['rate'])*0.18+(float)(temp[j]['quantity'])*(float)(temp[j]['rate'])
   ma=ma+(float)(Item[ab]['amt_monthly_sale'])
   Item[ab]['amt_monthly_sale']=ma
   Item[ab]['sale']=us	
   ucs=(float)(Item[ab]['current_stock'])-(float)(temp[j]['quantity'])
   Item[ab]['current_stock']=ucs
   Bill[bn]['Products'][j]['rate']=temp[j]['rate']
   Bill[bn]['Products'][j]['Item_Amount']=temp[j]['quantity']*temp[j]['rate']
   Bill[bn]['Products'][j]['tax']=0.18*Bill[bn]['Products'][j]['Item_Amount']
   tt+=Bill[bn]['Products'][j]['tax']
   Bill[bn]['Total_Tax']=tt
   ta+=Bill[bn]['Products'][j]['Item_Amount']
   Bill[bn]['Total_Amount']=ta
   Bill[bn]['Final_Amount']=ta+tt
  with open('Bill.txt','w') as wtf:
   txt=json.dumps(Bill)
   wtf.write(txt)                # storing the bill records into Bill.txt 
  
  bn=bn+1
  Bill_No['no']=bn               # storing the bill number in the dictionary
  with open('billno.txt','w') as wtf:
   txt=json.dumps(Bill_No)
   wtf.write(txt)               # incrasing the bill number and storing it in billno.txt
  with open('string.txt','w') as wtff:
   txt=json.dumps(Item)
   wtff.write(txt)               # incrasing the bill number and storing it in billno.txt

  txtRec.insert(END,"\n\t\t\tTotal:")  ## printing bill 
  txtRec.insert(END,z)
  sgst=cgst=(0.09*z)
  z=z+sgst+cgst
  txtRec.insert(END,"\n\t\t\tSGST(9%):")
  txtRec.insert(END, round(sgst,2))   #  math.ceil() to get rounded off values
  txtRec.insert(END,"\n\t\t\tCGST(9%):")
  txtRec.insert(END, round(cgst,2))
  txtRec.insert(END,"\n\t\t\tGrand Total:")
  txtRec.insert(END, round(z,2))
  txtRec['state']='disabled'
def escape_hm(event):
 widget=event.widget
 #print(widget.get())
 txtwyw.focus()
 wyw.set("")

def enter_or(event):
 try:
  widget=event.widget
  r=open_rate.get()
  txthm.focus() 
 except ValueError:
  open_rate.set("")
  txtinfo.delete("1.0",END)
  txtinfo.insert(END,"\n\nEnter Numeric value only")
  txtor.focus()
 
def escape_or(event):
 open_rate.set("")
 txtor.focus()

rand= StringVar()
wyw=StringVar()
hm=DoubleVar()
x=DoubleVar()
y=DoubleVar()
p=StringVar()
q=DoubleVar()
r=DoubleVar()
s=DoubleVar()
z=DoubleVar()
tt=DoubleVar()
tt=0
ta=DoubleVar()
ta=0
z=0
us=DoubleVar()
us=0
sgst=DoubleVar()
cgst=DoubleVar()
bn=IntVar()
bn=1
j=DoubleVar()
j=1
ma=DoubleVar()
ma=0
ucs=DoubleVar()
ucs=0
open_rate=DoubleVar()
count_iteration=IntVar()
count_iteration=0
operator_id=StringVar()
ab=StringVar()


lblwyw = Label(f1 , font=('arial',16,'bold'),text='Item Code:',bd=16,anchor='w')
lblwyw.grid(row=1,column=0)
txtwyw=Entry(f1,font=('arial',16,'bold'),textvariable=wyw, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txtwyw.focus()
txtwyw.bind('<Return>', enter_wyw)
txtwyw.bind('<Escape>', escape_wyw)
txtwyw.grid(row=1,column=1)
wyw.set("")

lblor = Label(f1 , font=('arial',16,'bold'),text='Rate:',bd=16,anchor='w')
lblor.grid(row=2,column=0)
txtor=Entry(f1,font=('arial',16,'bold'),textvariable=open_rate, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txtor.bind('<Return>',enter_or)
txtor.bind('<Escape>', escape_or)
txtor.grid(row=2,column=1)
open_rate.set("")

lblhm = Label(f1 , font=('arial',16,'bold'),text='Quantity:',bd=16,anchor='w')
lblhm.grid(row=3,column=0)
txthm=Entry(f1,font=('arial',16,'bold'),textvariable=hm, bd=10 ,insertwidth=4 ,bg='powder blue', justify ='right')
txthm.bind('<Return>',enter_hm)
txthm.bind('<Escape>', escape_hm)
txthm.grid(row=3,column=1)
hm.set("")

###
txtinfo=Text(f2,width=35,height=15,bg='white',bd=8,font=('arial',10,'bold'))
txtinfo.grid(row=0,column=0,padx=14)

######receipt####
lblRec= Label(f3,font=('arial',12,'bold'),text='RECEIPT:', bd=2 ,anchor ='w')
lblRec.grid(row=0,column=0,sticky='w')
txtRec=Text(f3,width=59,height=22,bg='white',bd=8,font=('arial',10,'bold'))
txtRec.grid(row=1,column=0)
txtRec.insert(END,"\t\tMANGAL GENERAL STORE\n\t102,Rajtarang building-A,Dahisar(E),mum-400068.\n\t\t\tcontact:9819319419\n_ _ _ _ _ _")
txtRec.insert(END,"\noperator\t\tBill No.:")
txtRec.insert(END,Bill_No['no'])
txtRec.insert(END,'\t'+localtime+"\n_ _ _ _ _ _\n")
txtRec.insert(END,"Product\t\t\tQuantity\t\trate\tcost\n")
########button##########
#btnTotal = Button(f1,text='Total',font=('arial',12,'bold'),padx=4,pady=1,fg='black', anchor='w',command=lambda:Total(wyw.get(),hm.get())).grid(row=7,column=0)
btnReceipt = Button(f1,text='Receipt',font=('arial',12,'bold'),padx=4,pady=1,fg='black', anchor='w').grid(row=7,column=1)
btnExit = Button(f1,text='Exit',font=('arial',12,'bold'),padx=4,pady=1,fg='black', anchor='w',command=qExit).grid(row=7,column=2)


root.mainloop()