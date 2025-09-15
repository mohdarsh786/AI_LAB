from PIL import Image
import numpy as np

img = Image.open(r"C:\Users\amssr\Downloads\image.jpg")
matrix = np.array(img)
print(matrix)