import zipfile
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Tk
from tkinter import Button
from bitarray import bitarray
import MinHeap

class HuffmanNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None

class HuffmanCoding:
    def __init__(self):
        self.original_text = ""
        self.freq_table = {}
        self.heap = MinHeap.Heap()
        self.huffman_tree = None
        self.table_conversion = {}
        self.file_path = ""

    def set_original_text(self, text):

        with open(text, 'r') as file:
            self.original_text = file.read()
        self.file_path = text
        
    def set_original_file(self, file_path):
        with open(file_path, 'rb') as file:
            self.original_text = file.read()
        self.file_path = file_path



    def calculate_frequency_table(self):
        for c in self.original_text:
            if c in self.freq_table:
                self.freq_table[c] += 1
            else:
                self.freq_table[c] = 1

    def create_huffman_tree(self):
        elements = []

        for letter, freq in self.freq_table.items():
            elements.append(HuffmanNode(key=freq, value=letter))

        self.heap.build_heap(elements)

        while self.heap.get_size() > 1:
            left_node = self.heap.pop()
            right_node = self.heap.pop()

            nuevo_nodo = HuffmanNode(key=left_node.key + right_node.key)
            nuevo_nodo.left_child = left_node
            nuevo_nodo.right_child = right_node
            
            self.heap.insert(nuevo_nodo)
            
        self.huffman_tree = self.heap.pop()

    def calculate_table_conversion(self):
        self.table_conversion = {}
        self.__dfs(self.huffman_tree, "")

    def __dfs(self, curr_node, current_code):
        if not curr_node.left_child and not curr_node.right_child:
            self.table_conversion[curr_node.value] = current_code
        else:
            if curr_node.left_child:
                self.__dfs(curr_node.left_child, current_code + "0")

            if curr_node.right_child:
                self.__dfs(curr_node.right_child, current_code + "1")
                


                                                    #COMPRIMIR Y DESCOMPRIMIR ARCHIVO DE TEXTO

    def get_compressed_text(self):
        compressed_text = ""
        for char in self.original_text:
            compressed_text += self.table_conversion[char]
            
        file_compressed=bitarray()#en vez de regresar, ya usar bitarray  #donde se guarda los caracteres
        file_compressed.encode({char: bitarray(code) for char, code in self.table_conversion.items()},self.original_text)
        with open(r"C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\compreso_txt.zip", 'wb') as file:
            file_compressed.tofile(file)
            
        return compressed_text

    def decompress_text(self, compressed_text):
        decoded_text = ""
        current_node = self.huffman_tree

        for bit in compressed_text:
            if bit == "0":
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

            if not current_node.left_child and not current_node.right_child:
                decoded_text += current_node.value
                current_node = self.huffman_tree
        with open(r"C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\descompress_txt.txt", 'w') as file:
            file.write(decoded_text)

        return decoded_text
   
                                                 #COMPRIMIR Y DESCOMPRIMIR IMAGENES

    
    
    def get_compressed_img(self):          
        compressed_text = ""
        for char in self.original_text:
            compressed_text += self.table_conversion[char]
            
        file_compressed=bitarray()
        file_compressed.encode({char: bitarray(code) for char, code in self.table_conversion.items()},self.original_text)
        with open(r"C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\compressso_img.zip", 'wb') as file:
            file_compressed.tofile(file)
            
        return compressed_text

    def decompress_img(self, compressed_text):
        decoded_text = bytearray()
        current_node = self.huffman_tree

        for bit in compressed_text:
            if bit == "0":
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

            if not current_node.left_child and not current_node.right_child:
                decoded_text.append( current_node.value)
                current_node = self.huffman_tree
        with open(r"C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\descompressoo_img.png", 'wb') as file:
            file.write(decoded_text)

        return decoded_text
    
    
                                     
                                              #COMPRIMIR Y DESCOMPRIMIR AUDIOS

    def get_compressed_aud(self):          
        compressed_text = ""
        for byte in self.original_text:
            compressed_text += self.table_conversion[byte]
            
        file_compressed=bitarray()
        file_compressed.encode({byte: bitarray(code) for byte, code in self.table_conversion.items()},self.original_text)
        with open(r"C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\compreso_aud.zip", 'wb') as file:
            file_compressed.tofile(file)
            
        return compressed_text

    def decompress_aud(self, compressed_text):
        decoded_text_aud = bytearray()
        current_node = self.huffman_tree

        for bit in compressed_text:
            if bit == "0":
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

            if not current_node.left_child and not current_node.right_child:
                decoded_text_aud.append( current_node.value)
                current_node = self.huffman_tree
        with open(r"C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\descompreso_aud.mp3", 'wb') as file:
            file.write(decoded_text_aud)

        return decoded_text_aud
    
                                                       #   COMPRESS Y DESCOMPRESS VIDEOS 
    def get_compressed_vid(self):          
        compressed_text_vid = ""
        for byte in self.original_text:
            compressed_text_vid += self.table_conversion[byte]
            
        file_compressed=bitarray()
        file_compressed.encode({byte: bitarray(code) for byte, code in self.table_conversion.items()},self.original_text)
        with open(r'C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\compreso_vid.zip', 'wb') as file:
            file_compressed.tofile(file)
            
        return compressed_text_vid

    def decompress_vid(self, compressed_text):
        decoded_text_vid = bytearray()
        current_node = self.huffman_tree

        for bit in compressed_text:
            if bit == "0":
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

            if not current_node.left_child and not current_node.right_child:
                decoded_text_vid.append( current_node.value)
                current_node = self.huffman_tree
        with open(r"C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\descompreso_vid.mp4", 'wb') as file:
            file.write(decoded_text_vid)

        return decoded_text_vid
    



