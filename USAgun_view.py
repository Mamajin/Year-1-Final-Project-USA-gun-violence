"""
This View represents the user interface.
This displays the dat from the Model and sends user inputs to the Controller.
"""

import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class UsaGVView(ctk.CTkScrollableFrame):
    """
    Program view class that keeps all the visual components of the program.
    """

    def __init__(self, root, model):
        super().__init__(root)
        self.root = root
        self.model = model
        # StringVar for information text
        self.information_text = tk.StringVar(self.root, "None")
        # Font sets here
        self.tick_font = {'weight': 'normal',
                          'size': 12}
        self.label_font = {'weight': 'normal',
                           'size': 14}
        self.button_font = ("Impact", 20)
        self.detail_font = ("Helvetica", 16)
        # Main page components
        self.init_components()

    def init_components(self):
        """
        Initialize components in the program.
        """
        font = ('Helvetica', 24)
        self.option_add('*Font', font)

        # Menu box
        self.menu_box = self.make_menu_box()

        # Graph plot
        self.graph_display = self.make_graph_plotter()

        # Information about the displaying attribute
        self.information_box = self.information_detail()
        self.information_box.grid(row=6, column=0, padx=8, pady=8,
                                  columnspan=9, rowspan=4,
                                  sticky="news")

        # Combobox to select hue
        self.combobox_hue = ttk.Combobox(self.root)
        self.combobox_hue.grid(row=8, column=9, padx=5, pady=5,
                               columnspan=2, sticky="news")
        self.update_hue_combobox()
        self.combobox_hue.bind("<MouseWheel>", self.disable_mousewheel)
        self.combobox_hue.bind("<<ComboboxSelected>>", self.on_hue_selected)

        # Confirm button
        self.confirm_button = ctk.CTkButton(self.root, text="Confirm",
                                            fg_color="SpringGreen3",
                                            text_color="black",
                                            hover_color="light green",
                                            corner_radius=32,
                                            font=self.button_font)
        self.confirm_button.grid(row=9, column=9, padx=5, pady=5,
                                 sticky="news")

        # Clear button
        self.clear_button = ctk.CTkButton(self.root, text="Clear",
                                          fg_color="light grey",
                                          text_color="black",
                                          hover_color="grey",
                                          corner_radius=32,
                                          font=self.button_font)
        self.clear_button.grid(row=9, column=10, padx=5, pady=5,
                               sticky="news")

        # Information selector
        self.info_selector = tk.Listbox(self.root)
        self.info_selector.grid(row=0, column=9, padx=10, pady=10,
                                columnspan=4, rowspan=7,
                                sticky="news")

    def information_detail(self):
        """
        Information text that uses a text-variable.
        :returns information detail box
        """
        info_detail = ctk.CTkLabel(self.root,
                                   textvariable=self.information_text,
                                   fg_color="white", anchor="nw",
                                   justify=tk.LEFT, corner_radius=8,
                                   font=self.detail_font, text_color="black")
        return info_detail

    def make_menu_box(self):
        """
        Creates a Menu.
        """
        menu_box = tk.Menu()
        self.root.config(menu=menu_box)
        menu_box.add_command(label='Exit', command=self.quit)

    def set_info_options(self, options):
        """
        Set options for information selector.
        :param options: options for the selector
        """
        self.info_selector.delete(0, tk.END)
        for option in options:
            self.info_selector.insert(tk.END, f" ⭕ {option}")

    def update_hue_combobox(self):
        """
        Updates hue combobox with data attributes
        :return:
        """
        self.combobox_hue['values'] = self.model.get_hue_attributes()

    def disable_mousewheel(self, event):
        """
        Disable mousewheel to prevent error message
        :param event:
        :return:
        """
        event.widget.unbind_all("<MouseWheel>")

    def on_hue_selected(self, event):
        """
        Sends the selected data attribute to controller
        :param event:
        :return:
        """
        selected_hue = self.combobox_hue.get()
        # Notify hue to controller
        self.controller.on_hue_selected(selected_hue)

    def make_graph_plotter(self):
        """
        Plot a blank graph that will be later changed when the user
        selects a data to view.
        """
        # Create a frame to contain the canvas and scrollbar
        self.graph_frame = ttk.Frame(self.root)
        self.graph_frame.grid(row=0, column=0, padx=10, pady=10,
                              columnspan=9, rowspan=6, sticky="news")

        # Create Matplotlib figure and axis
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        # Create a canvas to display the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,
                                         expand=True)
