"""This View represents the user interface.
This displays the dat from the Model and sends user inputs to the Controller"""

import tkinter as tk


class UsaGVView(tk.Frame):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title("USA Gun Violence Database Navigator")

        # Main page components
        self.display_label = tk.Label(root,
                                      text="Display of the chosen information")
        self.display_label.pack()

        self.information_label = tk.Label(root,
                                          text="Information about the chosen information")
        self.information_label.pack()

        self.confirm_button = tk.Button(root, text="Confirm")
        self.confirm_button.pack()

        self.clear_button = tk.Button(root, text="Clear")
        self.clear_button.pack()

        self.info_selector = tk.Listbox(root)
        self.info_selector.pack()

    def set_info_options(self, options):
        """Set options for information selector."""
        self.info_selector.delete(0, tk.END)
        for option in options:
            self.info_selector.insert(tk.END, option)

    def run(self):
        self.root.mainloop()