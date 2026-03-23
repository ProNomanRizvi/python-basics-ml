from .base_pipeline import BasePipeline


class DataNormalizer(BasePipeline):

    def __init__(self):
        super().__init__("DataNormalizer")
        self._min = None
        self._max = None

    def process(self):
        if not self._data:
            print("No data to normalize")
            return

        self._min = min(self._data)
        self._max = max(self._data)

        if self._max == self._min:
            self._data = [0.5] * len(self._data)
        else:
            self._data = [
                (x - self._min) / (self._max - self._min)
                for x in self._data
            ]

        self._processed = True

    def get_min(self):
        return self._min

    def get_max(self):
        return self._max