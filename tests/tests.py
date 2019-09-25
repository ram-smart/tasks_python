import unittest
import hexlet.pairs as pairs


checked_parameters = ((1, 2),
                      (1.0, 5),
                      (5, 2.0),
                      (2.0, 3.0),
                      (1, ''),
                      ('', 2),
                      (1, 'foo'),
                      ('foo', 2),
                      ('', ''),
                      ('foo', 'foo'),
                      (1, True),
                      ('', False),
                      (True, False))


class Is_finction(unittest.TestCase):

    def cons_is_function(self):
        for a, b in checked_parameters:
            result = pairs.cons(a, b)
            self.assertEqual(True, callable(result))


# class Get_elements_pairs(unittest.TestCase):
#
#     def get_elements_pair(self):
#         for a, b in checked_parameters:
#             pair = pairs.cons(a, b)
#             get_a = pairs.car(pair)
#             get_b = pairs.cdr(pair)
#             self.assertEqual(a, get_a)
#             self.assertEqual(a, get_b)
#
# def main():
#     element_pair = Get_elements_pairs()


if __name__ == '__main__':
    unittest.main()
