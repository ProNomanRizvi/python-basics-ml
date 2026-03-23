from .base_pipeline import BasePipeline


class DataLoader(BasePipeline):

    def __init__(self, name):
        super().__init__(name)
        self._rejected_count = 0

    def load_from_file(self, filepath):
        self._data = []
        self._rejected_count = 0

        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    number = float(line)
                    self._data.append(number)
                except ValueError:
                    print(f"Rejected '{line}': not a number")
                    self._rejected_count += 1

    def get_rejected_count(self):
        return self._rejected_count

    def process(self):
        self._processed = True