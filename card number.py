from tkinter import *
#print("Enter card Number")
#n = int(input())


class cardNumber:
    def check(self,label,n):
        a=[]
        s=0
        
        #print("you card No.=",n)
        while(n > 0):
            r = n%10
            n = int(n/10)
            a.append(r)
        a.reverse()
        if len(a)<16:
            #print('it is not a card Number')
            label.config(text="invalied card number")
            return
        for i in range(len(a)):
            if i%2==0:
                if 2*a[i]>9:
                    z=2*a[i]
                    r=z%10
                    q=z//10
                    s=s+(r+q)
                else:
                    s=s+2*(a[i])
            else:
                s=s+a[i]
        if s%10==0:
            #print("valied card number")
            label.config(text="valied card number")
        else:
            #print("invalied card number")
            label.config(text="invalied card number")

      
root = Tk()
root.title("Card Number")
root.geometry("400x200")
root.maxsize(400,200)
root.minsize(375,175)
n = IntVar()
c = cardNumber()
label = Label(root,font="15",text="Enter your card Number").pack(pady=10)
entry = Entry(root,textvariable=n,validate='key', width=40,borderwidth=4).pack(pady=20)
l1 = Label(root,text="")

Button(root,text="check",command=lambda :c.check(l1,n.get())).pack()
l1.pack(pady=5)

root.mainloop()
