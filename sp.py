from Tkinter import* 
import random
import time
import json
import tkMessageBox
import math




root=Tk()
root.geometry("1400x800+0+0")
root.title("Billing system")

Tops = Frame(root,width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=1000,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

r=DoubleVar()
r=0
j=IntVar()
j=0

localtime=time.asctime(time.localtime(time.time()))


Bill={} 
with open('bill.txt','r') as b:
 q1=b.read()
 Bill=json.loads(q1)
Item={} 
with open('string.txt','r') as wf:
 q=wf.read()
 Item=json.loads(q)
txtRec=Text(f1,width=900,height=600,bg='white',bd=8,font=('arial',10,'bold'))
txtRec.grid(row=1,column=0) 
# r=len(Item)
# print(r)
txtRec.insert(END,"\n\n\n\t\t\t\tSTOCK DATA\n\n") 
txtRec.insert(END,"Item Code\t\tItem name\t\tsale\t\tamount\t\tcurrent stock\n")
for j in Item : 
 j=(str)(j)	
 r=(float)(Item[j]['amt_monthly_sale'])
 txtRec.insert(END,(str)(j)+"\t\t"+(str)(Item[j]['name'])+"\t\t"+(str)(Item[j]['sale'])+"\t\t"+(str)(r)+"\t\t"+(str)(Item[j]['current_stock'])+"\n")
txtRec.insert(END,"\n\n\n\t\t\t\tBILL DATA\n\n") 
txtRec.insert(END,"Bill no.\t\t\tDate\t\t\tTotal_Tax\t\tTotal_Amount\t\tFinal_Amount\n")

for j in Bill :
 j=(str)(j)
 if( 'Jul 06' in (str)(Bill[j]['Date']) ) :
  txtRec.insert(END,j+"\t\t\t"+(str)(Bill[j]['Date'])+"\t\t\t"+(str)(Bill[j]['Total_Tax'])+"\t\t"+(str)(Bill[j]['Total_Amount'])+"\t\t"+(str)(Bill[j]['Final_Amount'])+"\n")


root.mainloop()