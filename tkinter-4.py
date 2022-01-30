from cgi import test
from cgitb import text
from tkinter import*

root = Tk()

def get_deta():
    get_name_input =  name_input.get()
    get_phone_number_input = phone_number_input.get()
    ge_email_input = email_input.get()

    with open('contact.txt','a+') as c:
        c.write(get_name_input +', ')
        c.write(get_phone_number_input+', ')
        c.write(ge_email_input+'\n')

    name_input.delete(0,'end')
    phone_number_input.delete(0,'end')
    email_input.delete(0,'end')


    succes_label = Label(root , text= "contact was saved successfully")
    succes_label.grid(row=4,column=1)
   

   


name_label = Label(root,text= " name")
name_input = Entry(root,width = 30)
name_label.grid(row=0 , column=0)
name_input.grid(row=0 , column=1)

phone_number_label = Label ( root , text="phone")
phone_number_input = Entry(root,width = 30)
phone_number_label.grid(row=1 , column=0)
phone_number_input.grid(row=1 , column=1)

email_label = Label(root,text="email")
email_input = Entry(root,width = 30)
email_label.grid(row=2 , column=0)
email_input.grid(row=2 , column=1)

save_button = Button(root , text = "save" , command=get_deta)
save_button.grid(row=3 , column=0 ,columnspan = 2)

root.geometry("500x400")

root.mainloop()

