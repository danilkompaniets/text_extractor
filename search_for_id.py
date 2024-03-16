import pandas as pd

class IDFinder:
    def __init__(self, csv_file_path):
        self.df = pd.read_csv(csv_file_path, delimiter=";")

    def get_id(self, desired_value):
        """Retrieve the ID from the DataFrame based on the desired value."""
        column_name = 'Артикул2'
        column_id = "Код"

        desired_value_cleaned = desired_value.strip().upper()  # Remove leading/trailing whitespace and convert to uppercase

        # Case insensitive matching
        search_result = self.df[self.df[column_name].str.strip().str.upper() == desired_value_cleaned]

        if search_result.empty:
            print(f"No matching row found for {desired_value}")
            return None

        row = search_result.index[0]
        value_in_specific_row = self.df.loc[row, column_id]

        return value_in_specific_row

