from tkinter import *
from tkinter import messagebox
root=Tk()
root.configure(background="lightgoldenrodyellow")
c=Canvas(root,bg='lightgoldenrodyellow')
c.grid(row=0,column=0)
img=PhotoImage(file='elephant.png')
c.create_image(0,0,image=img,anchor=NW)
c1=Canvas(root,bg='lightgoldenrodyellow')
c1.grid(row=0,column=1)
img2=PhotoImage(file='dog.png')
c1.create_image(0,0,image=img2,anchor=NW)
c2=Canvas(root,bg='lightgoldenrodyellow')
c2.grid(row=1,column=0)
img3=PhotoImage(file='donkey.png')
c2.create_image(0,0,image=img3,anchor=NW)
c3=Canvas(root,bg='lightgoldenrodyellow')
c3.grid(row=1,column=1)
img4=PhotoImage(file='giraffe.png')
c3.create_image(0,0,image=img4,anchor=NW)
def cc1():
    c4=Canvas(root,bg='lightgoldenrodyellow')
    c4.grid(row=1,column=1)
    img24=PhotoImage(file='giraffe.png')
    ot=c4.create_image(0,0,image=img24,anchor=NW)
    new=PhotoImage(file="giraffe.png")
    c4.itemconfig(ot,image=new)
    o=c4.create_image(0,0,image=new,anchor=NW)
    c4.image=new
def cc2():
             c=Canvas(root,bg='lightgoldenrodyellow')
             c.grid(row=0,column=0)
             img=PhotoImage(file='elephant.png')
             f=c.create_image(0,0,image=img3,anchor=NW)
             new=PhotoImage(file="elephant.png")
             c.itemconfig(f,image=new)
             f=c.create_image(0,0,image=new,anchor=NW)
             c.image=new
def cc3():
             c1=Canvas(root,bg='lightgoldenrodyellow')
             c1.grid(row=0,column=1)
             img2=PhotoImage(file='dog.png')
             o=c1.create_image(0,0,image=img2,anchor=NW)
             new=PhotoImage(file="dog.png")
             c1.itemconfig(o,image=new)
             o=c1.create_image(0,0,image=new,anchor=NW)
             c1.image=new
def cc4():
             c2=Canvas(root,bg='lightgoldenrodyellow')
             c2.grid(row=1,column=0)
             img3=PhotoImage(file='donkey.png')
             f=c2.create_image(0,0,image=img3,anchor=NW)
             new=PhotoImage(file="donkey.png")
             c2.itemconfig(f,image=new)
             f=c2.create_image(0,0,image=new,anchor=NW)
             c2.image=new
