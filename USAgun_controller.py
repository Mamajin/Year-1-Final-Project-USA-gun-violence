"""The Controller handles user input and updates the Model accordingly.
It also updates the View based on changes in the Model"""
import matplotlib.pyplot as plt


class UsaGVController:
    def __init__(self, root, model, view):
        self.root = root
        self.model = model
        self.view = view

        self.view.confirm_button.config(command=self.on_confirm)
        self.view.clear_button.config(command=self.on_clear)

        self.info_options = [
            "Age Group Distribution",
            "Incident Locations",
            "Incident Severity"
        ]
        self.view.set_info_options(self.info_options)

    def on_confirm(self):
        selected_info = self.view.info_selector.curselection()
        if selected_info:
            selected_info_index = selected_info[0]
            info_type = self.info_options[selected_info_index]
            if info_type == "Age Group Distribution":
                age_distribution = self.model.get_shooter_age_distribution()
                self.update_graph("Age Group Distribution",
                                  "Age Group", age_distribution.keys(),
                                  "Frequency", age_distribution.values())

            elif info_type == "Incident Locations":
                locations = self.model.get_incident_locations()
                print("Incident Locations:", locations)
            elif info_type == "Incident Severity":
                severity = self.model.get_incident_severity()
                print("Incident Severity:", severity)

    def update_graph(self, title,
                     x_label, attribute_x,
                     y_label, attribute_y):
        """Update the graph"""
        self.view.ax.clear()
        self.view.ax.bar(attribute_x, attribute_y)
        self.view.ax.set_xlabel(x_label)
        self.view.ax.set_xticklabels(attribute_x, rotation=10)
        self.view.ax.set_ylabel(y_label)
        self.view.ax.set_title(title)
        self.view.canvas.draw()

    def update_information_text(self):
        """Update the information text box below the graph"""
        pass


    def on_clear(self):
        """Clears graph display and graph information"""
        print("Clearing information...")
        self.view.ax.clear()
        self.view.canvas.draw()
