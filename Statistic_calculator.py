"""This is a Statistical caculator. This class calculates the statistical value
of an attribute."""
import statistics


class StatisticalCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self, key):
        """Calculate the mean of the specified numerical attribute."""
        values = [entry[key] for entry in self.data if isinstance(entry[key], (int, float))]
        if values:
            return sum(values) / len(values)
        else:
            return None

    def calculate_median(self, key):
        """Calculate the median of the specified numerical attribute."""
        values = [entry[key] for entry in self.data if isinstance(entry[key], (int, float))]
        if values:
            return statistics.median(values)
        else:
            return None

    def calculate_mode(self, key):
        """Calculate the mode of the specified numerical attribute."""
        values = [entry[key] for entry in self.data if isinstance(entry[key], (int, float))]
        if values:
            return statistics.mode(values)
        else:
            return None

    def calculate_min(self, key):
        """Calculate the minimum value of the specified numerical attribute."""
        values = [entry[key] for entry in self.data if isinstance(entry[key], (int, float))]
        if values:
            return min(values)
        else:
            return None

    def calculate_max(self, key):
        """Calculate the maximum value of the specified numerical attribute."""
        values = [entry[key] for entry in self.data if isinstance(entry[key], (int, float))]
        if values:
            return max(values)
        else:
            return None

    def calculate_variance(self, key):
        """Calculate the variance of the specified numerical attribute."""
        values = [entry[key] for entry in self.data if isinstance(entry[key], (int, float))]
        if len(values) > 1:
            return statistics.variance(values)
        else:
            return None

    def calculate_standard_deviation(self, key):
        """Calculate the standard deviation of the specified numerical attribute."""
        values = [entry[key] for entry in self.data if isinstance(entry[key], (int, float))]
        if len(values) > 1:
            return statistics.stdev(values)
        else:
            return None