def cli():
    if((i.get()+p.get()+k.get()+l.get()+m.get()+n.get()+O.get()+L.get()+K.get()+V.get())!=4):
        messagebox.showinfo("TRY AGAIN"," SELECT 4 OPTION")
    else:
        bu.configure(state=DISABLED)
        bu1.configure(state=DISABLED)
        bu7.configure(state=DISABLED)        
        bu4.configure(state=DISABLED)
        bu5.configure(state=DISABLED)
        bu6.configure(state=DISABLED)
        bu8.configure(state=DISABLED)
        bu9.configure(state=DISABLED)
        bu10.configure(state=DISABLED)
        bu11.configure(state=DISABLED)
        print(i.get(),p.get(),k.get(),l.get())
        if((i.get()+p.get()+k.get()+l.get())==4):
            Label(root,text="CORRECT GUESS 4").grid(row=2,column=5)
            fh=open("hello.txt","a")
            fh.write("FIRST CORRECT GUESS 4")
            fh.close()
        if((i.get()+p.get()+k.get()+l.get())==3):
            Label(root,text="CORRECT GUESS 3").grid(row=2,column=5)
            fh=open("hello.txt","a")
            fh.write("\nFIRST CORRECT GUESS 3")
            fh.close()
            if(i.get()>(p.get())):
                cc4()
                """donkey"""

            if(l.get()>i.get()):
                cc3()
                """dog"""
 
            if(k.get()>(l.get())):
                cc2()
                """elephant"""

            if(k.get()==0):
                cc1()
                """giraffe"""

        if((i.get()+p.get()+k.get()+l.get())==2):
            Label(root,text="CORRECT GUESS 2").grid(row=2,column=5)
            fh=open("hello.txt","a")
            fh.write("\nFIRST CORRECT GUESS 2")
            fh.close()
            if(i.get()==0):
                cc3()

            if(p.get()==0):
                cc4()

            if(k.get()==0):
                cc1()
            if(l.get()==0):
                
                 cc2()
            
        if((i.get()+p.get()+k.get()+l.get())==1):
             Label(root,text="CORRECT GUESS 1").grid(row=2,column=5)
             fh=open("hello.txt","a")
             fh.write("\nFIRST CORRECT GUESS 1")
             fh.close()
             if(i.get()==1):
                 cc2()
                 cc1()
                 cc4()
             if(p.get()==1):
                 cc2()
                 cc3()
                 cc1()
             if(l.get()==1):
                 cc1()
                 cc3()
                 cc4()
             if(k.get()==1):
                 cc2()
                 cc3()
                 cc4()
                
                
                     
                     

                    
        if((i.get()+p.get()+k.get()+l.get())==0):
             Label(root,text="CORRECT GUESS 0").grid(row=2,column=5)
             fh=open("hello.txt","a")
             fh.write("\nFIRST CORRECT GUESS 0")
             fh.close()
             cc1()
             cc2()
             cc3()
             cc4()
             

    
    
                                    


        
def clear():
    bu.configure(state=NORMAL)
    bu1.configure(state=NORMAL)
    bu7.configure(state=NORMAL)        
    bu4.configure(state=NORMAL)
    bu5.configure(state=NORMAL)
    bu6.configure(state=NORMAL)
    bu8.configure(state=NORMAL)
    bu9.configure(state=NORMAL)
    bu10.configure(state=NORMAL)
    bu11.configure(state=NORMAL)
        
    c=Canvas(root,bg='lightgoldenrodyellow')
    c.grid(row=0,column=0)
    img=PhotoImage(file='elephant.png')
    q=c.create_image(0,0,image=img,anchor=NW)
    c1=Canvas(root,bg='lightgoldenrodyellow')
    c1.grid(row=0,column=1)
    img2=PhotoImage(file='dog.png')
    t=c1.create_image(0,0,image=img2,anchor=NW)
    c2=Canvas(root,bg='lightgoldenrodyellow')
    c2.grid(row=1,column=0)
    img3=PhotoImage(file='donkey.png')
    p=c2.create_image(0,0,image=img3,anchor=NW)
    c3=Canvas(root,bg='lightgoldenrodyellow')
    c3.grid(row=1,column=1)
    img4=PhotoImage(file='giraffe.png')
    r=c3.create_image(0,0,image=img4,anchor=NW)
    new=PhotoImage(file="questionmark.png")
    c3.itemconfig(r,image=new)
    r=c3.create_image(0,0,image=new,anchor=NW)
    c3.image=new
    c2.itemconfig(r,image=new)
    p=c2.create_image(0,0,image=new,anchor=NW)
    c2.image=new
    c1.itemconfig(r,image=new)
    t=c1.create_image(0,0,image=new,anchor=NW)
    c1.image=new
    c.itemconfig(r,image=new)
    q=c.create_image(0,0,image=new,anchor=NW)
    c.image=new
