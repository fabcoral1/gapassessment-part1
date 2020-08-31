import unittest
import gapassessmentpart1


class test_gapassessmentpart1(unittest.TestCase):

    # Test will assert correct results when the largest word is in the first position.
    def test_largestleading(self):
        testcontent = ['abcde', 'a', 'abc', 'ab', 'abcd']
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[0],"abcde")
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[1],"edcba")

    # Test will assert correct results when the largest word is in the first position.
    def test_largesttrailing(self):
        testcontent = ['a', 'abcd', 'abc', 'ab', 'abcde']
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[0],"abcde")
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[1],"edcba")

    # Test will assert correct results when the largest word is not in the first or the last position.
    def test_largestnotleadingnottrailing(self):
        testcontent = ['abc', 'ab', 'abcd', 'abcde', 'a']
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[0],"abcde")
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[1],"edcba")

    # Test will assert correct results when the file contains a blank row (row with no word).
    def test_blankrow(self):
        testcontent = ['abc', 'ab', '', 'abcd', 'abcde', 'a']
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[0],"abcde")
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[1],"edcba")

    # Test will assert correct results when the largest word contains spaces that are not trailing (valid spaces).
    def test_largestcountingvalidspaces(self):
        testcontent = ['abc', 'abc de', 'ab', 'abcd', 'abcde', 'a']
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[0],"abc de")
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[1],"ed cba")

    # Test will assert validation messages when file is empty.
    def test_emptyfile(self):
        testcontent = []
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[0],"Largest word was not obtained since file is empty.")
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[1],"Largest word reversed was not obtained since file is empty.")

    # Test will assert validation messages when file is empty and only contains spaces.
    def test_emptyfilewithonlyspaces(self):
        testcontent = ['  ']
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[0],"Largest word was not obtained since file is empty.")
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[1],"Largest word reversed was not obtained since file is empty.")

    # Test will assert correct results when the words contain lower, upper and special characters.
    def test_(self):
        testcontent = ['$A&b?C@d;E}', '$A&', '$A&b?C@', '$A&b?', '$A&b?C@d;']
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[0], "$A&b?C@d;E}")
        self.assertEqual(gapassessmentpart1.largestwordandreverse(testcontent)[1], "}E;d@C?b&A$")


if __name__ == '__main__':
    unittest.main()
