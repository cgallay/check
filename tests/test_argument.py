import unittest

import check


@check.arg(name='proba', vtype=check.Integer())
def basic_function(proba):
    return None

@check.arg(name="test", vtype=check.Integer())
def extra_arg(test=7):
    return None


class TestBasic(unittest.TestCase):
    def test_integer(self):        
        self.assertRaises(ValueError, basic_function, 5.6)
        self.assertRaises(ValueError, basic_function, "djsk")

    def test_default_arg(self):
        # test that arguement defaults are consider, and not overwriting user defined value.
        extra_arg()
        self.assertRaises(ValueError, extra_arg, 5.8)

    


if __name__ == '__main__':
    unittest.main()