import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Generate and store the key (this would typically be done once and securely saved)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_message():
    message = entry_message.get("1.0", tk.END).strip()
    if message:
        encrypted_message = cipher_suite.encrypt(message.encode()).decode()
        entry_result.delete("1.0", tk.END)
        entry_result.insert(tk.END, encrypted_message)
    else:
        messagebox.showwarning("Warning", "Please enter a message to encrypt")

def decrypt_message():
    encrypted_message = entry_message.get("1.0", tk.END).strip()
    if encrypted_message:
        try:
            decrypted_message = cipher_suite.decrypt(encrypted_message.encode()).decode()
            entry_result.delete("1.0", tk.END)
            entry_result.insert(tk.END, decrypted_message)
        except Exception as e:
            messagebox.showerror("Error", "Decryption failed. Check the encrypted text.")
    else:
        messagebox.showwarning("Warning", "Please enter an encrypted message to decrypt")

# Set up the GUI
app = tk.Tk()
app.title("Encryption & Decryption App")

# Message Input
tk.Label(app, text="Enter Message:").pack()
entry_message = tk.Text(app, height=5, width=40)
entry_message.pack()

# Encrypt Button
encrypt_button = tk.Button(app, text="Encrypt", command=encrypt_message)
encrypt_button.pack(pady=5)

# Decrypt Button
decrypt_button = tk.Button(app, text="Decrypt", command=decrypt_message)
decrypt_button.pack(pady=5)

# Result Output
tk.Label(app, text="Result:").pack()
entry_result = tk.Text(app, height=5, width=40)
entry_result.pack()

# Run the application
app.mainloop()
