import requests
import json
import tkinter as tk


def api():
    a = entry1.get()
    b = entry2.get()
    setbalance = f"https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&method=setbalance&user={a}&balance={b}"
    requests.get(setbalance)
    url = f"https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&user={a}"
    res = requests.get(url)
    json = res.json()
    for i in range(len(json)):
       if json[i]["id"] is None:
          label.config(text = "Error")
       else:
          label.config(text = json)

window = tk.Tk()
window.minsize(500, 200)
label = tk.Label()
entry1 = tk.Entry()
entry2 = tk.Entry()
button = tk.Button(
    text="registration",
    width=20,
    height=5,
    command=api
    )
    
label.pack()
entry1.pack()
entry2.pack()
button.pack()


window.mainloop()