from .base_pipeline import BasePipeline


class DataCleaner(BasePipeline):

    def __init__(self):
        super().__init__("DataCleaner")
        self._removed_count = 0
        self._duplicates_removed = 0
        self._outliers_removed = 0

    def process(self):
        if not self._data:
            print("No data to clean")
            return

        # Remove duplicates
        initial_length = len(self._data)
        self._data = list(set(self._data))
        self._duplicates_removed = initial_length - len(self._data)

        # Remove outliers manually
        mean = sum(self._data) / len(self._data)
        variance = sum((x - mean) ** 2 for x in self._data) / len(self._data)
        std_dev = variance ** 0.5
        lower_bound = mean - 1.5 * std_dev
        upper_bound = mean + 1.5 * std_dev

        cleaned = []
        for value in self._data:
            if lower_bound <= value <= upper_bound:
                cleaned.append(value)
            else:
                self._outliers_removed += 1

        self._data = cleaned
        self._removed_count = self._duplicates_removed + self._outliers_removed
        self._processed = True

    def get_removed_count(self):
        return self._removed_count

    def get_duplicates_removed(self):
        return self._duplicates_removed

    def get_outliers_removed(self):
        return self._outliers_removed