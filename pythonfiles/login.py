from tkinter import *
from tkinter import messagebox


class login_system:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#f0f2f5")

        # Title
        title = Label(
            self.root,
            text="Login System",
            font=("Arial", 30, "bold"),
            bg="#f0f2f5",
            fg="#0f4d7d"
        )
        title.pack(pady=30)

        # Login Frame
        login_frame = Frame(self.root, bg="white", bd=3, relief=RIDGE)
        login_frame.place(x=475, y=150, width=400, height=350)

        Label(
            login_frame,
            text="LOGIN",
            font=("Arial", 22, "bold"),
            bg="white",
            fg="#0f4d7d"
        ).pack(pady=20)

        # Username
        Label(
            login_frame,
            text="Username",
            font=("Arial", 14),
            bg="white"
        ).pack(anchor="w", padx=40)

        self.txt_user = Entry(login_frame, font=("Arial", 14))
        self.txt_user.pack(padx=40, fill=X, pady=5)

        # Password
        Label(
            login_frame,
            text="Password",
            font=("Arial", 14),
            bg="white"
        ).pack(anchor="w", padx=40, pady=(10, 0))

        self.txt_pass = Entry(login_frame, font=("Arial", 14), show="*")
        self.txt_pass.pack(padx=40, fill=X, pady=5)

        # Login Button
        Button(
            login_frame,
            text="Login",
            command=self.login,
            bg="#0f4d7d",
            fg="white",
            font=("Arial", 14, "bold"),
            cursor="hand2"
        ).pack(pady=25)

    def login(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required!")

        elif username == "admin" and password == "1234":
            messagebox.showinfo("Success", "Welcome Admin!")

        else:
            messagebox.showerror("Error", "Invalid Username or Password!")


root = Tk()
obj = login_system(root)
root.mainloop()