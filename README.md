# Encryption/Decryption GUI Application

A simple encryption and decryption application with a graphical user interface (GUI) built using Python and `tkinter`. This project demonstrates the use of modular code design by separating encryption logic from the GUI implementation.

---

## **Features**

- **Encryption Process**: 
  - Uses a simple DES-like method for initial encryption.
  - Applies a second AES-like layer of encryption to the DES output.
- **Decryption Process**: 
  - Reverses the process by applying AES decryption followed by DES decryption.
- **GUI Interface**: 
  - Built with `tkinter`, the interface allows users to input plaintext, encrypt it, view the encrypted output (in hexadecimal), and decrypt it back to plaintext.

---

## **Setup and Usage**

### **Prerequisites**
- Python 3.6 or later.

### **Folder Structure**
```
project/
│
├── encryption_logic.py  # Contains the encryption and decryption logic
├── main_app.py          # The GUI implementation
└── README.md            # This file
```

---

### **Running the Application**

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the GUI application using the following command:
   ```bash
   python main_app.py
   ```

---

## **Encryption Logic**

The encryption logic is implemented in `encryption_logic.py` and uses XOR-based byte manipulation to simulate encryption. Keys are generated using Python's `os.urandom`:

- **DES-like Encryption**: Encrypts plaintext with an 8-byte key.
- **AES-like Encryption**: Applies a second layer of encryption with a 16-byte key.

---

## **Customization**

You can customize the encryption logic, keys, or GUI theme:
1. Update keys in `encryption_logic.py` if you want fixed keys instead of randomly generated ones.
2. Modify colors, fonts, or dimensions in `main_app.py` to change the theme.

---

## **Limitations**
- The encryption logic is for demonstration purposes and is not secure for real-world use.
- Only basic error handling is implemented.

---

## **License**

This project is open-source and available under the MIT License. You are free to use, modify, and distribute it as long as proper credit is given.

---

## **Acknowledgments**

- Inspired by basic cryptography concepts and modular software design.
- Built with Python and `tkinter`.

---

### **Contact**

For questions or suggestions, feel free to reach out:

- **Email**: adriansdsilva@gmail.com
- **GitHub**: [LeoSeeker526](https://github.com/LeoSeeker526)
  
