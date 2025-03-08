import tkinter as tk
from tkinter import messagebox, scrolledtext
import string
import matplotlib.pyplot as plt
from collections import Counter
import itertools

# Caesar Cipher
def caesar_cipher(text, shift, decrypt=False):
    shift = -shift if decrypt else shift
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Vigenere Cipher
def vigenere_cipher(text, key, decrypt=False):
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            shift = -shift if decrypt else shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# Playfair Cipher
def playfair_cipher(text, key, decrypt=False):
    return text[::-1]  # Placeholder for now

# Brute Force Monoalphabetic Cipher
def brute_force_mono(text):
    letters = string.ascii_lowercase
    possibilities = []
    for perm in itertools.permutations(letters[:3]):  # Limiting for performance
        key_map = str.maketrans(letters, ''.join(perm) + letters[3:])
        possibilities.append(text.translate(key_map))
    return possibilities

# Frequency Analysis
def frequency_analysis(text):
    counts = Counter(filter(str.isalpha, text.upper()))
    plt.figure(figsize=(8, 5))
    plt.bar(counts.keys(), counts.values(), color='blue')
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.title("Letter Frequency Analysis")
    plt.show()
    return counts

# GUI Functions
def open_cipher_window(title, cipher_func):
    win = tk.Toplevel()
    win.title(title)
    tk.Label(win, text="Enter text:").pack()
    text_entry = tk.Entry(win)
    text_entry.pack()
    tk.Label(win, text="Key/Shift:").pack()
    key_entry = tk.Entry(win)
    key_entry.pack()
    
    def process(decrypt=False):
        text, key = text_entry.get(), key_entry.get()
        result = cipher_func(text, int(key) if "Caesar" in title else key, decrypt)
        messagebox.showinfo("Result", result)
    
    tk.Button(win, text="Encrypt", command=lambda: process(False)).pack()
    tk.Button(win, text="Decrypt", command=lambda: process(True)).pack()
    tk.Button(win, text="Back", command=win.destroy).pack()

def open_brute_force_window():
    win = tk.Toplevel()
    win.title("Brute Force Monoalphabetic")
    tk.Label(win, text="Enter Cipher Text:").pack()
    text_entry = tk.Entry(win)
    text_entry.pack()
    result_box = scrolledtext.ScrolledText(win, width=50, height=20)
    result_box.pack()
    
    def attack():
        results = brute_force_mono(text_entry.get())
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, "\n".join(results))
    
    tk.Button(win, text="Start Attack", command=attack).pack()
    tk.Button(win, text="Back", command=win.destroy).pack()

def open_analysis_window():
    win = tk.Toplevel()
    win.title("Frequency Analysis")
    tk.Label(win, text="Enter text:").pack()
    text_entry = tk.Entry(win)
    text_entry.pack()
    
    def analyze():
        counts = frequency_analysis(text_entry.get())
        messagebox.showinfo("Letter Frequency", "\n".join(f"{k}: {v} times" for k, v in counts.items()))
    
    tk.Button(win, text="Analyze", command=analyze).pack()
    tk.Button(win, text="Back", command=win.destroy).pack()

def open_main_menu():
    root = tk.Tk()
    root.title("Crypto Game")
    root.geometry("500x400")
    root.configure(bg="#2E8B57")
    
    def start():
        for widget in root.winfo_children():
            widget.destroy()
        tk.Button(root, text="Caesar Cipher", command=lambda: open_cipher_window("Caesar Cipher", caesar_cipher), bg="#FFA500").pack(pady=10)
        tk.Button(root, text="Vigenère Cipher", command=lambda: open_cipher_window("Vigenère Cipher", vigenere_cipher), bg="#FF4500").pack(pady=10)
        tk.Button(root, text="Playfair Cipher", command=lambda: open_cipher_window("Playfair Cipher", playfair_cipher), bg="#32CD32").pack(pady=10)
        tk.Button(root, text="Brute Force Mono", command=open_brute_force_window, bg="#8A2BE2").pack(pady=10)
        tk.Button(root, text="Frequency Analysis", command=open_analysis_window, bg="#4682B4").pack(pady=10)
        tk.Button(root, text="Back", command=root.quit, bg="#DC143C").pack(pady=10)
    
    tk.Label(root, text="Welcome to Crypto Game!", font=("Arial", 16), bg="#2E8B57", fg="white").pack(pady=50)
    tk.Button(root, text="Let's Go!", command=start, bg="#FFD700").pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    open_main_menu()