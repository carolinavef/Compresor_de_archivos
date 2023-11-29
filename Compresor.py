
import os
from bitarray import bitarray
import MinHeap
import tkinter as tk
from tkinter import filedialog

                                    ##HUFFMAN 
class HuffmanNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None

class HuffmanCoding:
    def __init__(self,root):
        self.root = root
    
        # Botones y etiquetas
        self.select_file_button = tk.Button(root, text="Seleccionar Archivo", command=self.select_file)
        self.select_file_button.pack(pady=10)

        self.compress_button = tk.Button(root, text="Comprimir Archivo", command=self.process_file)
        self.compress_button.pack(pady=10)
        self.compress_button = tk.Button(root, text="Descomprimir Archivo", command=self.process_file)
        self.compress_button.pack(pady=10)

        self.file_label = tk.Label(root, text="")
        self.file_label.pack(pady=10)
        
        #huffman
        self.original_text = ""
        self.freq_table = {}
        self.heap = MinHeap.Heap()
        self.huffman_tree = None
        self.table_conversion = {}
    
    #interfaz
    def select_file(self):
        file_path = filedialog.askopenfilename(title="Seleccionar archivo")
        self.file_label.config(text=f"Archivo seleccionado: {os.path.basename(file_path)}")
        self.set_original_text(file_path)  
    
    def interfaz_grafica(self, root):
            if not self.original_text:
                self.file_label.config(text="Selecciona un archivo primero.")
                return

            compressed_file_path = filedialog.asksaveasfilename(title="Guardar archivo comprimido como", defaultextension=".compressed")
            self.calculate_frequency_table()
            self.create_huffman_tree()
            self.calculate_table_conversion()
            compressed_text = self.get_compressed_text()
            
            decompressed_file_path = filedialog.asksaveasfilename(title="Guardar archivo comprimido como", defaultextension=".compressed")
            self.calculate_frequency_table()
            self.create_huffman_tree()
            self.calculate_table_conversion()
            decompressed_text = self.get_compressed_text()

            with open(compressed_file_path, 'wb') as file:
                file.write(bitarray(compressed_text).tobytes())
            
            with open(decompressed_file_path, 'wb') as file:
                file.write(bitarray(decompressed_text).tobytes())

            self.file_label.config(text="Compresión completa")

    #proceso huffman
    def set_original_text(self, text):

        with open(text, 'rb') as file:
            self.original_text = file.read()

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
        with open(r'C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\compreso_txt.txt', 'wb') as file:
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
        with open(r'C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\descompress_txt.txt', 'w') as file:
            file.write(decoded_text)

        return decoded_text
   
                                                 #COMPRIMIR Y DESCOMPRIMIR IMAGENES    
    def get_compressed_img(self):          
        compressed_text = ""
        for char in self.original_text:
            compressed_text += self.table_conversion[char]
            
        file_compressed=bitarray()
        file_compressed.encode({char: bitarray(code) for char, code in self.table_conversion.items()},self.original_text)
        with open(r"C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\compressso_img.zip", 'wb') as file:
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
        with open(r'C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\\descompressoo_img.png', 'wb') as file:
            file.write(decoded_text)

        return decoded_text
                                              #COMPRIMIR Y DESCOMPRIMIR AUDIOS

    def get_compressed_aud(self):          
        compressed_text = ""
        for byte in self.original_text:
            compressed_text += self.table_conversion[byte]
            
        file_compressed=bitarray()
        file_compressed.encode({byte: bitarray(code) for byte, code in self.table_conversion.items()},self.original_text)
        with open(r'C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\compreso_aud.zip', 'wb') as file:
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
        with open(r'C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\descompreso_aud.mp3', 'wb') as file:
            file.write(decoded_text_aud)

        return decoded_text_aud
    
                                                       #   COMPRESS Y DESCOMPRESS VIDEOS 
    def get_compressed_vid(self):          
        compressed_text_vid = ""
        for byte in self.original_text:
            compressed_text_vid += self.table_conversion[byte]
            
        file_compressed=bitarray()
        file_compressed.encode({byte: bitarray(code) for byte, code in self.table_conversion.items()},self.original_text)
        with open(r'C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\compreso_vid.zip', 'wb') as file:
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
        with open(r'C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\\descompreso_vid.mp4', 'wb') as file:
            file.write(decoded_text_vid)

        return decoded_text_vid

    compressed_text_path = 'compressed_file2.txt'
    decompressed_text_path = 'decompressed_file2.txt'
    zip_file_path = 'compressed_file.zip'

    def determine_file_type(file_path):
        _, file_extension = os.path.splitext(file_path)
        return file_extension.lower()

# FUNCIÓN PARA DETERMINAR EL TIPO DE ARCHIVO Y LLAMAR A LAS FUNCIONES CORRESPONDIENTES
    def process_file(self, file_path):
        file_extension = self.determine_file_type(file_path)
        
        # TEXTOOOOO
        if file_extension == ".txt":
            HC = HuffmanCoding()
            HC.set_original_text(file_path)
            HC.calculate_frequency_table()
            HC.create_huffman_tree()
            HC.calculate_table_conversion()
            compressed_text = HC.get_compressed_text()
            decoded_text = HC.decompress_text(compressed_text)

        # IMAGEEENNNNN
        elif file_extension in {".bmp", ".png", ".jpg"}:
            HC = HuffmanCoding()
            HC.set_original_text(file_path)
            HC.calculate_frequency_table()
            HC.create_huffman_tree()
            HC.calculate_table_conversion()
            compressed_text = HC.get_compressed_img()
            decoded_text = HC.decompress_img(compressed_text)


        #AUDIOOOOO
        elif file_extension == ".mp3":
            HC = HuffmanCoding()
            HC.set_original_text(file_path)
            HC.calculate_frequency_table()
            HC.create_huffman_tree()
            HC.calculate_table_conversion()
            compressed_text = HC.get_compressed_aud()
            decoded_text = HC.decompress_aud(compressed_text)
        

        #VIDEOOOOO
        elif file_extension == ".mp4":
            HC = HuffmanCoding()
            HC.set_original_text(file_path)  
            HC.calculate_frequency_table()
            HC.create_huffman_tree()
            HC.calculate_table_conversion()
            compressed_text = HC.get_compressed_vid()
            decoded_text = HC.decompress_vid(compressed_text)

        else:
            print(f"Unsupported file type: {file_extension}")


if __name__ == "__main__":
    root = tk.Tk()
    app = HuffmanCoding(root)
    root.mainloop()