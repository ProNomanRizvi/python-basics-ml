class DataSet:
    def __init__(self, name, max_size):
        self._name = name
        self._data = []
        self._max_size = max_size

    def add_record(self, value):
        if not isinstance(value, (int, float)):
            print(f"Rejected '{value}': not a number")
            return False

        if self.is_full():
            print(f"Rejected {value}: dataset is full")
            return False

        if value in self._data:
            print(f"Rejected {value}: duplicate")
            return False

        self._data.append(value)
        print(f"Added: {value}")
        return True

    def get_data(self):
        return self._data.copy()

    def get_size(self):
        return len(self._data)

    def is_full(self):
        return len(self._data) >= self._max_size

    def summary(self):
        print(f"\n--- Summary: {self._name} ---")

        if not self._data:
            print("No records in dataset")
            return

        avg = sum(self._data) / len(self._data)

        print(f"Size    : {self.get_size()}/{self._max_size}")
        print(f"Min     : {min(self._data)}")
        print(f"Max     : {max(self._data)}")
        print(f"Average : {avg:.2f}")

    def __str__(self):
        return f"DataSet: {self._name} | Records: {self.get_size()}/{self._max_size}"

    def __repr__(self):
        return f"DataSet(name='{self._name}', size={self.get_size()}, max_size={self._max_size})"

    def __len__(self):
        return len(self._data)


# ---------------- CLI SYSTEM ---------------- #

def get_number_from_user():
    value = input("Enter a number (or 'q' to quit): ")

    if value.lower() == 'q':
        return None

    try:
        return float(value)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return "invalid"


def run_dataset_app():
    name = input("Enter dataset name: ")
    max_size = int(input("Enter max size: "))

    ds = DataSet(name, max_size)

    print("\nStart entering data...\n")

    while not ds.is_full():
        value = get_number_from_user()

        if value is None:
            break

        if value == "invalid":
            continue

        ds.add_record(value)

    print("\nFinal Output:")
    print(ds)
    print(repr(ds))
    print(f"Length: {len(ds)}")
    ds.summary()


# Run program
if __name__ == "__main__":
    run_dataset_app()