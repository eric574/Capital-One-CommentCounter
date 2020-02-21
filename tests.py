# Author: Eric Liu (e48liu@edu.uwaterloo.ca)
# Affiliation: CapitalOne - Technical Assessment

import unittest
from commentcounter import *

# CommentCounter Class tests

class CommentCounterTest(unittest.TestCase):
    def test_1_file_extension(self):
        # Capability to detect valid file extensions
        filename = "gitig.nore.c++"
        test_class = CommentCounter(filename)
        result = test_class.file_extension
        self.assertEqual(result, "c++")

    def test_2_file_extension(self):
        filename = ".gitig.nore.c++"
        test_class = CommentCounter(filename)
        result = test_class.file_extension
        self.assertEqual(result, False)

    def test_3_file_extension(self):
        # Test CommentCounter class's capability to detect valid file extensions
        filename = "LICENSE"
        test_class = CommentCounter(filename)
        result = test_class.file_extension
        self.assertEqual(result, False)

    def test_4_file_extension(self):
        # Test CommentCounter class's capability to detect valid file extensions
        filename = "CommentCounter.py"
        test_class = CommentCounter(filename)
        result = test_class.file_extension
        self.assertEqual(result, "py")

    def test_1_loc_count(self):
        # Test CommentCounter class's capability to detect valid file extensions
        filename = "extensions.py"
        test_class = CommentCounter(filename)
        test_class.analyze_code()
        result = test_class.counter_dict["loc"]
        self.assertEqual(result, 117)

    def test_1_output(self):
        # Test CommentCounter class's capability to analyze comments
        filename = "tests/test1.java"
        test_class = CommentCounter(filename)
        test_class.analyze_code()
        test_output = test_class.analysis_output('JSON')
        actual_output = {'loc': 60, 'tot_comments': 28, 'single_comments': 6,
                        'block_comment_lines': 22, 'block_comments': 2, 'todos': 1}
        self.assertEqual(test_output, actual_output)

    def test_2_output(self):
        # Test CommentCounter class's capability to analyze comments
        filename = "tests/test2.js"
        test_class = CommentCounter(filename)
        test_class.analyze_code()
        test_output = test_class.analysis_output('JSON')
        actual_output = {'loc': 40, 'tot_comments': 23, 'single_comments': 5,
                        'block_comment_lines': 18, 'block_comments': 4, 'todos': 1}
        self.assertEqual(test_output, actual_output)

    def test_3_output(self):
        # Test CommentCounter class's capability to analyze comments
        filename = "tests/test3.py"
        test_class = CommentCounter(filename)
        test_class.analyze_code()
        test_output = test_class.analysis_output('JSON')
        actual_output = {'loc': 61, 'tot_comments': 19, 'single_comments': 10,
                        'block_comment_lines': 9, 'block_comments': 3, 'todos': 3}
        self.assertEqual(test_output, actual_output)


    def test_4_output(self):
        # Test CommentCounter class's capability to analyze comments
        filename = "tests/test4.py"
        test_class = CommentCounter(filename)
        test_class.analyze_code()
        test_output = test_class.analysis_output('JSON')
        actual_output = {'loc': 25, 'tot_comments': 13, 'single_comments': 8,
                        'block_comment_lines': 5, 'block_comments': 2, 'todos': 5}
        self.assertEqual(test_output, actual_output)

    def test_5_output(self):
        # Test CommentCounter class's capability to analyze comments
        filename = "tests/test5.cpp"
        test_class = CommentCounter(filename)
        test_class.analyze_code()
        test_output = test_class.analysis_output('JSON')
        actual_output = {'loc': 61, 'tot_comments': 13, 'single_comments': 4,
                        'block_comment_lines': 9, 'block_comments': 1, 'todos': 1}
        self.assertEqual(test_output, actual_output)

if __name__ == '__main__':
    unittest.main()