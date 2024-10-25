import unittest

def count_occurence(lst):
    occurences={}

    for x in lst:

        if x in occurences:
            occurences[x] = occurences[x] + 1
        else:
            occurences[x] = 1

    return  occurences


class Testcaseoccurence(unittest.TestCase):
    def testwithinteger(self):
        input = [1,2,2,4,2,]
        expected_output= {1:1,2:3,4:1}
        self.assertEqual(count_occurence(input),expected_output)

    def testwithnotinteger(self):
        input = [1,2,2,4,5]
        expected_output= {1:1,2:3,4:1}
        self.assertEqual(count_occurence(input),expected_output)