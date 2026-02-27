import pandas


def input_from_console(prompt: str = "Введіть дані: ") -> str:
    """Reads a string input from the user via the console.

    Args:
        prompt (str, optional): The text displayed to the user before input.
            Defaults to "Введіть дані: ".

    Returns:
        str: The string entered by the user.
    """
    return input(prompt)


def input_from_file(file_path: str) -> str:
    """Reads the entire content of a standard text file.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a single string.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def input_from_file_pandas(file_path: str) -> pandas.DataFrame:
    """Reads data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the parsed data.

    Raises:
        FileNotFoundError: If the specified CSV file does not exist.
    """
    return pandas.read_csv(file_path)