def again():
    back=Button(root,text='   RESET  ',command=again).grid(row=3,column=1)
    root.configure(background="lightgoldenrodyellow")
    Label(root,text=" H ").grid(row=2,column=4)
    Label(root,text=" H ").grid(row=4,column=4)
    Label(root,text=" H ").grid(row=3,column=4)
    
    c=Canvas(root,bg='lightgoldenrodyellow')
    c.grid(row=0,column=0)
    img=PhotoImage(file='grapefruit.png')
    c.create_image(0,0,image=img,anchor=NW)
    c1=Canvas(root,bg='lightgoldenrodyellow')
    c1.grid(row=0,column=1)
    img2=PhotoImage(file='lemon.png')
    c1.create_image(0,0,image=img2,anchor=NW)
    c2=Canvas(root,bg='lightgoldenrodyellow')
    c2.grid(row=1,column=0)
    img3=PhotoImage(file='kiwi.png')
    c2.create_image(0,0,image=img3,anchor=NW)
    c3=Canvas(root,bg='lightgoldenrodyellow')
    c3.grid(row=1,column=1)
    img4=PhotoImage(file='coconut.png')
    c3.create_image(0,0,image=img4,anchor=NW)
    def cc12():
        
        c4=Canvas(root,bg='lightgoldenrodyellow')
        c4.grid(row=0,column=0)
        img24=PhotoImage(file='grapefruit.png')
        ot=c4.create_image(0,0,image=img24,anchor=NW)
        new=PhotoImage(file="grapefruit.png")
        c4.itemconfig(ot,image=new)
        o=c4.create_image(0,0,image=new,anchor=NW)
        c4.image=new
    
    def cc22():
        
                 c=Canvas(root,bg='lightgoldenrodyellow')
                 c.grid(row=1,column=0)
                 img=PhotoImage(file='kiwi.png')
                 f=c.create_image(0,0,image=img3,anchor=NW)
                 new=PhotoImage(file="kiwi.png")
                 c.itemconfig(f,image=new)
                 f=c.create_image(0,0,image=new,anchor=NW)
                 c.image=new
    def cc32():
             c1=Canvas(root,bg='lightgoldenrodyellow')
             c1.grid(row=1,column=1)
             img2=PhotoImage(file='coconut.png')
             o=c1.create_image(0,0,image=img2,anchor=NW)
             new=PhotoImage(file="coconut.png")
             c1.itemconfig(o,image=new)
             o=c1.create_image(0,0,image=new,anchor=NW)
             c1.image=new
    def cc42():
             c2=Canvas(root,bg='lightgoldenrodyellow')
             c2.grid(row=0,column=1)
             img3=PhotoImage(file='lemon.png')
             f=c2.create_image(0,0,image=img3,anchor=NW)
             new=PhotoImage(file="lemon.png")
             c2.itemconfig(f,image=new)
             f=c2.create_image(0,0,image=new,anchor=NW)
             c2.image=new
    def cli1():
        if((ii.get()+pp.get()+kk.get()+ll.get()+mm.get()+nn.get()+OO.get()+LL.get()+KK.get()+VV.get())!=4):
            messagebox.showinfo("TRY AGAIN"," SELECT 4 OPTION")
        else:
            buz.configure(state=DISABLED)
            buz1.configure(state=DISABLED)
            buz7.configure(state=DISABLED)        
            buz4.configure(state=DISABLED)
            buz5.configure(state=DISABLED)
            buz6.configure(state=DISABLED)
            buz8.configure(state=DISABLED)
            buz9.configure(state=DISABLED)
            buz10.configure(state=DISABLED)
            buz11.configure(state=DISABLED)
            print(ii.get(),pp.get(),kk.get(),ll.get())
            """if((ii.get()+pp.get()+kk.get()+ll.get())==4):                                                     
                Label(root,text="CORRECT GUESS 4").grid(row=3,column=5)
            if((ii.get()+pp.get()+kk.get()+ll.get())==3):
                Label(root,text="CORRECT GUESS 3").grid(row=3,column=5)
            if((ii.get()+pp.get()+kk.get()+ll.get())==2):
                Label(root,text="CORRECT GUESS 2").grid(row=3,column=5)
            if((ii.get()+pp.get()+kk.get()+ll.get())==1):
                Label(root,text="CORRECT GUESS 1").grid(row=3,column=5)
            if((ii.get()+pp.get()+kk.get()+ll.get())==0):
                Label(root,text="CORRECT GUESS 0").grid(row=3,column=5)
            Label(root,text="NR").grid(row=3,column=4)"""
            if((ii.get()+pp.get()+kk.get()+ll.get())==4):
                
                Label(root,text="CORRECT GUESS 4").grid(row=3,column=5)
                fh=open("hello.txt","a")
                fh.write("\nSECOND CORRECT GUESS 4")
                fh.close()
            if((ii.get()+pp.get()+kk.get()+ll.get())==3):
                Label(root,text="CORRECT GUESS 3").grid(row=3,column=5)
                fh=open("hello.txt","a")
                fh.write("\nSECOND CORRECT GUESS 3")
                fh.close()
                if(ii.get()>(pp.get())):
                    cc42()
                    """donkey"""

                if(ll.get()>ii.get()):
                    cc32()
                    """dog"""
     
                if(kk.get()>(ll.get())):
                    cc22()
                    """elephant"""

                if(kk.get()==0):
                    cc12()
                    """giraffe"""

            if((ii.get()+pp.get()+kk.get()+ll.get())==2):
                Label(root,text="CORRECT GUESS 2").grid(row=3,column=5)
                fh=open("hello.txt","a")
                fh.write("\nSECOND CORRECT GUESS 2")
                fh.close()
                
                if(ii.get()==0):
                    cc32()

                if(pp.get()==0):
                    cc42()

                if(kk.get()==0):
                    cc12()
                if(ll.get()==0):
                    
                     cc22()
                
            if((ii.get()+pp.get()+kk.get()+ll.get())==1):
                 Label(root,text="CORRECT GUESS 1").grid(row=3,column=5)
                 fh=open("hello.txt","a")
                 fh.write("\nSECOND CORRECT GUESS 1")
                 fh.close()
                 if(ii.get()==1):
                     cc22()
                     cc12()
                     cc42()
                 if(pp.get()==1):
                     cc22()
                     cc32()
                     cc12()
                 if(ll.get()==1):
                     cc12()
                     cc32()
                     cc42()
                 if(kk.get()==1):
                     cc22()
                     cc32()
                     cc42()
                    
                    
                         
                         

                        
            if((ii.get()+pp.get()+kk.get()+ll.get())==0):
                 Label(root,text="CORRECT GUESS 0").grid(row=3,column=5)
                 fh=open("hello.txt","a")
                 fh.write("\nSECOND CORRECT GUESS 0")
                 fh.close()
                 cc12()
                 cc22()
                 cc32()
                 cc42()
            Label(root,text="NR").grid(row=3,column=4)



        
    def clear1():
        buz.configure(state=NORMAL)
        buz1.configure(state=NORMAL)
        buz7.configure(state=NORMAL)        
        buz4.configure(state=NORMAL)
        buz5.configure(state=NORMAL)
        buz6.configure(state=NORMAL)
        buz8.configure(state=NORMAL)
        buz9.configure(state=NORMAL)
        buz10.configure(state=NORMAL)
        buz11.configure(state=NORMAL)
        c=Canvas(root,bg='lightgoldenrodyellow')
        c.grid(row=0,column=0)
        img=PhotoImage(file='grapefruit.png')
        q=c.create_image(0,0,image=img,anchor=NW)
        c1=Canvas(root,bg='lightgoldenrodyellow')
        c1.grid(row=0,column=1)
        img2=PhotoImage(file='lemon.png')
        t=c1.create_image(0,0,image=img2,anchor=NW)
        c2=Canvas(root,bg='lightgoldenrodyellow')
        c2.grid(row=1,column=0)
        img3=PhotoImage(file='kiwi.png')
        p=c2.create_image(0,0,image=img3,anchor=NW)
        c3=Canvas(root,bg='lightgoldenrodyellow')
        c3.grid(row=1,column=1)
        img4=PhotoImage(file='coconut.png')
        r=c3.create_image(0,0,image=img4,anchor=NW)
        new=PhotoImage(file="questionmark.png")
        c3.itemconfig(r,image=new)
        r=c3.create_image(0,0,image=new,anchor=NW)
        c3.image=new
        c2.itemconfig(r,image=new)
        p=c2.create_image(0,0,image=new,anchor=NW)
        c2.image=new
        c1.itemconfig(r,image=new)
        t=c1.create_image(0,0,image=new,anchor=NW)
        c1.image=new
        c.itemconfig(r,image=new)
        q=c.create_image(0,0,image=new,anchor=NW)
        c.image=new

    
    ii=IntVar()
    pp=IntVar()
    kk=IntVar()
    ll=IntVar()
    mm=IntVar()
    nn=IntVar()
    OO=IntVar()
    LL=IntVar()
    KK=IntVar()
    VV=IntVar()

    buz=Checkbutton(root,text='COCONUT',fg='black',variable=ii,state=DISABLED,bg='white')
    buz.grid(row=0,column=8)
    buz1=Checkbutton(root,text='LEMON',fg='black',variable=pp,state=DISABLED,bg='white')
    buz1.grid(row=0,column=5)
    buz4=Checkbutton(root,text='MANGO',fg='black',variable=mm,state=DISABLED,bg='white')
    buz4.grid(row=0,column=6)
    buz5=Checkbutton(root,text='KIWI',fg='black',variable=ll,state=DISABLED,bg='white',width="8")
    buz5.grid(row=1,column=4)
    buz6=Checkbutton(root,text='GRAPEFRUIT',fg='black',variable=kk,state=DISABLED,bg='white')
    buz6.grid(row=1,column=7)
    buz7=Checkbutton(root,text='PINEAPPLE',fg='black',variable=nn,state=DISABLED,bg='white')
    buz7.grid(row=1,column=6)
    buz8=Checkbutton(root,text='STRAWBERRY',fg='black',variable=OO,state=DISABLED,bg='white')
    buz8.grid(row=0,column=7)
    buz9=Checkbutton(root,text='LITCHI',fg='black',variable=LL,state=DISABLED,bg='white')
    buz9.grid(row=0,column=4)
    buz10=Checkbutton(root,text='   BERRY    ',fg='black',state=DISABLED,variable=KK,bg='white')
    buz10.grid(row=1,column=5)
    buz11=Checkbutton(root,text='WATERMALEN',fg='black',state=DISABLED,variable=VV,bg='white')
    buz11.grid(row=1,column=8)
    buz3=Button(root,text='SUBMIT',command=cli1,fg='black',bg='white')
    buz3.grid(row=1,column=10)
    ok1=Button(root,text='Ok',command=clear1,bg='white').grid(row=1,column=11)
    refresh1=Button(root,text='Refresh',command=again2).grid(row=2,column=1)
    root.mainloop()    
