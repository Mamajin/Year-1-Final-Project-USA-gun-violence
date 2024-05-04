"""The Controller handles user input and updates the Model accordingly.
It also updates the View based on changes in the Model"""
import pandas as pd


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
                locations['Other'] = locations.pop('Other')
                self.update_graph("Incident Locations",
                                  "Locations", locations.keys(),
                                  "Frequency", locations.values())
            elif info_type == "Incident Severity":
                severity = self.model.get_incident_severity()
                self.update_graph("Incident Severity",
                                  "Date", severity.keys(),
                                  "Count", severity.values())

    def update_graph(self, title,
                     x_label, attribute_x,
                     y_label, attribute_y):
        """Update the graph"""
        self.view.ax.clear()
        if title == "Age Group Distribution" or title == "Incident Locations":
            self.view.ax.bar(attribute_x, attribute_y, color='lightsalmon')
            self.view.ax.set_xlabel(x_label)
            self.view.ax.set_xticklabels(attribute_x)
            self.view.ax.set_ylabel(y_label)
            self.view.ax.set_title(title)
            self.view.canvas.draw()
        elif title == "Incident Severity":
            start_date = max(self.model.data['date'].min(), pd.Timestamp('2022-01-01'))
            end_date = min(self.model.data['date'].max(), pd.Timestamp('2022-12-31'))
            # Filter the data for the specified date range
            new_df = self.model.data[
                (self.model.data['date'] >= start_date) &
                (self.model.data['date'] <= end_date)]
            # Set the date column as the index
            self.model.data.set_index('date', inplace=True)
            # Define the periods
            periods = [(start_date, pd.Timestamp('2022-06-30')),
                       (pd.Timestamp('2022-07-01'), end_date)]
            print(self.model.data.head())
            # Plot each period separately
            # self.view.ax.figure(figsize=(12, 8))
            # for i, period in enumerate(periods, 1):
            #     self.view.ax.subplot(2, 1, i)  # Create subplots for each period
            #     start, end = period
            #     # Filter the data for the current period
            #     sliced_data = self.model.data.loc[start:end]
            #     # Group and aggregate the sliced data by date
            #     grouped_data = sliced_data.resample('D').sum()  # Resample to daily frequency and sum the values
            #     # Plot the graph for the current period
            #     self.view.ax.plot(grouped_data.index, grouped_data['injured'],
            #              label='Injuries', color='blue')
            #     self.view.ax.plot(grouped_data.index, grouped_data['fatalities'],
            #              label='Deaths', color='red')
            #     self.view.ax.plot(grouped_data.index, grouped_data['total_victims'],
            #              label='Total Victims', color='green')
            #     # Customize the plot
            #     self.view.ax.title(f'Gun Violence Incidents Over Time (Period {i})')
            #     self.view.ax.xlabel('Date')
            #     self.view.ax.ylabel('Count')
            #     self.view.ax.legend()
            #     self.view.ax.grid(True)

    def update_information_text(self, key):
        """Update the information text box below the graph"""
        pass

    def on_clear(self):
        """Clears graph display and graph information"""
        print("Clearing information...")
        self.view.ax.clear()
        self.view.canvas.draw()
