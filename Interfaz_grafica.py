import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Importa ttk para el manejo de estilos
import zipfile

class Compresor:
    def __init__(self, master):
        self.master = master
        self.master.title("Compresor de Archivos")
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#87CEEB')  # Fondo del marco
        self.style.configure('TLabel', background='#333', foreground='white')  # Color del texto
        self.style.configure('TButton', background='#00bcd4', foreground='blue') 

        self.frame = ttk.Frame(self.master)
        self.frame.pack(padx=20, pady=20)

        self.label = ttk.Label(self.frame, text="Selecciona un archivo para comprimir:")
        self.label.pack()

        self.boton_seleccionar = ttk.Button(self.frame, text="Seleccionar Archivo", command=self.seleccionar_archivo)
        self.boton_seleccionar.pack(pady=10)

        self.boton_comprimir = ttk.Button(self.frame, text="Comprimir", command=self.comprimir_archivo)
        self.boton_comprimir.pack(pady=10)

    def seleccionar_archivo(self):
        self.archivo = filedialog.askopenfilename(initialdir="/", title="Seleccionar Archivo")
        self.label.configure(text=f"Archivo seleccionado: {self.archivo}")

    def comprimir_archivo(self):
        if hasattr(self, 'archivo'):
            archivo_comprimido = self.archivo + ".zip"
            with zipfile.ZipFile(archivo_comprimido, 'w') as zipf:
                zipf.write(self.archivo, arcname="archivo_comprimido")
            messagebox.showinfo("Éxito", f"Archivo comprimido como {archivo_comprimido}")
        else:
            messagebox.showwarning("Error", "Selecciona un archivo antes de comprimir.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Compresor(root)
    root.mainloop()
