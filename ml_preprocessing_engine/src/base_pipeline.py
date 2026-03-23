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