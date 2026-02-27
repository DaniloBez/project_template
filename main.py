from app.io.input import *
from app.io.output import *


def main():
    data_console = input_from_console("Введіть тестовий рядок: ")

    try:
        data_text_file = input_from_file("input.txt")
    except FileNotFoundError:
        data_text_file = "Помилка: Файл input.txt не знайдено."

    try:
        data_pandas = input_from_file_pandas("data.csv")
        data_pandas_str = data_pandas.to_string()
    except FileNotFoundError:
        data_pandas_str = "Помилка: Файл data.csv не знайдено."

    output_in_console("Дані з консолі:")
    output_in_console(data_console)

    output_in_console("\nДані з текстового файлу:")
    output_in_console(data_text_file)

    output_in_console("\nДані з Pandas CSV:")
    output_in_console(data_pandas_str)

    final_output = (
        f"Дані з консолі:\n{data_console}\n\n"
        f"Дані з текстового файлу:\n{data_text_file}\n\n"
        f"Дані з Pandas CSV:\n{data_pandas_str}\n"
    )

    output_in_file("final_results.txt", final_output)

if __name__ == '__main__':
    main()