def again2():
    root.configure(background="lightgoldenrodyellow")
    Label(root,text=" H ").grid(row=3,column=4)
    c=Canvas(root,bg='lightgoldenrodyellow')
    c.grid(row=0,column=0)
    img=PhotoImage(file='cards.png')
    c.create_image(0,0,image=img,anchor=NW)
    c1=Canvas(root,bg='lightgoldenrodyellow')
    c1.grid(row=0,column=1)
    img2=PhotoImage(file='dice.png')
    c1.create_image(0,0,image=img2,anchor=NW)
    c2=Canvas(root,bg='lightgoldenrodyellow')
    c2.grid(row=1,column=0)
    img3=PhotoImage(file='bell.png')
    c2.create_image(0,0,image=img3,anchor=NW)
    c3=Canvas(root,bg='lightgoldenrodyellow')
    c3.grid(row=1,column=1)
    img4=PhotoImage(file='candle.png')
    c3.create_image(0,0,image=img4,anchor=NW)
    def cc121():
        
        
        c4=Canvas(root,bg='lightgoldenrodyellow')
        c4.grid(row=0,column=0)
        img24=PhotoImage(file='dice.png')
        ot=c4.create_image(0,0,image=img24,anchor=NW)
        new=PhotoImage(file="dice.png")
        c4.itemconfig(ot,image=new)
        o=c4.create_image(0,0,image=new,anchor=NW)
        c4.image=new
    
    def cc221():
        
                 c=Canvas(root,bg='lightgoldenrodyellow')
                 c.grid(row=1,column=0)
                 img=PhotoImage(file='cards.png')
                 f=c.create_image(0,0,image=img3,anchor=NW)
                 new=PhotoImage(file="cards.png")
                 c.itemconfig(f,image=new)
                 f=c.create_image(0,0,image=new,anchor=NW)
                 c.image=new
    def cc321():
             c1=Canvas(root,bg='lightgoldenrodyellow')
             c1.grid(row=1,column=1)
             img2=PhotoImage(file='candle.png')
             o=c1.create_image(0,0,image=img2,anchor=NW)
             new=PhotoImage(file="candle.png")
             c1.itemconfig(o,image=new)
             o=c1.create_image(0,0,image=new,anchor=NW)
             c1.image=new
    def cc421():
             c2=Canvas(root,bg='lightgoldenrodyellow')
             c2.grid(row=0,column=1)
             img3=PhotoImage(file='bell.png')
             f=c2.create_image(0,0,image=img3,anchor=NW)
             new=PhotoImage(file="bell.png")
             c2.itemconfig(f,image=new)
             f=c2.create_image(0,0,image=new,anchor=NW)
             c2.image=new
    def cli21():
        if((ii.get()+pp.get()+kk.get()+ll.get()+mm.get()+nn.get()+OO.get()+LL.get()+KK.get()+VV.get())!=4):
            messagebox.showinfo("TRY AGAIN"," SELECT 4 OPTION")
        else:
            buz.configure(state=DISABLED)
            buz1.configure(state=DISABLED)
            buz7.configure(state=DISABLED)        
            buz4.configure(state=DISABLED)
            buz5.configure(state=DISABLED)
            buz6.configure(state=DISABLED)
            buz8.configure(state=DISABLED)
            buz9.configure(state=DISABLED)
            buz10.configure(state=DISABLED)
            buz11.configure(state=DISABLED)
            print(ii.get(),pp.get(),kk.get(),ll.get())
            """if((ii.get()+pp.get()+kk.get()+ll.get())==4):                                                     
                Label(root,text="CORRECT GUESS 4").grid(row=4,column=5)
            if((ii.get()+pp.get()+kk.get()+ll.get())==3):
                Label(root,text="CORRECT GUESS 3").grid(row=4,column=5)
            if((ii.get()+pp.get()+kk.get()+ll.get())==2):
                Label(root,text="CORRECT GUESS 2").grid(row=4,column=5)
            if((ii.get()+pp.get()+kk.get()+ll.get())==1):
                Label(root,text="CORRECT GUESS 1").grid(row=4,column=5)
            if((ii.get()+pp.get()+kk.get()+ll.get())==0):
                Label(root,text="CORRECT GUESS 0").grid(row=4,column=5)"""
            Label(root,text="NR").grid(row=4,column=4)
            if((ii.get()+pp.get()+kk.get()+ll.get())==4):
                Label(root,text="CORRECT GUESS 4").grid(row=4,column=5)
                fh=open("hello.txt","a")
                fh.write("\nTHIRD CORRECT GUESS 4")
                fh.close()
            if((ii.get()+pp.get()+kk.get()+ll.get())==3):
                Label(root,text="CORRECT GUESS 3").grid(row=4,column=5)
                fh=open("hello.txt","a")
                fh.write("\nTHIRD CORRECT GUESS 3")
                fh.close()
                if(ii.get()>(pp.get())):
                    cc421()
                    """bellpp"""

                if(ll.get()>ii.get()):
                    cc121()
                    """diceii"""
             
                if(kk.get()>(ll.get())):
                    cc221()
                    """cardsll"""

                if(kk.get()==0):
                    cc321()
                    """candlekk"""
                            

            if((ii.get()+pp.get()+kk.get()+ll.get())==2):
                        Label(root,text="CORRECT GUESS 2").grid(row=4,column=5)
                        fh=open("hello.txt","a")
                        fh.write("\nTHIRD CORRECT GUESS 2")
                        fh.close()
                        if(ii.get()==0):
                            cc121()

                        if(pp.get()==0):
                            cc421()

                        if(kk.get()==0):
                            cc321()
                        if(ll.get()==0):
                            
                             cc221()
                    
            if((ii.get()+pp.get()+kk.get()+ll.get())==1):
                     Label(root,text="CORRECT GUESS 1").grid(row=4,column=5)
                     fh=open("hello.txt","a")
                     fh.write("\nTHIRD CORRECT GUESS 1")
                     fh.close()
                     if(ii.get()==1):
                         cc221()
                         cc321()
                         cc421()
                     if(pp.get()==1):
                         cc221()
                         cc321()
                         cc121()
                     if(ll.get()==1):
                         cc221()
                         cc321()
                         cc421()
                     if(kk.get()==1):
                         cc221()
                         cc121()
                         cc421()
                        
                        
                             
                             

                            
            if((ii.get()+pp.get()+kk.get()+ll.get())==0):
                     Label(root,text="CORRECT GUESS 0").grid(row=4,column=5)
                     fh=open("hello.txt","a")
                     fh.write("\nTHIRD CORRECT GUESS 0")
                     fh.close()
                     cc121()
                     cc221()
                     cc321()
                     cc421()
            


        
    def clear12():
        buz.configure(state=NORMAL)
        buz1.configure(state=NORMAL)
        buz7.configure(state=NORMAL)        
        buz4.configure(state=NORMAL)
        buz5.configure(state=NORMAL)
        buz6.configure(state=NORMAL)
        buz8.configure(state=NORMAL)
        buz9.configure(state=NORMAL)
        buz10.configure(state=NORMAL)
        buz11.configure(state=NORMAL)
        c=Canvas(root,bg='lightgoldenrodyellow')
        c.grid(row=0,column=0)
        img=PhotoImage(file='dice.png')
        q=c.create_image(0,0,image=img,anchor=NW)
        c1=Canvas(root,bg='lightgoldenrodyellow')
        c1.grid(row=0,column=1)
        img2=PhotoImage(file='bell.png')
        t=c1.create_image(0,0,image=img2,anchor=NW)
        c2=Canvas(root,bg='lightgoldenrodyellow')
        c2.grid(row=1,column=0)
        img3=PhotoImage(file='cards.png')
        p=c2.create_image(0,0,image=img3,anchor=NW)
        c3=Canvas(root,bg='lightgoldenrodyellow')
        c3.grid(row=1,column=1)
        img4=PhotoImage(file='candle.png')
        r=c3.create_image(0,0,image=img4,anchor=NW)
        new=PhotoImage(file="questionmark.png")
        c3.itemconfig(r,image=new)
        r=c3.create_image(0,0,image=new,anchor=NW)
        c3.image=new
        c2.itemconfig(r,image=new)
        p=c2.create_image(0,0,image=new,anchor=NW)
        c2.image=new
        c1.itemconfig(r,image=new)
        t=c1.create_image(0,0,image=new,anchor=NW)
        c1.image=new
        c.itemconfig(r,image=new)
        q=c.create_image(0,0,image=new,anchor=NW)
        c.image=new

    
    ii=IntVar()
    pp=IntVar()
    kk=IntVar()
    ll=IntVar()
    mm=IntVar()
    nn=IntVar()
    OO=IntVar()
    LL=IntVar()
    KK=IntVar()
    VV=IntVar()

    buz=Checkbutton(root,text='     DICE    ',fg='black',variable=ii,state=DISABLED,bg='white')
    buz.grid(row=0,column=8)
    buz1=Checkbutton(root,text='   BELL   ',fg='black',variable=pp,state=DISABLED,bg='white')
    buz1.grid(row=0,column=5)
    buz4=Checkbutton(root,text='MANGO',fg='black',variable=mm,state=DISABLED,bg='white')
    buz4.grid(row=0,column=6)
    buz5=Checkbutton(root,text='CARDS',fg='black',variable=ll,state=DISABLED,bg='white',width="8")
    buz5.grid(row=1,column=4)
    buz6=Checkbutton(root,text='    CANDLE ',fg='black',variable=kk,state=DISABLED,bg='white')
    buz6.grid(row=1,column=7)
    buz7=Checkbutton(root,text='PINEAPPLE',fg='black',variable=nn,state=DISABLED,bg='white')
    buz7.grid(row=1,column=6)
    buz8=Checkbutton(root,text='STRAWBERRY',fg='black',variable=OO,state=DISABLED,bg='white')
    buz8.grid(row=0,column=7)
    buz9=Checkbutton(root,text='LITCHI',fg='black',variable=LL,state=DISABLED,bg='white')
    buz9.grid(row=0,column=4)
    buz10=Checkbutton(root,text='   BERRY    ',fg='black',state=DISABLED,variable=KK,bg='white')
    buz10.grid(row=1,column=5)
    buz11=Checkbutton(root,text='WATERMALEN',fg='black',state=DISABLED,variable=VV,bg='white')
    buz11.grid(row=1,column=8)
    buz3=Button(root,text='SUBMIT',command=cli21,fg='black',bg='white')
    buz3.grid(row=1,column=10)
    ok1=Button(root,text='Ok',command=clear12,bg='white').grid(row=1,column=11)
    refresh1=Button(root,text='Refresh',command=again2).grid(row=2,column=1)
    back=Button(root,text='Previous',command=again).grid(row=3,column=1)
    root.mainloop()    

    
