from unittest import TestCase

ROOT = '/home/przemek/Dokumenty/Projects/applications/python/zad2/zad2-moskalap/sample_codes/'

example_codes = {
    'binarysearch': 'O(log N)',
    'bublesort': 'O(N^2)',
    'heapsort': 'O(N log N)',
    'insertionsort': 'O(N^2)',
    'list_insertion': 'O(1)',
    'quicksort': 'O(N log N)',
    'sorted': 'O(N log N)',
    'index_of': 'O(N)'}


class TestCount_it(TestCase):
    def test_count_it(self):
        for k in example_codes.keys():
            import cmptcomplexity.aprox as cmpt
            res = cmpt.count_it(pattern_invoke=ROOT + 'x_' + k + '.py', init_code=ROOT + 'i_' + k + '.py',
                                log_verbose=False, timeout=30)
            self.assertEqual(res.complexity, example_codes[k])
