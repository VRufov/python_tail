import os
import unittest

from tail import tail, check_file
from exceptions import IsNotFile


TEST_FILE = "test.csv"


class TestTailProgram(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(TEST_FILE, "w") as file:
            file_content = "\n".join(map(str, list(range(20))))
            file.write(file_content)

    @classmethod
    def tearDownClass(cls):
        os.remove(TEST_FILE)

    def test_tail_default(self):
        with open(TEST_FILE, "rb") as file:
            actual = tail(file, 10)

            assert actual == "\n".join(map(str, list(range(10, 20))))

    def test_tail_by_15(self):
        with open(TEST_FILE, "rb") as file:
            actual = tail(file, 15)

            assert actual == "\n".join(map(str, list(range(5, 20))))

    def test_tail_on_short_file(self):
        test_data = "\n".join(map(str, list(range(5))))

        with open(TEST_FILE, "w") as file:
            file.write(test_data)

        with open(TEST_FILE, "rb") as file:
            actual = tail(file, 10)
            assert actual == str(test_data)

    def test_check_file_existing(self):
        self.assertRaises(FileNotFoundError, check_file, "test1.csv")

    def test_check_file_on_folder(self):
        self.assertRaises(IsNotFile, check_file, "tests")
