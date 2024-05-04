import tkinter as tk
from USAgun_model import UsaGVModel
from USAgun_controller import UsaGVController
from USAgun_view import UsaGVView

if __name__ == "__main__":
    root = tk.Tk()
    # MVC components
    model = UsaGVModel()
    view = UsaGVView(root)
    controller = UsaGVController(root, model, view)
    # Root component
    root.title("USA Gun Violence Database Navigator")
    # Alternate size: 600x400, Intended size: 1200x800
    root.geometry('1320x720')
    root.columnconfigure(tuple(range(12)), weight=1)
    root.rowconfigure(tuple(range(10)), weight=1)
    root.mainloop()
