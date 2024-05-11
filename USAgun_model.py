"""
Model of calculator compose of the calculator component
"""

import pandas as pd


class UsaGVModel:
    """
    Program model class that keeps all the functions of the program.
    """

    def __init__(self):
        self.data = pd.read_csv('shooting_data.csv')
        self.original_data = self.data.copy()
        self.data['date'] = pd.to_datetime(self.data['date'])
        # Hue attributes for combobox
        self.hue_attributes = ["age_group", "location.1",
                               "prior_signs_mental_health_issues",
                               "weapons_obtained_legally", "gender",
                               "day_of_week", "decade"]

    def get_hue_attributes(self):
        """
        Returns attribute list
        :return list of attributes:
        """
        return self.hue_attributes

    def get_statistical_fstring(self, key):
        """
        Returns strings of statistical values from a given statistic dict
        :param key: key of the data needed
        :return: statistic values in a single string
        """
        f_stat_value = (f"\n"
                        f"Statistical Values of {key}\n"
                        f"▪️Mean: {round(self.data[key].mean(), 2)}\n"
                        f"▪️Median: {round(self.data[key].median(), 2)}\n"
                        f"▪️Mode: {round(self.data[key].mode()[0], 2)}\n"
                        f"▪️Min: {round(self.data[key].min(), 2)}\n"
                        f"▪️Max: {(self.data[key].max())}\n"
                        f"▪️Std: {round(self.data[key].std(), 2)}")
        return f_stat_value

    def get_ordinal_stat_fstring(self, key):
        """
        Returns Ordinals statistic of data
        :param key: key of the data needed
        :return: statistic values in a single string
        """
        new_df = self.data.copy()
        ordinal_values = self.data[key].unique()
        # Create string template
        ordinal_string = (f"\nStatistical Values of {key}\n"
                          f"▪️Mode: {self.data[key].mode()[0]}\n"
                          f"Percentages of unique values in {key}\n")
        # Get percentage of the data in string
        for value in ordinal_values:
            value_percent = round(
                new_df[key].value_counts()[value]/len(new_df.index) * 100, 2
            )
            ordinal_string = (
                    ordinal_string +
                    f"▪️percentage of {value}: {value_percent}%\n"
            )
        return ordinal_string

    def filter_by_age_group(self, age_group):
        """
        Filter data by age group of the shooter.
        :param age_group: age groups
        :return: age_group data
        """
        return self.data[self.data['age_group'] == age_group]

    def get_incident_locations(self):
        """
        Get unique incident locations.
        :return: unique location.1 counted
        """
        return self.data['location.1'].value_counts()

    def get_shooter_age_distribution(self):
        """
        Get the distribution of shooter ages.
        :return: distribution of shooter age
        """
        return self.data['age_group'].value_counts()

    def get_incident_severity(self):
        """
        Get the severity of each incident.
        :return: group data aggregated with 3 attributes
        """
        grouped_data = self.data.groupby('date').agg({
            'injured': 'sum',
            'fatalities': 'sum',
            'total_victims': 'sum'
        })
        return grouped_data
