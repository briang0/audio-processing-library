import os, sys
sys.path.insert(0, os.path.abspath("../../.."))
import python.main.math.complex_num as cmplx
import python.main.util.format as fmt
import python.main.util.random_util as ru
import python.main.io.writer as writer
import python.main.io.reader as reader
import unittest

class test_format(unittest.TestCase):

    def test_write_csv_1(self):
        zero = cmplx.complex_num(0.0,0.0)
        dir = "../../../../resources"
        path = dir + ("/test_write_csv_1.csv")
        rows = 32
        cols = 64
        expected = []
        for i in range (0, rows):
            expected.append(ru.get_random_complex_vec(cols, -100000, 100000))
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
        assert os.path.isfile(path) == False, "File was not deleted"



if __name__ == "__main__":
    unittest.main()
