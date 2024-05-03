import tkinter as tk
from USAgun_model import UsaGVModel
from USAgun_controller import UsaGVController
from USAgun_view import UsaGVView

if __name__ == "__main__":
    root = tk.Tk()

    model = UsaGVModel
    view = UsaGVView(root)
    controller = UsaGVController(root, model, view)
    root.title("USA Gun Violence")
    root.geometry('1100x700')
    view.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

# def main():
#     root = tk.Tk()
#     model = GunViolenceData(data)  # You need to replace 'data' with your actual dataset
#     view = View(root)
#     controller = Controller(root, model, view)
#     view.run()