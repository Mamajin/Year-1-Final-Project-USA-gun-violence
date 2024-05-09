"""Model of calculator compose of the calculator component"""
import csv

import pandas as pd
import numpy as np


class UsaGVModel:
    """Program model class that keeps all the functions of the program."""

    def __init__(self):
        self.data = pd.read_csv('shooting_data.csv')
        self.data['date'] = pd.to_datetime(self.data['date'])

    def get_statistical_fstring(self, key):
        """Returns strings of statistical values from a given statistic dict"""
        f_stat_value = (f" Statistical Values of {key}:\n"
                        f" ▪️Mean: {round(self.data[key].mean(), 2)}\n"
                        f" ▪️Median: {round(self.data[key].median(), 2)}\n"
                        f" ▪️Mode: {round(self.data[key].mode()[0], 2)}\n"
                        f" ▪️Min: {round(self.data[key].min(), 2)}\n"
                        f" ▪️Max: {(self.data[key].max())}\n"
                        f" ▪️Std: {round(self.data[key].std(), 2)}")
        return f_stat_value

    def get_ordinal_stat_fstring(self, key):
        """Returns Ordinals statistic of data"""
        new_df = self.data.copy()
        ordinal_values = self.data[key].unique()
        new_df.ordinal_val = pd.Categorical(
            new_df.ordinal_val, ordinal_values, ordered=True)
        median_value = np.median(new_df[""])

    def filter_by_age_group(self, age_group):
        """Filter data by age group of the shooter."""
        return [event for event in self.data if
                event['age_group'] == age_group]

    def get_incident_locations(self):
        """Get unique incident locations."""
        return self.data['location.1'].value_counts().to_dict()

    def get_shooter_age_distribution(self):
        """Get the distribution of shooter ages."""
        return self.data['age_group'].value_counts().to_dict()

    def get_incident_severity(self):
        """Get the severity of each incident."""
        return self.data.groupby('date').agg({
            'injured': 'sum',
            'fatalities': 'sum',
            'total_victims': 'sum'
        }).to_dict()