# INTERFAZ Y LLAMADA DE FUNCIONES

class HuffmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='#9c89b8')
        self.root.title("Algoritmo Huffman")

        custom_font = ("Oswald", 10, "bold")

        self.open_button = tk.Button(root, text="Abrir archivo", command=self.open_file, bg="#f0e6ef", width=20, borderwidth=10, relief=tk.GROOVE, font=custom_font)
        self.compress_button = tk.Button(root, text="Comprimir", command=self.compress, bg="#f0e6ef", width=10, borderwidth=10, relief=tk.GROOVE, font=custom_font)
        self.decompress_button = tk.Button(root, text="Descomprimir", command=self.decompress, bg="#f0e6ef", width=10, borderwidth=10, relief=tk.GROOVE, font=custom_font)

        

 
        self.open_button.pack(pady=10, padx=37, side=tk.LEFT)
        self.compress_button.pack(pady=5)
        self.decompress_button.pack(pady=10)

        root.geometry("460x230")

        # Crear un frame para contener los otros dos botones
        button_frame = tk.Frame(root)  # Color de fondo del frame
        button_frame.pack(side=tk.RIGHT, padx=20)

        # Colocar los botones "Comprimir" y "Descomprimir" en columna dentro del frame
        self.compress_button.pack(pady=40, anchor=tk.N)
        self.decompress_button.pack(pady=5, anchor=tk.S)

       
        self.HC = HuffmanCoding()

    # BOTÓN ABRIR ARCHIVO

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Seleccionar archivo")
        if file_path:
            file_extension = determine_file_type(file_path)
            if file_extension == ".txt":
                self.HC.set_original_text(file_path)
                messagebox.showinfo("Archivo abierto", f"Ruta del archivo: {file_path}")
            elif file_extension in {".bmp", ".png", ".jpg"}:
                self.HC.set_original_file(file_path)
                messagebox.showinfo("Archivo abierto", f"Ruta del archivo: {file_path}")
            elif file_extension == ".mp3":
                self.HC.set_original_file(file_path)
                messagebox.showinfo("Archivo abierto", f"Ruta del archivo: {file_path}")
            elif file_extension == ".mp4":
                self.HC.set_original_file(file_path)
                messagebox.showinfo("Archivo abierto", f"Ruta del archivo: {file_path}")
            else:
                messagebox.showwarning("Ruta inválida", f"Tipo de archivo: {file_extension}")

    
    #BOTÓN COMPRIMIR

    def compress(self):
        if not self.HC.file_path:  
            messagebox.showwarning("No se encontró ningún archivo", "Selecciona un archivo primero.")
            return

        file_extension = determine_file_type(self.HC.file_path)  
        if file_extension == ".txt":
            self.compress_text()
        elif file_extension in {".bmp", ".png", ".jpg"}:
            self.compress_img()
        elif file_extension == ".mp3":
            self.compress_aud()
        elif file_extension == ".mp4":
            self.compress_vid()
        else:
            messagebox.showwarning("Ruta inválida", f"Tipo de archivo: {file_extension}")

    
    #BOTÓN DESCOMPRIMIR

    def decompress(self):
        if not self.HC.file_path:  
            messagebox.showwarning("No se encontró ningún archivo", "Selecciona un archivo primero.")
            return

        file_extension = determine_file_type(self.HC.file_path) 
        if file_extension == ".txt":
            self.decompress_text()
        elif file_extension in {".bmp", ".png", ".jpg"}:
            self.decompress_img()
        elif file_extension == ".mp3":
            self.decompress_aud()
        elif file_extension == ".mp4":
            self.decompress_vid()
        else:
            messagebox.showwarning("Ruta inválida", f"Tipo de archivo: {file_extension}")

    # TEXTOOOOOOOO

    def compress_text(self):
        self.HC.calculate_frequency_table()
        self.HC.create_huffman_tree()
        self.HC.calculate_table_conversion()

        self.HC.get_compressed_text()
        messagebox.showinfo("Completado", "Archivo comprimido satisfactoriamente.")

    def decompress_text(self):
        compressed_text = self.HC.get_compressed_text()
        self.HC.decompress_text(compressed_text)
        messagebox.showinfo("Completado", "Archivo descomprimido satisfactoriamente.")

    # IMAGENNNNNNN

    def compress_img(self):
        self.HC.calculate_frequency_table()
        self.HC.create_huffman_tree()
        self.HC.calculate_table_conversion()

        self.HC.get_compressed_img()
        messagebox.showinfo("Completado", "Archivo comprimido satisfactoriamente.")
 

    def decompress_img(self):
        compressed_text = self.HC.get_compressed_img()
        self.HC.decompress_img(compressed_text)
        messagebox.showinfo("Completado", "Archivo descomprimido satisfactoriamente.")

    
    # AUDIOOOOOO

    def compress_aud(self):
        self.HC.calculate_frequency_table()
        self.HC.create_huffman_tree()
        self.HC.calculate_table_conversion()

        self.HC.get_compressed_aud()
        messagebox.showinfo("Completado", "Archivo comprimido satisfactoriamente.")
 

    def decompress_aud(self):
        compressed_text = self.HC.get_compressed_aud()
        self.HC.decompress_aud(compressed_text)
        messagebox.showinfo("Completado", "Archivo descomprimido satisfactoriamente.")


    # VIDEOOOOOOO
   

    def compress_vid(self):
        self.HC.calculate_frequency_table()
        self.HC.create_huffman_tree()
        self.HC.calculate_table_conversion()

        self.HC.get_compressed_vid()
        messagebox.showinfo("Completado", "Archivo comprimido satisfactoriamente.")


    def decompress_vid(self):
        compressed_text = self.HC.get_compressed_vid()
        self.HC.decompress_vid(compressed_text)
        messagebox.showinfo("Completado", "Archivo descomprimido satisfactoriamente.")
        

    


def determine_file_type(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower()

if __name__ == "__main__":
    root = tk.Tk()
    gui = HuffmanGUI(root)
    root.mainloop()