import webbrowser as wb
import tkinter as tk
import folium
import os

root = tk.Tk()
root.title("find_this   :)")
root.geometry("500x600")
root.resizable(False, False)

def get_entry():
    value_latitude = entry_1.get()
    value_longitude = entry_2.get()
    place = folium.Map(location=[value_latitude, value_longitude])
    try:
        os.remove("tut.html")
    except:
        pass
    place.save("tut.html")
    url = "tut.html"
    wb.open(url)

label_welcome = tk.Label(root, text="Enter coordinates",
                         font=("Arial", 20, "bold")
                         )

label_lat = tk.Label(root, text="Width -->",
                     font=("Arial", 20, "bold")
                     )

entry_1 = tk.Entry(root, font=("Arial", 12, "bold"))

label_long = tk.Label(root, text="Longitude -->",
                      font=("Arial", 20, "bold")
                      )

entry_2 = tk.Entry(root, font=("Arial", 12, "bold"))

butt_on = tk.Button(root, text="Show",
                    font=("Arial", 15, "bold"),
                    command=get_entry
                    )

label_me = tk.Label(root, text="by Reckson", fg="red")

label_welcome.place(x=120, y=65)
label_lat.place(x=40, y=220)
entry_1.place(x=240, y=220)
label_long.place(x=40, y=280)
entry_2.place(x=240, y=280)
butt_on.place(x=200, y=350)
label_me.place(x=400, y=550)

root.mainloop()
