from tkinter import*
root = Tk()
root.title("When we will do something intresting in pythonnnnnnnnnnnnnnnnNNNNNN")
root.geometry("1000x1000")

label = Label(root)
label1 = Label(root)
label2 = Label(root)

class Pointy:
    def gy():
        label['text'] = "Pointyman"
    def gy2():
        label1['text'] = "Pointyman22"
    def gy3():
        label2['text'] = "Pointyman33"
        
class qwerty(Pointy):
    def gy(self):
        Pointy.gy()
    def gy2(self):
        Pointy.gy2()
    def gy3(self):
        Pointy.gy3()
        
obj1 = qwerty()
btn = Button(root,text = "Man1",command = obj1.gy)
btn2 = Button(root,text = "Man2",command = obj1.gy2)
btn3 = Button(root,text = "Man3",command = obj1.gy3)

btn.pack()
btn2.pack()
btn3.pack()
label.pack()
label1.pack()
label2.pack()

root.mainloop()