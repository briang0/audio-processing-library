import os
import unittest

from src.python.main.io import writer, reader
from src.python.main.util import random_util


class TestFormat(unittest.TestCase):

    def test_write_csv_1(self):
        resource_directory = "../../../../resources"
        path = resource_directory + "/test_write_csv_1.csv"
        rows = 32
        cols = 64
        expected = []
        for i in range(0, rows):
            expected.append(random_util.get_random_complex_vec(cols, -100000, 100000))
        writer.write_cmplx_matrix_to_csv(expected, path)
        actual = reader.read_cmplx_matrix_from_csv(path)
        assert os.path.isfile(path) == True, "File was not created"
        assert len(expected) == len(actual) == rows, "Row length mismatch"
        for i in range(0, rows):
            for j in range(0, cols):
                exp = expected[i][j]
                act = actual[i][j]
                assert exp == act, "Actual data does not match expected"
            assert len(expected[i]) == len(actual[i]), "Column length mismatch"
        os.remove(path)
        assert os.path.isfile(path) is False, "File was not deleted"


if __name__ == "__main__":
    print("test_reader")
    unittest.main()
