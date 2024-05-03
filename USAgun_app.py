import tkinter as tk
from USAgun_model import UsaGVModel
from USAgun_controller import UsaGVController
from USAgun_view import UsaGVView

if __name__ == "__main__":
    root = tk.Tk()
    # root.columnconfigure(0, weight=1)
    # root.rowconfigure(0, weight=1)
    # MVC components
    model = UsaGVModel
    view = UsaGVView(root)
    controller = UsaGVController(root, model, view)
    # Root component
    root.title("USA Gun Violence Database Navigator")
    # Alternate size: 600x400, Intended size: 1200x800
    root.geometry('1100x700')
    root.columnconfigure(tuple(range(11)), weight=1)
    root.rowconfigure(tuple(range(8)), weight=1)
    root.mainloop()
