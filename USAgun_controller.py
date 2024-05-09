"""The Controller handles user input and updates the Model accordingly.
It also updates the View based on changes in the Model"""
import pandas as pd


class UsaGVController:
    def __init__(self, root, model, view):
        self.root = root
        self.model = model
        self.view = view

        self.view.confirm_button.configure(command=self.on_confirm)
        self.view.clear_button.configure(command=self.on_clear)

        self.info_options = [
            "Age Group Distribution",
            "Age Distribution",
            "Incident Locations",
            "Incident Severity",
            "Incident Heatmap",
            "Place holder option"
        ]
        self.view.set_info_options(self.info_options)

    def on_confirm(self):
        selected_info = self.view.info_selector.curselection()
        if selected_info:
            selected_info_index = selected_info[0]
            info_type = self.info_options[selected_info_index]
            if info_type == "Age Group Distribution":
                age_distribution = self.model.get_shooter_age_distribution()
                self.update_display(info_type,
                                    "Age Group", age_distribution.keys(),
                                    "Frequency", age_distribution.values())
            elif info_type == "Age Distribution":
                # fill in function here
                self.update_display(info_type,
                                    "Age", age_)
            # If information is Incident Locations
            elif info_type == "Incident Locations":
                locations = self.model.get_incident_locations()
                locations['Other'] = locations.pop('Other')
                self.update_display(info_type,
                                    "Locations", locations.keys(),
                                    "Frequency", locations.values())
            # If information is Incident Severity
            elif info_type == "Incident Severity":
                severity = self.model.get_incident_severity()
                self.update_display(info_type,
                                    "Date", severity.keys(),
                                    "Count", severity.values())

    def update_display(self, title,
                       x_label, attribute_x,
                       y_label, attribute_y):
        """Update the graph"""
        self.view.ax.clear()
        if title == "Age Group Distribution" or title == "Incident Locations":
            self.view.ax.bar(attribute_x, attribute_y, color='lightsalmon')
            self.view.ax.set_xlabel(
                x_label, fontdict=self.view.label_font)
            self.view.ax.set_xticklabels(
                attribute_x, fontdict=self.view.tick_font)
            self.view.ax.set_ylabel(
                y_label, fontdict=self.view.label_font)
            self.view.ax.set_title(title)
            self.view.canvas.draw()
            # Update information about the graph

        elif title == "Age Distribution":
            self.view.dist(attribute_x, attribute_y, color='light pink')
            self.view.ax.set_xlabel(x_label, fontdict=self.view.label_font)
            self.view.ax.set_xticklabels(
                attribute_x, fontdict=self.view.tick_font)
            self.view.ax.set_ylabel(attribute_y, fontdict=self.view.label_font)
            self.view.ax.set_title(title)
            self.view.canvas.draw()
            # Update information about the graph

        elif title == "Incident Severity":
            # Make dataframe copy
            df_copy = self.model.data.copy()
            # Convert the date column to datetime format and set it as the index
            df_copy['date'] = pd.to_datetime(df_copy['date'])
            df_copy.set_index('date', inplace=True)
            # Find the index of the row with the maximum fatalities
            max_fatalities_index = df_copy['fatalities'].idxmax()
            # Remove the row with the maximum fatalities
            data = df_copy.drop(index=max_fatalities_index)
            # Group and aggregate the data by date
            grouped_data = data.resample(
                'D').sum()  # Resample to daily frequency and sum the values
            # Plot the graph
            self.view.ax.plot(grouped_data.index, grouped_data['injured'],
                              label='Injuries', color='blue')
            self.view.ax.plot(grouped_data.index, grouped_data['fatalities'],
                              label='Deaths', color='red')
            self.view.ax.plot(grouped_data.index,
                              grouped_data['total_victims'],
                              label='Total Victims', color='green')
            # Customize the plot
            self.view.ax.set_title(
                'Gun Violence Incidents Over Time (Excluding Maximum '
                'Fatalities)')
            self.view.ax.set_xlabel(x_label, fontdict=self.view.label_font)
            self.view.ax.set_ylabel(y_label, fontdict=self.view.label_font)
            self.view.ax.legend()
            self.view.canvas.draw()
            # Update information text
            self.update_information_text('injured', 'numerical')

    def update_information_text(self, key, dtype):
        """Update the information text box below the graph"""
        if dtype == "numerical":
            return self.view.information_text.set(
                self.model.get_statistical_fstring(key))
        if dtype == "ordinal":
            pass

    def on_clear(self):
        """Clears graph display and graph information"""
        print("Clearing information...")
        self.view.ax.clear()
        self.view.canvas.draw()
        self.view.information_text.set("Empty")
