import unittest
from Sorting import *


class BubbleSortTest(unittest.TestCase):
    """Bubble sort isn't part of the graded Problem 1(a)/(b)/(c) (insertion sort,
    merge sort, heapsort) -- kept separate from SortingTest.py so that file stays
    exactly as supplied. See SOLUTIONS.md for the written bubble-sort analysis."""

    def test_bubble_sort(self):
        input_array = [3, 6, 1]
        sorting = Sorting(input_array)
        sorting.bubble_sort()
        self.assertEqual(sorting.sorting_array, [1, 3, 6])
        self.assertEqual(sorting.comparison_count, 3)

        input_array = [1, 2, 3, 4]
        sorting = Sorting(input_array)
        sorting.bubble_sort()
        self.assertEqual(sorting.sorting_array, [1, 2, 3, 4])
        self.assertEqual(sorting.comparison_count, 6)

        input_array = [4, 3, 2, 1]
        sorting = Sorting(input_array)
        sorting.bubble_sort()
        self.assertEqual(sorting.sorting_array, [1, 2, 3, 4])
        self.assertEqual(sorting.comparison_count, 6)

    def test_bubble_sort_early_termination(self):
        input_array = [3, 6, 1]
        sorting = Sorting(input_array)
        sorting.bubble_sort_early_termination()
        self.assertEqual(sorting.sorting_array, [1, 3, 6])
        self.assertEqual(sorting.comparison_count, 3)

        input_array = [1, 2, 3, 4]
        sorting = Sorting(input_array)
        sorting.bubble_sort_early_termination()
        self.assertEqual(sorting.sorting_array, [1, 2, 3, 4])
        self.assertEqual(sorting.comparison_count, 3)

    def test_bubble_sort_early_termination_matches_theta_n_best_case(self):
        # Already-sorted input: standard bubblesort always runs n(n-1)/2 comparisons,
        # while the early-termination variant stops after one pass -> n-1 comparisons.
        n = 10
        standard = Sorting(list(range(1, n + 1)))
        standard.bubble_sort()
        self.assertEqual(standard.comparison_count, n * (n - 1) // 2)

        early = Sorting(list(range(1, n + 1)))
        early.bubble_sort_early_termination()
        self.assertEqual(early.comparison_count, n - 1)


if __name__ == '__main__':
    unittest.main()
