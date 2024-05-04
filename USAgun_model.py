"""Model of calculator compose of the calculator component"""
import csv

import pandas as pd

from Statistic_calculator import StatisticalCalculator


class UsaGVModel:
    """Program model class that keeps all the functions of the program."""

    def __init__(self):
        self.data = pd.read_csv('shooting_data.csv')
        self.data['date'] = pd.to_datetime(self.data['date'])
        self.stat_cal = StatisticalCalculator(self.data)

    def get_statistical_values(self, key):
        """Returns the statistical values of a numerical attribute.
        The returned values are the following in order
        mean, median, mode, min, max, variance, standard deviation"""
        return [
            self.stat_cal.calculate_mean(key),
            self.stat_cal.calculate_median(key),
            self.stat_cal.calculate_mode(key),
            self.stat_cal.calculate_min(key),
            self.stat_cal.calculate_variance(key),
            self.stat_cal.calculate_standard_deviation(key),
        ]

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
