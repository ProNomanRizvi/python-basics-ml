class BasePipeline:

    def __init__(self, name):
        self._name = name
        self._data = []
        self._processed = False

    def load(self, data):
        if not isinstance(data, list) or len(data) == 0:
            print("Invalid input. Provide a non-empty list.")
            return
        self._data.extend(data)
        print(f"Loaded {len(data)} records into {self._name}")
        

    def process(self):
        raise NotImplementedError("Subclasses must implement the process method")

    def get_result(self):
        if not self._processed:
            print("Not processed yet")
            return None
        return self._data.copy()

    def summary(self):
        print(f"\n--- Summary: {self._name} ---")
        print(f"Size      : {len(self._data)}")
        print(f"Processed : {self._processed}")

    def __str__(self):
        return f"Pipeline: {self._name} | Size: {len(self._data)} | Processed: {self._processed}"
    
    def __len__(self):
        return len(self._data)
    
class NormalizePipeline(BasePipeline):

    def __init__(self, name):
        super().__init__(name)
        self._min = None
        self._max = None

    def get_min(self):
        return self._min

    def get_max(self):
        return self._max

    def process(self):
        if not self._data:
            print("No records to process")
            return
        
        self._min = min(self._data)
        self._max = max(self._data)

        if self._max == self._min:
            print("All values are the same. Normalization is not possible.")
            return
        
        self._data = [(value - self._min) / (self._max - self._min) for value in self._data]
        self._processed = True

class CleanPipeline(BasePipeline):

    def __init__(self, name):
        super().__init__(name)
        self._removed_count = 0

    def get_removed_count(self):
        return self._removed_count

    def process(self):
        if not self._data:
            print("No records to process")
            return
        
        mean = sum(self._data) / len(self._data)
        variance = sum((value - mean) ** 2 for value in self._data) / len(self._data)
        std_dev = variance ** 0.5

        lower_bound = mean - 1.5 * std_dev
        upper_bound = mean + 1.5 * std_dev

        cleaned_data = [value for value in self._data if lower_bound <= value <= upper_bound]
        self._removed_count = len(self._data) - len(cleaned_data)
        self._data = cleaned_data
        self._processed = True


if __name__ == "__main__":
    raw = [10, 200, 30, 400, 50, 1000, 60]

    n = NormalizePipeline("NormPipeline")
    n.load(raw)
    n.process()
    print(n.get_result())
    print(n)

    c = CleanPipeline("CleanPipeline")
    c.load(raw)
    c.process()
    print(c.get_result())
    print(f"Removed: {c.get_removed_count()}")