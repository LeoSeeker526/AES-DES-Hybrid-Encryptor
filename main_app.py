import tkinter as tk
from tkinter import messagebox
from encryption_logic import des_encrypt, des_decrypt, aes_encrypt, aes_decrypt, DES_KEY, AES_KEY


class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AES & DES Hybrid Encryptor")
        self.root.configure(bg="black")  # Set background color to black
        self.root.geometry("600x500")  # Set the window size (width x height)

        # Input Label and Entry
        self.input_label = tk.Label(root, text="Enter Plaintext:", fg="red", bg="black", font=("Arial", 12))
        self.input_label.pack(pady=10)
        self.input_entry = tk.Entry(root, width=60, fg="red", bg="black", insertbackground="red")
        self.input_entry.pack(pady=10)

        # Encrypt Button
        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt, fg="black", bg="red", font=("Arial", 12))
        self.encrypt_button.pack(pady=10)

        # Output Label
        self.output_label = tk.Label(root, text="Encrypted Output (Hex):", fg="red", bg="black", font=("Arial", 12))
        self.output_label.pack(pady=10)
        self.output_text = tk.Text(root, height=6, width=60, fg="red", bg="black", insertbackground="red")
        self.output_text.pack(pady=10)

        # Decrypt Button
        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt, fg="black", bg="red", font=("Arial", 12))
        self.decrypt_button.pack(pady=10)

        # Decrypted Output Label
        self.decrypted_label = tk.Label(root, text="Decrypted Plaintext:", fg="red", bg="black", font=("Arial", 12))
        self.decrypted_label.pack(pady=10)
        self.decrypted_text = tk.Text(root, height=4, width=60, fg="red", bg="black", insertbackground="red")
        self.decrypted_text.pack(pady=10)

    def encrypt(self):
        plaintext = self.input_entry.get()
        if not plaintext:
            messagebox.showerror("Error", "Please enter plaintext to encrypt!")
            return

        # Encryptions
        des_encrypted = des_encrypt(plaintext, DES_KEY)
        aes_encrypted = aes_encrypt(des_encrypted, AES_KEY)

        # Display encrypted output
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, aes_encrypted.hex())

    def decrypt(self):
        encrypted_hex = self.output_text.get(1.0, tk.END).strip()
        if not encrypted_hex:
            messagebox.showerror("Error", "No encrypted data found!")
            return

        try:
            # Convert hex back to bytes
            aes_encrypted = bytes.fromhex(encrypted_hex)

            # Decryptions
            aes_decrypted = aes_decrypt(aes_encrypted, AES_KEY)
            des_decrypted = des_decrypt(aes_decrypted, DES_KEY)

            # Display decrypted output
            self.decrypted_text.delete(1.0, tk.END)
            self.decrypted_text.insert(tk.END, des_decrypted)
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {e}")


# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
