"""Model of calculator compose of the calculator component"""
import csv


class UsaGVModel:
    """Program model class that keeps all the functions of the program."""
    def __init__(self):
        self.data = self.convert_to_dict('shooting_data.csv')
        self.data_key = self.get_attribute_name()

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

    def filter_by_age_group(self, age_group):
        """Filter data by age group of the shooter."""
        return [event for event in self.data if event['age_group'] == age_group]

    def get_incident_locations(self):
        """Get unique incident locations."""
        return list(set(event['location'] for event in self.data))

    def get_shooter_age_distribution(self):
        """Get the distribution of shooter ages."""
        age_distribution = {}
        for event in self.data:
            age = event['age_of_shooter']
            if age in age_distribution:
                age_distribution[age] += 1
            else:
                age_distribution[age] = 1
        return age_distribution

    def get_incident_severity(self):
        """Get the severity of each incident."""
        severity = {}
        for event in self.data:
            severity[event['case']] = event['total_victims']
        return severity

