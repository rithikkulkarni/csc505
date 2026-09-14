class Sorting:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0

    def merge_sort(self, p, r):
        """CLRS MERGE-SORT(A, p, r), translated to 0-indexed, inclusive [p, r] bounds."""
        if p >= r:
            return
        q = (p + r) // 2
        self.merge_sort(p, q)
        self.merge_sort(q + 1, r)
        self._merge(p, q, r)

    def _merge(self, p, q, r):
        """CLRS MERGE(A, p, q, r). Counts the 'L[i] <= R[j]' test on line 13,
        once per iteration of the main while loop (lines 12-18); the trailing
        copy loops (20-27) do no comparisons.
        """
        a = self.sorting_array
        left = a[p:q + 1]
        right = a[q + 1:r + 1]
        i = j = 0
        k = p
        while i < len(left) and j < len(right):
            self.comparison_count += 1
            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1

    def heap_sort(self):
        """CLRS BUILD-MAX-HEAP + HEAPSORT, operating in place on
        self.sorting_array with 0-indexed PARENT(i)=(i-1)//2, LEFT(i)=2i+1,
        RIGHT(i)=2i+2.
        """
        a = self.sorting_array
        n = len(a)

        # Phase 1: BUILD-MAX-HEAP(A, n) -- heapify down from the last internal
        # node (index n//2 - 1) up to the root.
        for i in range(n // 2 - 1, -1, -1):
            self._max_heapify(i, n)

        # Phase 2: HEAPSORT(A, n) -- repeatedly swap the max into the slot
        # freed up at the end of the heap region, shrink the heap, and sift
        # the new root down.
        heap_size = n
        for end in range(n - 1, 0, -1):
            a[0], a[end] = a[end], a[0]
            heap_size -= 1
            self._max_heapify(0, heap_size)

    def _max_heapify(self, i, heap_size):
        """Standard CLRS MAX-HEAPIFY sift-down (0-indexed). Counts the
        'A[l] > A[largest]' / 'A[r] > A[largest]' key comparisons, each only
        when the child index is within heap_size (the bound check itself
        isn't a comparison operation and isn't counted).
        """
        a = self.sorting_array
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < heap_size:
                self.comparison_count += 1
                if a[left] > a[largest]:
                    largest = left
            if right < heap_size:
                self.comparison_count += 1
                if a[right] > a[largest]:
                    largest = right
            if largest == i:
                break
            a[i], a[largest] = a[largest], a[i]
            i = largest

    def insertion_sort(self):
        """CLRS INSERTION-SORT(A, n), translated to 0-indexed (for i = 1 to n-1).
        Line 5's 'j > 0 and A[j] > key' short-circuits on the bound check, so
        the key comparison is only counted when j >= 0 (0-indexed).
        """
        a = self.sorting_array
        n = len(a)
        for i in range(1, n):
            key = a[i]
            j = i - 1
            while True:
                if j < 0:
                    break
                self.comparison_count += 1
                if not (a[j] > key):
                    break
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key

    def bubble_sort(self):
        """CLRS Problem 2-2 BUBBLESORT, translated to 0-indexed A.
        for i = 1 to n-1: for j = n downto i+1: if A[j] < A[j-1]: swap
        comparison_count counts every '<' test (line 3), matching HW part (d).
        """
        a = self.sorting_array
        n = len(a)
        for i in range(0, n - 1):
            for j in range(n - 1, i, -1):
                self.comparison_count += 1
                if a[j] < a[j - 1]:
                    a[j], a[j - 1] = a[j - 1], a[j]

    def bubble_sort_early_termination(self):
        """HW part (e) variant: stop as soon as a full inner-loop pass makes no swaps,
        since that means the unsorted prefix is already sorted.
        """
        a = self.sorting_array
        n = len(a)
        for i in range(0, n - 1):
            swapped = False
            for j in range(n - 1, i, -1):
                self.comparison_count += 1
                if a[j] < a[j - 1]:
                    a[j], a[j - 1] = a[j - 1], a[j]
                    swapped = True
            if not swapped:
                break
