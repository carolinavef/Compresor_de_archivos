import zipfile
import os
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

    def set_original_text(self, text):

        with open(text, 'r') as file:
            self.original_text = file.read()
        
    def set_original_img(self, img):
        with open(img, 'rb') as file:
            self.original_text = file.read()

    def set_original_aud(self, audio):
        with open(audio, 'rb') as file:
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
        with open(r"C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\compreso_txt.txt", 'wb') as file:
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
        with open(r"C:\Users\caro_\OneDrive\Desktop\UP\Estructura de datos\PARCIAL 3\COMPRESOR DE ARCHIVOS\descompressoo_img.png", 'wb') as file:
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
        with open(r"C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\descompreso_aud.mp4", 'wb') as file:
            file.write(decoded_text_vid)

        return decoded_text_vid
    






compressed_text_path = 'compressed_file2.txt'
decompressed_text_path = 'decompressed_file2.txt'
zip_file_path = 'compressed_file.zip'


# TEXTOOOOOO

original_text_path = r'C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\archivo.txt'
HC_text = HuffmanCoding()
HC_text.set_original_text(original_text_path)
HC_text.calculate_frequency_table()
HC_text.create_huffman_tree()
HC_text.calculate_table_conversion()
compressed_text_text = HC_text.get_compressed_text()

# Imprimir resultados para el archivo de texto
print("\nTexto original:", HC_text.original_text)
print("Texto comprimido:", compressed_text_text)

# Decodificar el texto comprimido
decoded_text_text = HC_text.decompress_text(compressed_text_text)
print("Texto reconstruido: ", decoded_text_text, "\n")

# Guardar el archivo comprimido de texto
with open(compressed_text_path, 'w') as file:
    file.write(compressed_text_text)



# IMAGENNNNNNNN


original_text_path= r'C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\input_img.bmp'
# Comprimir la imagen
HC_img = HuffmanCoding()
HC_img.set_original_img(original_text_path)  # Cambiado a set_original_img
HC_img.calculate_frequency_table()
HC_img.create_huffman_tree()
HC_img.calculate_table_conversion()
compressed_text_img = HC_img.get_compressed_img()  # Cambiado a get_compressed_img

# Imprimir resultados para la imagen
print("\nImagen original:", HC_img.original_text)
print("Imagen comprimida:", compressed_text_img)

# Decodificar la imagen comprimida
decoded_text_img = HC_img.decompress_img(compressed_text_img)
print("Imagen reconstruida: ", decoded_text_img, "\n")

# Guardar el archivo comprimido de imagen
with open(compressed_text_img, 'w') as file:
    file.write(compressed_text_img)



#AUDIOOOOOOO


original_audio_path= r'C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\audio2.mp3'

HC_aud = HuffmanCoding()
HC_aud.set_original_aud(original_audio_path)  # Cambiado a set_original_img
HC_aud.calculate_frequency_table()
HC_aud.create_huffman_tree()
HC_aud.calculate_table_conversion()
compressed_text_aud = HC_aud.get_compressed_aud()  # Cambiado a get_compressed_img

# Imprimir resultados para la imagen
print("\nImagen original:", HC_aud.original_text)
print("Imagen comprimida:", compressed_text_aud)

# Decodificar la imagen comprimida
decoded_text_aud = HC_aud.decompress_aud(compressed_text_aud)
print("Imagen reconstruida: ", decoded_text_aud, "\n")

# Guardar el archivo comprimido de imagen
with open(compressed_text_aud, 'w') as file:
    file.write(compressed_text_aud)

          
# VIDEOOOO

original_text_path= r'C:\Users\1123122549\OneDrive - up.edu.mx\Documentos\UP\ESTRUCTURAS II\COMPRESOR\Prueba1.mp4'

HC_vid = HuffmanCoding()
HC_vid.set_original_img(original_text_path)  
HC_vid.calculate_frequency_table()
HC_vid.create_huffman_tree()
HC_vid.calculate_table_conversion()
compressed_text_vid = HC_vid.get_compressed_vid()

print("\nImagen original:", HC_vid.original_text)
print("Imagen comprimida:", compressed_text_vid)

decoded_text_aud = HC_vid.decompress_vid(compressed_text_vid)
print("Imagen reconstruida: ", decoded_text_aud, "\n")

# Guardar el archivo comprimido de imagen
with open(compressed_text_vid, 'w') as file:
    file.write(compressed_text_vid)