from tkinter import *

from PIL import ImageTk, Image

root = Tk()

root.title("GCS Calculator 1.0 - Dr Hrishikesh Sarkar")
root.geometry("660x350")

label1 = Label(root, text="This is a Glasgow Coma Scale Calculator")
label2 = Label(root, text="Click on the value as below!")
labela = Label(root, text="Assessment of Motor response")
labelb = Label(root, text="Assessment of Eye response")
labelc = Label(root, text="Assessment of Verbal response")


label1.grid(column = 1, row = 0)
label2.grid(column = 1, row = 1)
labela.grid(column = 0, row = 2)
labelb.grid(column = 1, row = 2)
labelc.grid(column = 2, row = 2)

motor = IntVar() # 1 Step: radiobutton variable to be declared as type of data. Here we have assigned as integer so IntVar. For strings StrVar
eye = IntVar()
verbal = IntVar()

#create function what will a click response on radiobutton would do. In this case it takes up value from the radiobutton and prints out a label
#three different function for separate radiobutton group 
def clicked1(value):
    return value
    #label3 = Label(root, text = value).grid(column = 0, row = 9)
    
def clicked2(value):
    return value
    #label4 = Label(root, text = value).grid(column = 1, row = 9)
    
def clicked3(value):
    return value
    #label5 = Label(root, text = value).grid(column = 2, row = 9)

def total_gcs():
    global label6
    gcs = motor.get() + eye.get() + verbal.get()
    label6 = Label(root, text = "The GCS score is" + str(gcs))
    label6.grid(column = 1, row = 14)

def all_clear():
    motor.set(None)
    eye.set(None)
    verbal.set(None)
    label6.destroy()
#2 Step: Create radiobuttons. They can be grouped as below. If we insert command line function with argument(motor.get()). The value will be displayed on clicking 
r1 = Radiobutton(root, text = "Obeying commands", variable = motor, value = 6, command =lambda:clicked1(motor.get())).grid(column = 0, row = 3, sticky =W)
r2 = Radiobutton(root, text = "Localises", variable = motor, value = 5, command =lambda:clicked1(motor.get())).grid(column = 0, row = 4, sticky = W)
r3 = Radiobutton(root, text = "Normal Flexion", variable = motor, value = 4,command =lambda:clicked1(motor.get())).grid(column = 0, row = 5, sticky = W)
r4 = Radiobutton(root, text = "Abnormal Flexion", variable = motor, value = 3, command =lambda:clicked1(motor.get())).grid(column = 0, row = 6, sticky = W)
r5 = Radiobutton(root, text = "Abormal extension", variable = motor, value = 2, command =lambda:clicked1(motor.get())).grid(column = 0, row = 7, sticky = W)
r6 = Radiobutton(root, text = "None", variable = motor, value = 1, command =lambda:clicked1(motor.get())).grid(column = 0, row = 8, sticky = W)


r7 = Radiobutton(root, text = "Spontaneously", variable = eye, value = 4,command =lambda:clicked2(eye.get())).grid(column = 1, row = 3, sticky =W)
r8 = Radiobutton(root, text = "On Call", variable = eye, value = 3, command =lambda:clicked2(eye.get())).grid(column = 1, row = 4, sticky = W)
r9 = Radiobutton(root, text = "On Pain", variable = eye, value = 2, command =lambda:clicked2(eye.get())).grid(column = 1, row = 5, sticky = W)
r10 = Radiobutton(root, text = "Nil response", variable = eye, value = 1, command =lambda:clicked2(eye.get())).grid(column = 1, row = 6, sticky = W)


#2 a: If we dont include command, it will not be diplayed automatically. To call value via button see below
r11 = Radiobutton(root, text = "Oriented", variable = verbal, value = 5).grid(column = 2, row = 3, sticky =W)
r12 = Radiobutton(root, text = "Confused", variable = verbal, value = 4).grid(column = 2, row = 4, sticky = W)
r13 = Radiobutton(root, text = "Sentences", variable = verbal, value = 3).grid(column = 2, row = 5, sticky = W)
r14 = Radiobutton(root, text = "Incomprehensible sounds", variable = verbal, value = 2).grid(column = 2, row = 6, sticky = W)
r15 = Radiobutton(root, text = "None", variable = verbal, value = 1).grid(column = 2, row = 7, sticky = W)



#button_click1= Button(root, text = "click to calculate", command = lambda:clicked1(motor.get())).grid(column = 0, row = 8)
#button_click2= Button(root, text = "click to calculate", command = lambda:clicked2(eye.get())).grid(column = 1, row = 8)
#button_click3= Button(root, text = "click to calculate", command = lambda:clicked3(verbal.get())).grid(column = 2, row = 8)

button_gcs_click = Button(root, text = "Click to calculate GCS", command = total_gcs).grid(column = 1, row = 12)
button_clear = Button(root, text = "Click to reset", command = all_clear).grid(column = 1, row = 16)
root.mainloop()



