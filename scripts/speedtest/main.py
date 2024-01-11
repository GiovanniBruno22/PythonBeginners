'''
SpeedTest using speedtest-cli, used tkinter for GUI
'''
import tkinter as tk
from tkinter import Tk
from tkinter import ttk
import speedtest
from decimal import Decimal
from PIL import Image, ImageTk

root = Tk()
root.title('SpeedTest 101')
root.geometry("300x500")
root.configure(bg="#9F9998")
root.resizable(False, False)

'''
check_speed() function will get trigerred after clicking SpeedTest Button
1. intiliaze an object of speedtest.SpeedTest()
2. Calculate downlaoding speed in Mbps
3. Calculate upload speed in Mbps
4. Calculate ping in ms
5. return it to respected labels
'''

def check_speed():

    check_speed_button.config(state=tk.DISABLED)
    quit_button.config(state=tk.DISABLED)

    st = speedtest.Speedtest()

    check_speed_button.config(state=tk.NORMAL)
    quit_button.config(state=tk.NORMAL)

    check_speed_button.config(state=tk.NORMAL)
    quit_button.config(state=tk.NORMAL)

    download_speed = Decimal(st.download()) / Decimal('1024') / Decimal('1024')
    download_speed = download_speed.quantize(Decimal('0.00'))

    upload_speed = Decimal(st.upload()) / Decimal('1024') / Decimal('1024')
    upload_speed = upload_speed.quantize(Decimal('0.00'))

    ping = st.results.ping

    download_label.config(text=f"Downoad Speed: {download_speed} Mbps")
    upload_label.config(text=f"Upload Speed: {upload_speed} Mbps")
    ping_label.config(text=f"Ping: {ping} ms")


'''
This function will resize the downlod logo, upload logo and ping logo to fit rows.
'''
def resize_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)


download_logo = resize_image('images/download_logo.png', 50, 50)
upload_logo = resize_image('images/upload_logo.png', 50, 50)
ping_logo = resize_image('images/ping_logo.png', 50, 50)


download_logo_label = tk.Label(root, image=download_logo)
download_logo_label.grid(row=0, column=0, padx=10, pady=10)
download_label = tk.Label(root, text="Click SpeedTest....")
download_label.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="", bg="#9F9998").grid(row=1) #add space of 1 row btw two sections

upload_logo_label = tk.Label(root, image=upload_logo)
upload_logo_label.grid(row=2, column=0, padx=10, pady=10)
upload_label = tk.Label(root, text="Click SpeedTest....")
upload_label.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="", bg="#9F9998").grid(row=3) #add space of 1 row btw two sections

ping_logo_label = tk.Label(root, image=ping_logo)
ping_logo_label.grid(row=4, column=0, padx=10, pady=10)
ping_label = tk.Label(root, text="Click SpeedTest....")
ping_label.grid(row=4, column=1, padx=10, pady=10)

#add space of 2 rows btw two sections
tk.Label(root, text="", bg="#9F9998").grid(row=5)
tk.Label(root, text="", bg="#9F9998").grid(row=6)


check_speed_button = ttk.Button(root, text='SpeedTest', command=check_speed) #this button will trigger check_speed() function initialzing speedTest
check_speed_button.grid(row=8, column=1, padx=7, pady=5, sticky='w')

tk.Label(root, text="", bg="#9F9998").grid(row=9) #add space of 1 row btw two sections

quit_button = ttk.Button(root, text="Quit", command=root.destroy) #quit button
quit_button.grid(row=10, column=1, padx=7, pady=5, sticky='w')


root.mainloop()
