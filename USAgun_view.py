"""This View represents the user interface.
This displays the dat from the Model and sends user inputs to the Controller"""

import tkinter as tk


class UsaGVView(tk.Frame):
    def __init__(self, root):
        super().__init__()
        # Main page components
        self.display_label = self.empty_graph_display()
        self.display_label.grid(row=0, column=0, padx=10, pady=10,
                                columnspan=6, rowspan=4,
                                sticky="news")

        self.information_box = self.information_detail()
        self.information_box.grid(row=4, column=0, padx=10, pady=10,
                                  columnspan=6, rowspan=3,
                                  sticky="news")

        self.confirm_button = tk.Button(root, text="Confirm", bg="light green")
        self.confirm_button.grid(row=6, column=8, padx=5, pady=5,
                                 sticky="news")

        self.clear_button = tk.Button(root, text="Clear")
        self.clear_button.grid(row=6, column=9, padx=5, pady=5,
                               sticky="news")

        self.info_selector = tk.Listbox(root)
        self.info_selector.grid(row=0, column=6, padx=10, pady=10,
                                columnspan=4, rowspan=6,
                                sticky="news")

    def empty_graph_display(self):
        """Creates an empty display for graphs to be show on"""
        display = tk.Label(text="Empty", bg="grey")
        return display

    def information_detail(self):
        info_detail = tk.Label(text="Information about the chosen information",
                               bg="grey")
        return info_detail

    def data_combobox(self, attributes):
        """Creates a combobox for the data attributes"""
        pass

    def set_info_options(self, options):
        """Set options for information selector."""
        self.info_selector.delete(0, tk.END)
        for option in options:
            self.info_selector.insert(tk.END, option)
