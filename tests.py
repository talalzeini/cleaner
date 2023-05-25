import unittest
from main import get_file_info

class CustomTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.writeln("\nPassed")
    def addFailure(self, test, err):
        self.stream.writeln("Failed: {}".format(err[1]))

class CustomTestRunner(unittest.TextTestRunner):
    resultclass = CustomTestResult

class TestGetFileInfo(unittest.TestCase):

    def test_get_file_info(self):
        file_path = "/Users/talalzeini/.Library/Access/Junk/Tests/Files/file-0.txt"
        expected_result = ["file-0.txt", ".txt", "/Users/talalzeini/.Library/Access/Junk/Tests/Files"]
        self.assertEqual(get_file_info(file_path), expected_result)

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)