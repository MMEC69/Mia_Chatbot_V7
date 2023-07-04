from tkinter import *
from main import application_msg_parser, bot_name

BG_PINK = '#FFB6C1'
BG_LIGHTBLUE = '#99E0DF'
BG_LIGHTYELLOW = '#CECE5E'
TEXT_COLOR = '#FFFFFF'

FONT = 'Helvetica 20'
FONT_BOLD = 'Helvetica 20 bold'


class MiaApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Mia <3")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=600, height=900, bg=BG_PINK)

        # head label
        head_label = Label(self.window, bg=BG_PINK, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1, relheight=0.3)

        # tiny divider
        #line = Label(self.window, width=450, bg=BG_PINK)
        #line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_PINK,
                                fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.6275, relwidth=1, rely=0.3)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        #scrollbar = Scrollbar(self.text_widget)
        #scrollbar.place(relheight=1, relx=0.974)
        #scrollbar.configure(command=self.text_widget.yview())
        # this basically mean we can scroll up and down

        # bottom label
        bottom_label = Label(self.window, bg=BG_LIGHTBLUE, height=48)
        bottom_label.place(relwidth=1, rely=0.9275)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg=BG_LIGHTBLUE, fg=TEXT_COLOR,
                               font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.0085, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        #send button
        send_button = Button(bottom_label, text="Send", font = FONT_BOLD, width=20, bg=BG_LIGHTYELLOW,
                             command = lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely = 0.0085, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
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

        msg2 = f"{bot_name}: {application_msg_parser(msg)}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        self.text_widget.see(END)
        #This is to make sure chat i s set to the bottom of the conversation

if __name__ == "__main__":
    app = MiaApplication()
    app.run()
