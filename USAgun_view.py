"""This View represents the user interface.
This displays the dat from the Model and sends user inputs to the Controller"""

import tkinter as tk
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class UsaGVView(tk.Frame):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.information_text = tk.StringVar(self.root, "Empty")
        # Font set here
        self.tick_font = {'weight': 'normal',
                          'size': 12}
        self.label_font = {'weight': 'normal',
                           'size': 14}
        # Main page components
        self.init_components()

    def init_components(self):
        """Initialize components"""
        font = ('Helvetica', 22)
        self.option_add('*Font', font)
        # Progress bar

        # Menu box
        self.menu_box = self.make_menu_box()

        # Graph plot
        self.graph_display = self.make_graph_plotter()

        # Information about the displaying attribute
        self.information_box = self.information_detail()
        self.information_box.grid(row=6, column=0, padx=10, pady=10,
                                  columnspan=7, rowspan=3,
                                  sticky="news")

        # Confirm to choose the attribute
        self.confirm_button = ctk.CTkButton(self.root, text="Confirm",
                                            fg_color="green",
                                            text_color="black",
                                            hover_color="light green",
                                            corner_radius=32)
        self.confirm_button.grid(row=8, column=9, padx=5, pady=5,
                                 sticky="news")

        # Clear display
        self.clear_button = ctk.CTkButton(self.root, text="Clear",
                                          fg_color="light grey",
                                          text_color="black",
                                          hover_color="grey",
                                          corner_radius=32)
        self.clear_button.grid(row=8, column=10, padx=5, pady=5,
                               sticky="news")

        # Information selector
        self.info_selector = tk.Listbox(self.root)
        self.info_selector.grid(row=0, column=7, padx=8, pady=8,
                                columnspan=4, rowspan=7,
                                sticky="news")

    def information_detail(self):
        info_detail = tk.Label(textvariable=self.information_text,
                               bg="grey")
        return info_detail

    def make_menu_box(self):
        """Creates a Menu"""
        menu_box = tk.Menu()
        self.root.config(menu=menu_box)
        menu_box.add_command(label='Exit', command=self.quit)

    def set_info_options(self, options):
        """Set options for information selector."""
        self.info_selector.delete(0, tk.END)
        for option in options:
            self.info_selector.insert(tk.END, f" ⭕ {option}")

    def make_graph_plotter(self):
        """Plot a blank graph with the given data."""
        # Create Matplotlib figure and axis
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        # Create a canvas to display the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10,
                                         columnspan=7, rowspan=6,
                                         sticky="news")
