"""Model of calculator compose of the calculator component"""
import csv
from Statistic_calculator import StatisticalCalculator


class UsaGVModel:
    """Program model class that keeps all the functions of the program."""

    def __init__(self):
        self.data = self.convert_to_dict('shooting_data.csv')
        self.data_key = self.get_attribute_name()
        self.stat_cal = StatisticalCalculator(self.data)

    @staticmethod
    def convert_to_dict(csv_file):
        """Convert CSV file to a list of dictionaries."""
        data = []
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(dict(row))
        return data

    def get_attribute_name(self):
        """Returns the attributes of the data."""
        key_ls = []
        for key in self.data[0].keys():
            key_ls.append(key)
        return key_ls

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
        location_dist = {}
        for event in self.data:
            location = event['location.1']
            if location in location_dist:
                location_dist[location] += 1
            else:
                location_dist[location] = 1
        return location_dist

    def get_shooter_age_distribution(self):
        """Get the distribution of shooter ages."""
        age_group_distribution = {}
        for event in self.data:
            age_group = event['age_group']
            if age_group in age_group_distribution:
                age_group_distribution[age_group] += 1
            else:
                age_group_distribution[age_group] = 1
        return age_group_distribution

    def get_incident_severity(self):
        """Get the severity of each incident."""
        severity = {}
        for event in self.data:
            severity[event['case']] = event['total_victims']
        return severity
