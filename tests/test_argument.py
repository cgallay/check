import unittest

import check


@check.arg(name='proba', vtype=check.Integer())
def basic_function(proba):
    return None


class TestBasic(unittest.TestCase):
    def test_range(self):        
        self.assertRaises(ValueError, basic_function, 5.6)

    


if __name__ == '__main__':
    unittest.main()