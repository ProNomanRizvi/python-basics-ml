import os
from src.loader import DataLoader
from src.cleaner import DataCleaner
from src.normalizer import DataNormalizer
from src.reporter import Reporter


def main():
    print("=== ML Preprocessing Engine ===\n")

    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Step 1: Load
    print("[LOADER]")
    loader = DataLoader("DataLoader")
    loader.load_from_file(os.path.join(script_dir, "data/raw_data.txt"))
    loader.process()
    print(f"Valid records loaded: {len(loader)}")
    print(f"Rejected: {loader.get_rejected_count()}\n")

    # Step 2: Clean
    print("[CLEANER]")
    cleaner = DataCleaner()
    cleaner.load(loader.get_result())
    cleaner.process()
    print(f"Duplicates removed: {cleaner.get_duplicates_removed()}")
    print(f"Outliers removed  : {cleaner.get_outliers_removed()}")
    print(f"Records remaining : {len(cleaner)}\n")

    # Step 3: Normalize
    print("[NORMALIZER]")
    normalizer = DataNormalizer()
    normalizer.load(cleaner.get_result())
    normalizer.process()
    print(f"Original Min: {normalizer.get_min()}")
    print(f"Original Max: {normalizer.get_max()}")
    print(f"Normalized {len(normalizer)} records.\n")

    # Step 4: Report
    print("[REPORT]")
    reporter = Reporter()
    reporter.generate(normalizer.get_result(), name="Final Report")

    # Step 5: Save
    report_path = os.path.join(script_dir, "data/report.txt")
    reporter.save_to_file(normalizer.get_result(), report_path)
    print(f"\nReport saved to {report_path}")


if __name__ == "__main__":
    main()