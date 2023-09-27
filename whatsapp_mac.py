# Program to send bulk messages through WhatsApp web from an excel sheet without saving contact numbers
# pyinstaller  --windowed --icon=app_icon.icns whatsapp_mac.py

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

windows = "user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Wtsp"

mac = "user-data-dir=Users/{}/Library/Application Support/Google/Chrome/Wtsp"

linux = "user-data-dir=/home/{}/.config/google-chrome/wtsp"

success = []
failure = []
p_path = []

# excel_data = {'Contact': ["+4915209986443, +4915730765618, +4915209986443"]}
x_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'


# x = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'


def whatsapp(base_msg, contacts, profile_path):
    def element_presence(by, xpath, time):
        element_present = EC.presence_of_element_located((By.XPATH, xpath))
        WebDriverWait(driver, time).until(element_present)

    def send_message(url):
        driver.get(url)
        time.sleep(2)
        element_presence(By.XPATH, x_path, 15)
        msg_box = driver.find_element(By.XPATH, x_path)
        msg_box.send_keys('\n')
        time.sleep(1)

    def prepare_msg(base_msg, phone_no):
        base_url = 'https://web.whatsapp.com/send?phone={}&text={}'
        # msg = urllib.parse.quote(base_msg.format(Name))
        url_msg = base_url.format(phone_no, base_msg)
        send_message(url_msg)

    count = 0
    options = webdriver.ChromeOptions()
    options.add_argument(profile_path)
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get('https://web.whatsapp.com')

        input(f"{bcolors.OKCYAN}Press ENTER after login into Whatsapp Web and your chats are visiable.{bcolors.ENDC}")
        for column in contacts:
            try:
                url = 'https://web.whatsapp.com/send?phone=' + str(contacts[count]) + '&text=' + "hello"
                sent = False
                # It tries 3 times to send a message in case if there any error occurred
                driver.get(url)
                try:
                    prepare_msg(base_msg, column)
                    click_btn = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.XPATH, x_path)))
                except Exception as e:
                    print(f"{bcolors.FAIL}Sorry message could not sent to {bcolors.ENDC}" + str(column))
                    failure.append(str(column))
                else:
                    sleep(1)
                    click_btn.click()
                    sent = True
                    sleep(1)
                    print(f'{bcolors.OKGREEN}Message sent to: {bcolors.ENDC}' + str(column))
                    success.append(str(column))
                count = count + 1
            except Exception as e:
                print(f'{bcolors.FAIL}Failed to send message to {bcolors.ENDC}' + str(column) + str(e))
                failure.append(str(column))
        driver.quit()
    except:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://web.whatsapp.com')

        input("Press ENTER after login into Whatsapp Web and your chats are visiable.")
        for column in contacts:
            try:
                url = 'https://web.whatsapp.com/send?phone=' + str(contacts[count]) + '&text=' + "hello"
                sent = False
                # It tries 3 times to send a message in case if there any error occurred
                driver.get(url)
                try:
                    prepare_msg(base_msg, column)
                    click_btn = WebDriverWait(driver, 35).until(
                        EC.element_to_be_clickable((By.XPATH, x_path)))
                except Exception as e:
                    print("Sorry message could not sent to " + str(column))
                    failure.append(str(column))
                else:
                    sleep(1)
                    click_btn.click()
                    sent = True
                    sleep(1)
                    print('Message sent to: ' + str(column))
                    success.append(str(column))
                count = count + 1
            except Exception as e:
                print('Failed to send message to ' + str(column) + str(e))
                failure.append(str(column))
        driver.quit()


from tkinter import *
from tkinter import messagebox


