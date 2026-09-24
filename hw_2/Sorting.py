class Sorting:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0

    def merge_sort(self, p, r):
        if p >= r:
            return
        q = (p + r) // 2
        self.merge_sort(p, q)
        self.merge_sort(q + 1, r)
        self._merge(p, q, r)

    def _merge(self, p, q, r):
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
        a = self.sorting_array
        n = len(a)

        # Phase 1: BUILD-MAX-HEAP(A, n): heapify down from the last internal node (index n//2 - 1) up to the root.
        for i in range(n // 2 - 1, -1, -1):
            self._max_heapify(i, n)

        # Phase 2: HEAPSORT(A, n): repeatedly swap the max into the slot freed up at the end 
        # of the heap region, shrink the heap, and sift the new root down.
        heap_size = n
        for end in range(n - 1, 0, -1):
            a[0], a[end] = a[end], a[0]
            heap_size -= 1
            self._max_heapify(0, heap_size)

    def _max_heapify(self, i, heap_size):
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
