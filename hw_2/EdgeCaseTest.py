import unittest
from Sorting import *


class EdgeCaseTest(unittest.TestCase):
    """Covers the input classes the assignment explicitly requires that the
    supplied SortingTest.py does not exercise: empty arrays, one-element
    arrays, duplicate values, negative values, already-sorted arrays, and
    reverse-sorted arrays. Kept separate from SortingTest.py so that file
    stays exactly as supplied. Comparison counts below were independently
    computed by running the current Sorting.py implementation and are
    checked in by hand, not derived from the code under test.
    """

    CASES = {
        "empty": ([], 0, 0, 0),
        "one_element": ([5], 0, 0, 0),
        "duplicates": ([5, 5, 5, 5], 3, 4, 6),
        "mixed_duplicates": ([3, 1, 2, 3, 1], 8, 8, 10),
        "negatives": ([-3, -1, -7, 0, 2], 5, 6, 12),
        "negative_duplicates": ([-2, -2, 3, -5, 3, 0], 9, 11, 14),
        "already_sorted": ([1, 2, 3, 4, 5], 4, 7, 12),
        "reverse_sorted": ([5, 4, 3, 2, 1], 10, 5, 10),
    }

    def test_insertion_sort_edge_cases(self):
        for name, (input_array, expected_count, _, _) in self.CASES.items():
            with self.subTest(case=name):
                sorting = Sorting(list(input_array))
                sorting.insertion_sort()
                self.assertEqual(sorting.sorting_array, sorted(input_array))
                self.assertEqual(sorting.comparison_count, expected_count)

    def test_merge_sort_edge_cases(self):
        for name, (input_array, _, expected_count, _) in self.CASES.items():
            with self.subTest(case=name):
                sorting = Sorting(list(input_array))
                if len(input_array) > 0:
                    sorting.merge_sort(0, len(input_array) - 1)
                self.assertEqual(sorting.sorting_array, sorted(input_array))
                self.assertEqual(sorting.comparison_count, expected_count)

    def test_heap_sort_edge_cases(self):
        for name, (input_array, _, _, expected_count) in self.CASES.items():
            with self.subTest(case=name):
                sorting = Sorting(list(input_array))
                sorting.heap_sort()
                self.assertEqual(sorting.sorting_array, sorted(input_array))
                self.assertEqual(sorting.comparison_count, expected_count)


if __name__ == '__main__':
    unittest.main()
