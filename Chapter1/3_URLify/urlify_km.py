import unittest

class Test(unittest.TestCase):
    #eamples in the form of [in_str, length, expected_output]
    data = [ ('Mr John Smith    ', 13, 'Mr%20John%20Smith'),
             ('rizzuto?', 8, 'rizzuto?'),
             ('to infinity and beyond      ', 22, 'to%20infinity%20and%20beyond')]
   

    def test_urlify(self):
        # check
        for (instr,length,expected) in self.data:
            actual = urlify(instr,length)
            self.assertEqual(actual, expected)
       


def urlify(in_str,length):
    
    charArr = list(in_str) #expected length of string
    j = len(charArr) - 1 # starts at last element in input string
    
    #walk backwards through the expected string, assuming no leading spaces
    for i in range(length-1,-1,-1):
        if charArr[i] != ' ':
            charArr[j] = charArr[i]
            j -= 1 # step backwards from end of string with space
        else:
            #we hit a space, so need to pop in the '%20'
            #charArr[j-2], charArr[j-1], charArr[j] = '%', '2','0' # less pythonic
            charArr[j-2:j+1] = '%20' # more pythonic
            j -= 3
    return ''.join(charArr)

if __name__ == "__main__":
    unittest.main()

