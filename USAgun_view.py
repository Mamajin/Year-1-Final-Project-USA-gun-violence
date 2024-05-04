"""This View represents the user interface.
This displays the dat from the Model and sends user inputs to the Controller"""

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class UsaGVView(tk.Frame):
    def __init__(self, root):
        super().__init__()
        self.root = root
        # Main page components
        self.init_components()

    def init_components(self):
        """Initialize components"""
        font = ('Helvetica', 14)
        self.option_add('*Font', font)
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
        self.confirm_button = tk.Button(self.root, text="Confirm",
                                        bg="light green")
        self.confirm_button.grid(row=8, column=10, padx=5, pady=5,
                                 sticky="news")

        # Clear display
        self.clear_button = tk.Button(self.root, text="Clear")
        self.clear_button.grid(row=8, column=11, padx=5, pady=5,
                               sticky="news")

        # Information selector
        self.info_selector = tk.Listbox(self.root)
        self.info_selector.grid(row=0, column=8, padx=8, pady=8,
                                columnspan=4, rowspan=6,
                                sticky="news")

    def information_detail(self):
        info_detail = tk.Label(text="Information about the chosen information",
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
            self.info_selector.insert(tk.END, option)

    def make_graph_plotter(self):
        """Plot a graph with the given data."""
        # Create Matplotlib figure and axis
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        # Create a canvas to display the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10,
                                         columnspan=7, rowspan=4,
                                         sticky="news")

    def update_graph(self, attribute_x, attribute_y):
        """Update the graph"""
        self.ax.clear()
        self.ax.plot(attribute_x, attribute_y)
        self.ax.set_xlabel('X Label')
        self.ax.set_ylabel('Y Label')
        self.ax.set_title('Graph Title')
        self.canvas.draw()
