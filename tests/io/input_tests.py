import os
import unittest
import pandas

from app.io.input import input_from_file, input_from_file_pandas


class TestInputFromFIle(unittest.TestCase):
    def setUp(self):
        self.file_dir = "data/"
        self.test_txt_path = self.file_dir + "test_text.txt"
        self.empty_txt_path = self.file_dir + "empty_text.txt"
        self.test_csv_path = self.file_dir + "test_data.csv"
        self.missing_path = self.file_dir + "does_not_exist.txt"

        with open(self.test_txt_path, "w", encoding="utf-8") as f:
            f.write("Hello world!\nРядок 2")

        with open(self.empty_txt_path, "w", encoding="utf-8") as f:
            pass

        with open(self.test_csv_path, "w", encoding="utf-8") as f:
            f.write("name,age\nОлена,25\nІван,30")

    def tearDown(self):
        files_to_remove = [self.test_txt_path, self.empty_txt_path, self.test_csv_path]
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)

    def test_input_from_file_success(self):
        result = input_from_file(self.test_txt_path)
        expected = "Hello world!\nРядок 2"
        self.assertEqual(result, expected)

    def test_input_from_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            input_from_file(self.missing_path)

    def test_input_from_file_empty(self):
        result = input_from_file(self.empty_txt_path)
        self.assertEqual(result, "")


class TestInputFromFilePandas(unittest.TestCase):
    def setUp(self):
        self.file_dir = "data/"
        self.test_txt_path = self.file_dir + "test_text.txt"
        self.empty_txt_path = self.file_dir + "empty_text.txt"
        self.test_csv_path = self.file_dir + "test_data.csv"
        self.missing_path = self.file_dir + "does_not_exist.txt"

        with open(self.test_txt_path, "w", encoding="utf-8") as f:
            f.write("Hello world!\nРядок 2")

        with open(self.empty_txt_path, "w", encoding="utf-8") as f:
            pass

        with open(self.test_csv_path, "w", encoding="utf-8") as f:
            f.write("name,age\nОлена,25\nІван,30")

    def tearDown(self):
        files_to_remove = [self.test_txt_path, self.empty_txt_path, self.test_csv_path]
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)

    def test_input_from_file_pandas_success(self):
        df = input_from_file_pandas(self.test_csv_path)
        self.assertIsInstance(df, pandas.DataFrame)
        self.assertEqual(len(df), 2)

    def test_input_from_file_pandas_not_found(self):
        with self.assertRaises(FileNotFoundError):
            input_from_file_pandas(self.missing_path)

    def test_input_from_file_pandas_content(self):
        df = input_from_file_pandas(self.test_csv_path)

        expected_columns = ["name", "age"]
        self.assertListEqual(list(df.columns), expected_columns)

        self.assertEqual(df.iloc[0]["age"], 25)
        self.assertEqual(df.iloc[1]["name"], "Іван")


if __name__ == '__main__':
    unittest.main()
