import tkinter as tk
from tkinter import messagebox
import mysql.connector

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        # Centralizar a janela
        window_width = 500
        window_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height/2 - window_height/2)
        position_right = int(screen_width/2 - window_width/2)
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        # Frame principal centralizado
        main_frame = tk.Frame(root)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Label de título
        title_label = tk.Label(main_frame, text="Sistema de Login", font=("Segoe Print", 16, "bold"), pady=10)
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Campos de entrada
        tk.Label(main_frame, text="E-mail:", font=("Segoe Print", 12, "bold")).grid(row=1, column=0, sticky="e", pady=5, padx=10)
        self.email_entry = tk.Entry(main_frame, font=("Segoe Print", 12))
        self.email_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(main_frame, text="Senha:", font=("Segoe Print", 12, "bold")).grid(row=2, column=0, sticky="e", pady=5, padx=10)
        self.password_entry = tk.Entry(main_frame, font=("Segoe Print", 12), show="*")
        self.password_entry.grid(row=2, column=1, pady=5, padx=10)

        # Botão de login
        login_button = tk.Button(main_frame, text="Login", font=("Segoe Print", 14, "bold"), command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=20)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not (email and password):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        try:
            # Conectar ao banco de dados
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pieralini__login"
            )
            cursor = conn.cursor()

            # Verificar as credenciais
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
                self.root.destroy()
                self.open_cadastro_form()
            else:
                messagebox.showerror("Erro", "E-mail ou senha inválidos!")

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")

        finally:
            if conn:
                conn.close()

    def open_cadastro_form(self):
        new_root = tk.Tk()
        CadastroForm(new_root)
        new_root.mainloop()

class CadastroForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        # Centralizar a janela
        window_width = 500
        window_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height/2 - window_height/2)
        position_right = int(screen_width/2 - window_width/2)
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        # Frame principal centralizado
        main_frame = tk.Frame(root)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Label de título
        title_label = tk.Label(main_frame, text="Sistema de Cadastro", font=("Segoe Print", 16, "bold"), pady=10)
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Campos de entrada
        tk.Label(main_frame, text="Nome:", font=("Segoe Print", 12, "bold")).grid(row=1, column=0, sticky="e", pady=5, padx=10)
        self.name_entry = tk.Entry(main_frame, font=("Segoe Print", 12))
        self.name_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(main_frame, text="E-mail:", font=("Segoe Print", 12, "bold")).grid(row=2, column=0, sticky="e", pady=5, padx=10)
        self.email_entry = tk.Entry(main_frame, font=("Segoe Print", 12))
        self.email_entry.grid(row=2, column=1, pady=5, padx=10)

        tk.Label(main_frame, text="Telefone:", font=("Segoe Print", 12, "bold")).grid(row=3, column=0, sticky="e", pady=5, padx=10)
        self.phone_entry = tk.Entry(main_frame, font=("Segoe Print", 12))
        self.phone_entry.grid(row=3, column=1, pady=5, padx=10)

        tk.Label(main_frame, text="Endereço:", font=("Segoe Print", 12, "bold")).grid(row=4, column=0, sticky="e", pady=5, padx=10)
        self.address_entry = tk.Entry(main_frame, font=("Segoe Print", 12))
        self.address_entry.grid(row=4, column=1, pady=5, padx=10)

        tk.Label(main_frame, text="Senha:", font=("Segoe Print", 12, "bold")).grid(row=5, column=0, sticky="e", pady=5, padx=10)
        self.password_entry = tk.Entry(main_frame, font=("Segoe Print", 12), show="*")
        self.password_entry.grid(row=5, column=1, pady=5, padx=10)

        # Botão de cadastro
        submit_button = tk.Button(main_frame, text="Cadastrar", font=("Segoe Print", 14, "bold"), command=self.register)
        submit_button.grid(row=6, column=0, columnspan=2, pady=20)

    def register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        password = self.password_entry.get()

        if not (name and email and phone and address and password):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        try:
            # Conectar ao banco de dados
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pieralini__login"
            )
            cursor = conn.cursor()

            # Inserir os dados no banco
            query = "INSERT INTO users (name, email, phone, adress, password) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (name, email, phone, address, password))
            conn.commit()

            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.clear_fields()

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")

        finally:
            if conn:
                conn.close()

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()
