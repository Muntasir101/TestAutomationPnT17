import pandas as pd


def read_test_data(excel_file, sheet_name):
    data = pd.read_excel(excel_file, sheet_name=sheet_name)
    return data
