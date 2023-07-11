from tkinter import *
#import threading
from PIL import Image, ImageTk
import main
from main import application_msg_parser, bot_name

FG_Msg_Box = '#FFB6C1' #pink color
#BG_LIGHTBLUE = '#99E0DF'
#BG_LIGHTYELLOW = '#CECE5E'
#TEXT_COLOR = '#FFFFFF'
BG_Msg_Box = "#FFFFFF" #white
BG_Text_Box = "#FFFFFF" #white
BG_Window = '#FFB6C1' #pink
#Above varable names are meaning less for the record "#FFFFFF" is used to color almost all of the GUI,


FONT = 'Helvetica 20'
FONT_BOLD = 'Helvetica 20 bold'



#passing_message = ""

class MiaApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()


    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Mia <3")

        icon1 = PhotoImage(file='icon\\mia_icon.png')
        #assigned the .png file to icon1 variable
        self.window.iconphoto(True, icon1)

        self.window.resizable(width=True, height=True)
        self.window.configure(width=850, height=1000, bg=BG_Msg_Box)

        # head label
        #head_label = Label(self.window, bg=BG_PINK, fg=TEXT_COLOR,
        #                  text="Welcome", font=FONT_BOLD, pady=10)
        #head_label.place(relwidth=1, relheight=0.3)

        # tiny divider
        #line = Label(self.window, width=450, bg=BG_PINK)
        #line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window,
                                width=20,
                                height=2,
                                bg=BG_Text_Box,
                                fg=FG_Msg_Box,
                                font=FONT,
                                padx=5,
                                pady=5,
                                bd=0
                                )
        self.text_widget.place(relheight=0.925,
                               relwidth=0.60,
                               rely=0.,
                               relx=0
                               )
        self.text_widget.configure(cursor="arrow",
                                   state=DISABLED
                                   )

        #self.text_widget.tag_config("justify", justify="")
        # scroll bar
        #scrollbar = Scrollbar(self.text_widget)
        #scrollbar.place(relheight=1, relx=0.974)
        #scrollbar.configure(command=self.text_widget.yview())
        # this basically mean we can scroll up and down

        # bottom label
        bottom_label = Label(self.window, bg=BG_Text_Box, height=48)
        bottom_label.place(relwidth=1, rely=0.9250)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#F6EFEF", fg=FG_Msg_Box,
                               font=FONT, bd = 0)
        self.msg_entry.place(relwidth=0.8535, relheight=0.0750, rely=0.0085, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        #send button
        #self.send_button_icon = PhotoImage(file="icon\\send1.png")
        #self.send_button_icon_r = Image.open("icon\\send1.png")
        #self.send_button_icon_rn = self.send_button_icon_r.resize((115, 115))

        #open image
        self.send_button_icon = Image.open("icon\\send3.png")

        #resize
        self.send_button_icon_r = self.send_button_icon.resize((50, 50))

        self.send_button_icon_rn = ImageTk.PhotoImage(self.send_button_icon_r)
        send_button = Button(bottom_label,
                             text="S",
                             font=FONT_BOLD,
                             #width=20,
                             #height=20,
                             #bg=BG_Window,
                             #fg=BG_Text_Box,
                             activeforeground=BG_Text_Box,
                             activebackground=BG_Msg_Box,
                             command=lambda: self._on_enter_pressed(None),
                             bd=0,
                             image=self.send_button_icon_rn
                             )
        send_button.place(relx=0.9295,
                          rely = 0.0085,
                          relheight=0.0760,
                          relwidth=0.0755
                          )
        #0.5850

    #=============================================
    #mic button yet to be implemented
        # open image
        self.mic_button_icon = Image.open("icon\\microphone1.png")

        # resize
        self.mic_button_icon_r = self.mic_button_icon.resize((50, 50))

        self.mic_button_icon_rn = ImageTk.PhotoImage(self.mic_button_icon_r)
        mic_button = Button(bottom_label,
                            text="M",
                            font=FONT_BOLD,
                            # width=20,
                            # height=20,
                            # bg=BG_Window,
                            # fg=BG_Text_Box,
                            activeforeground=BG_Text_Box,
                            activebackground=BG_Msg_Box,
                            command=lambda: self._on_mic_pressed(None),
                            bd=0,
                            image=self.mic_button_icon_rn
                            )
        mic_button.place(relx=0.8540,
                         rely=0.0085,
                         relheight=0.0760,
                         relwidth=0.0755
                         )




    #def _on_enter_pressed(self, event):
        #msg = self.msg_entry.get()
        #self._insert_message(msg, "You")

    #=============================================
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    #This function below need to be completed
    def _on_mic_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")


    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, END)

        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        msg_returned_bot = application_msg_parser(msg)
        msg2 = f"{bot_name}: {msg_returned_bot}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        main.speak(msg_returned_bot)
        main.engine.runAndWait()
        self.text_widget.see(END)
        #This is to make sure chat i s set to the bottom of the conversation


if __name__ == "__main__":
    app = MiaApplication()
    app.run()
