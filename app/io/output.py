from typing import Any

import pandas


def output_in_console(data: Any) -> None:
    """Prints the given data to the console.

    Args:
        data (Any): The data to be printed. Can be of any type
            (str, int, dict, etc.).
    """
    print(data)


def output_in_file(file_path: str, data: str) -> None:
    """Writes a string to a text file.

    Overwrites the file if it already exists.

    Args:
        file_path (str): The path to the file where data will be written.
        data (str): The string data to write into the file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)


def output_in_file_pandas(dataframe: pandas.DataFrame, file_path: str) -> None:
    """Saves a pandas DataFrame to a CSV file.

    Args:
        dataframe (pd.DataFrame): The pandas DataFrame object to save.
        file_path (str): The destination path for the new CSV file.
    """
    dataframe.to_csv(file_path, index=False)