def test():
    if message_field.get() == "" or contacts_field.get() == "" or folder_field.get() == "" :
        messagebox.showwarning("Form details missing", "Please fill, all the input fields present in the form. ")
    elif delimeter_field.get() == "":
        res = messagebox.askyesno("submit", "Do you want to submit the form?")
        if res == 1:

            user_folder = folder_field.get()
            p_path.clear()
            p_path.append(mac.format(str(user_folder)))




            msg = message_field.get()
            cont = []
            cont.clear()
            for i in list(contacts_field.get().replace(" ", "").split('')):
                if i not in cont:
                    cont.append(i)
            contacts = cont
            whatsapp(msg, contacts, p_path[0])

            folder_field.delete(0, END)
            message_field.delete(0, END)
            contacts_field.delete(0, END)
            delimeter_field.delete(0, END)

            dis_msg_s = "Message send successfully to {s}. "
            dis_msg_f = "Message send failed to {f}."
            messagebox.showinfo("Result", dis_msg_s.format(s=success))
            messagebox.showerror("Result", dis_msg_f.format(f=failure))
            success.clear()
            failure.clear()
    elif delimeter_field.get() == " ":
        res = messagebox.askyesno("submit", "Do you want to submit the form?")
        if res == 1:

            user_folder = folder_field.get()
            p_path.clear()
            p_path.append(mac.format(str(user_folder)))



            msg = message_field.get()
            cont = []
            cont.clear()
            for i in list(contacts_field.get().split(delimeter_field.get())):
                if i not in cont:
                    cont.append(i)
            contacts = cont
            whatsapp(msg, contacts, p_path[0])

            folder_field.delete(0, END)
            message_field.delete(0, END)
            contacts_field.delete(0, END)
            delimeter_field.delete(0, END)

            dis_msg = "Message send successfully to {s}. "
            dis_msg_f = "Message send failed to {f}."
            messagebox.showinfo("Result", dis_msg.format(s=success))
            messagebox.showerror("Result", dis_msg_f.format(f=failure))
            success.clear()
            failure.clear()
    else:
        res = messagebox.askyesno("submit", "Do you want to submit the form?")
        if res == 1:

            user_folder = folder_field.get()
            p_path.clear()
            p_path.append(mac.format(str(user_folder)))



            msg = message_field.get()
            cont = []
            cont.clear()
            for i in list(contacts_field.get().replace(" ", "").split(delimeter_field.get())):
                if i not in cont:
                    cont.append(i)
            contacts = cont
            whatsapp(msg, contacts, p_path[0])

            folder_field.delete(0, END)
            message_field.delete(0, END)
            contacts_field.delete(0, END)
            delimeter_field.delete(0, END)

            dis_msg = "Message send successfully to {s}. "
            dis_msg_f = "Message send failed to {f}."
            messagebox.showinfo("Result", dis_msg.format(s=success))
            messagebox.showerror("Result", dis_msg_f.format(f=failure))
            success.clear()
            failure.clear()


def reset():
    res = messagebox.askyesno("submit", "Do you want to reset the form?")
    if res == 1:
        folder_field.delete(0, END)
        message_field.delete(0, END)
        contacts_field.delete(0, END)
        delimeter_field.delete(0, END)



# create a GUI window
# Function to set focus (cursor)
def focus1(event):
    # set focus on the course_field box
    message_field.focus_set()


# Function to set focus
def focus2(event):
    # set focus on the sem_field box
    contacts_field.focus_set()


# Function to set focus
def focus3(event):
    # set focus on the sem_field box
    delimeter_field.focus_set()


def focus4(event):
    # set focus on the sem_field box
    folder_field.focus_set()


root = Tk()

# set the background colour of GUI window
root.configure(background='black')

# set the title of GUI window
root.title("Whatsapp Automation tool")

# set the configuration of GUI window
root.geometry("500x300")

# create a Form label
heading = Label(root, text="Details for sending the messages", bg="black")

# create a message label
message = Label(root, text="Message to be send", bg="black", fg="white")

# create a contacts label
contacts = Label(root, text="Contacts list with Country code", bg="black", fg="white")

# create a contacts label
delimeter = Label(root, text="Delimeter", bg="black", fg="white")



folder = Label(root, text="User folder name", bg="black", fg="white")

heading.config(font=("Helvetica", 40, 'bold'), fg='green yellow')

message.config(font=("Helvetica", 24, 'bold'))

contacts.config(font=("Helvetica", 22, 'bold'))

delimeter.config(font=("Helvetica", 24, 'bold'))

folder.config(font=("Helvetica", 24, 'bold'))
# grid method is used for placing
# the widgets at respective positions
# in table like structure .
heading.place(x=550, y=20)

folder.place(x=40, y=180)
message.place(x=40, y=230)
contacts.place(x=40, y=280)
delimeter.place(x=40, y=330)

# create a text entry box
# for typing the information
message_field = Entry(root)
contacts_field = Entry(root)
delimeter_field = Entry(root)
folder_field = Entry(root)

# bind method of widget is used for
# the binding the function with the events

# whenever the enter key is pressed
# then call the focus1 function
message_field.bind("<Return>", focus1)
message_field.config(font=("Helvetica", 20))

# whenever the enter key is pressed
# then call the focus2 function
contacts_field.bind("<Return>", focus2)
contacts_field.config(font=("Helvetica", 20))

delimeter_field.bind("<Return>", focus3)
delimeter_field.config(font=("Helvetica", 20))

folder_field.bind("<Return>", focus4)
folder_field.config(font=("Helvetica", 20))

# grid method is used for placing
# the widgets at respective positions
# in table like structure .
folder_field.place(x=500, y=180, width=1000)
message_field.place(x=500, y=230, width=1000, )
contacts_field.place(x=500, y=280, width=1000, )
delimeter_field.place(x=500, y=330, width=1000)

# call excel function


# create a Submit Button and place into the root window
submit = Button(root, text="Submit", fg="white",
                bg="darkgreen", activeforeground='black', command=test, font=("Helvetica", 18))
reset = Button(root, text="Reset", fg="white", activeforeground='black', command=reset,
               bg="Darkred", font=("Helvetica", 18))
submit.place(x=600, y=450)
reset.place(x=750, y=450)



# start the GUI
root.mainloop()
print("The script executed successfully.")
