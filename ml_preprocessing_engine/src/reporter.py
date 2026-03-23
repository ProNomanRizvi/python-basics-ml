class Reporter:
    def generate(self, data, name="Report"):
        total_records = len(data)
        min_value = min(data) if data else None
        max_value = max(data) if data else None
        average = sum(data) / total_records if total_records > 0 else None
        first_five = data[:5]
        last_five = data[-5:]

        print(f"{name}:")
        print(f"Total Records: {total_records}")
        print(f"Min: {min_value}")
        print(f"Max: {max_value}")
        print(f"Average: {average}")
        print(f"First 5 values: {first_five}")
        print(f"Last 5 values: {last_five}")

    def save_to_file(self, data, filepath):
        total_records = len(data)
        min_value = min(data) if data else None
        max_value = max(data) if data else None
        average = sum(data) / total_records if total_records > 0 else None
        first_five = data[:5]
        last_five = data[-5:]

        with open(filepath, 'w') as file:
            file.write("Report:\n")
            file.write(f"Total Records: {total_records}\n")
            file.write(f"Min: {min_value}\n")
            file.write(f"Max: {max_value}\n")
            file.write(f"Average: {average:.2f}\n")
            file.write(f"First 5 values: {first_five}\n")
            file.write(f"Last 5 values: {last_five}\n")