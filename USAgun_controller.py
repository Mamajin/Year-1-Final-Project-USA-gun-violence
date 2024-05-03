"""The Controller handles user input and updates the Model accordingly.
It also updates the View based on changes in the Model"""


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
                print("Age Group Distribution:", age_distribution)
            elif info_type == "Incident Locations":
                locations = self.model.get_incident_locations()
                print("Incident Locations:", locations)
            elif info_type == "Incident Severity":
                severity = self.model.get_incident_severity()
                print("Incident Severity:", severity)

    def on_clear(self):
        print("Clearing information...")