i=IntVar()
p=IntVar()
k=IntVar()
l=IntVar()
m=IntVar()
n=IntVar()
O=IntVar()
L=IntVar()
K=IntVar()
V=IntVar()
bu=Checkbutton(root,text='DOG',fg='orange',state=DISABLED,variable=i)
bu.grid(row=0,column=7)
bu1=Checkbutton(root,text='DONKEY',fg='orange',state=DISABLED,variable=p)
bu1.grid(row=0,column=5)
bu4=Checkbutton(root,text='LION',fg='orange',state=DISABLED,variable=m)
bu4.grid(row=0,column=6)
bu5=Checkbutton(root,text='ELEPHENT',fg='orange',state=DISABLED,variable=l)
bu5.grid(row=1,column=4)
bu6=Checkbutton(root,text='GIRAFFE',fg='orange',state=DISABLED,variable=k)
bu6.grid(row=1,column=8)
bu7=Checkbutton(root,text='PEACOCK',fg='orange',state=DISABLED,variable=n)
bu7.grid(row=1,column=6)
bu8=Checkbutton(root,text='COW',fg='orange',state=DISABLED,variable=O)
bu8.grid(row=0,column=4)
bu9=Checkbutton(root,text='GOAT',fg='orange',state=DISABLED,variable=L)
bu9.grid(row=0,column=8)
bu10=Checkbutton(root,text='BEAR',fg='orange',state=DISABLED,variable=K)
bu10.grid(row=1,column=7)
bu11=Checkbutton(root,text='PANTHER',fg='orange',state=DISABLED,variable=V)
bu11.grid(row=1,column=5)
bu3=Button(root,text='SUBMIT',command=cli,fg='orange')
bu3.grid(row=1,column=10)
ok=Button(root,text='Ok',command=clear).grid(row=1,column=11)
refresh=Button(root,text='Refresh',command=again).grid(row=2,column=1)
Label(root,text='NR means NEW RESULT').grid(row=5,column=0)
Label(root,text='H means HISTORY').grid(row=6,column=0)
Label(root,text='FIRST PRESS OK BUTTON').grid(row=4,column=0)
root.mainloop()
