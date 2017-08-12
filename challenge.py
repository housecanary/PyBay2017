from inspect import isgeneratorfunction
import unittest


class Class(object):
    """
    Implement this class to make the test pass
    Hint: keep running the test!
    """


class Test(unittest.TestCase):
    def test(self):
        string = 'HouseCanary'
        outer_loops = 2
        inner_loops = 3

        instance = Class(s=string)
        i = 0
        for generator in instance(i=outer_loops):
            self.assertTrue(isgeneratorfunction(generator))
            i += 1

            j = 0
            for yielded_value in generator(j=inner_loops):
                j += 1
                self.assertEqual(yielded_value, string)
            self.assertEqual(j, inner_loops)

        self.assertEqual(i, outer_loops)


if __name__ == '__main__':
    unittest.main()
