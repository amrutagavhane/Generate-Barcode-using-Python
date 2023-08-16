# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:10:32 2023

@author: admin
"""

import barcode
from barcode.writer import ImageWriter
from PIL import Image

def generate_barcode(code):
    # Set the barcode format to UPC
    barcode_format = barcode.get_barcode_class("upc")
    
    # Generate the barcode and render as an image
    my_barcode = barcode_format(code, writer=ImageWriter())
    
    # Save the barcode as PNG
    file_name = f"generated_barcode_{code}.png"
    my_barcode.save(file_name)
    
    print(f"Barcode generated and saved as '{file_name}'")

def main():
    try:
        number = input("Enter the code to generate barcode: ")
        generate_barcode(number)
        
        # Open and display the generated barcode image
        image = Image.open(f"generated_barcode_{number}.png")
        image.show()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
