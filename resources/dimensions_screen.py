import tkinter as tk

root = tk.Tk()

screenWidth = root.winfo_screenwidth() #* Ancho de pantalla
screenHeight = root.winfo_screenheight() #* Alto de pantalla

position_x = int(screenWidth * 0.25)
position_y = int(screenHeight * 0.25)
position_w = int(screenWidth * 0.50)
position_h = int(screenHeight * 0.50)