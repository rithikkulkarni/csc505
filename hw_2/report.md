# hw_2 implementation report

Tracks changes and design decisions made while implementing the code for hw_2. Updated
as work progresses.

## The actual assignment (as given by the user)

> Implement insertion sort, merge sort, and heapsort and count the input-value
> comparisons made by each algorithm. Use the supplied Sorting.py ... framework and
> follow the textbook algorithms INSERTION-SORT, MERGE/MERGE-SORT, and
> MAX-HEAPIFY/HEAPSORT. Store the final sorted array and comparison count in the
> framework variables. Do not rename existing methods or variables, and do not alter
> the supplied test code. You may add helper methods.
>
> Count comparisons exactly as follows:
> - Insertion sort: count each comparison A[i] > key when i is a valid array index,
>   including a final unsuccessful value comparison when one occurs.
> - Merge sort: count each evaluation of L[i] ≤ R[j] in MERGE, including comparisons
>   involving a sentinel.
> - Heapsort: count each evaluation of A[l] > A[largest] or A[r] > A[largest] when the
>   corresponding child index is within the current heap.
> Do not count comparisons involving only indices, loop bounds, heap size, or other
> control variables.
>
> Must handle empty arrays, one-element arrays, duplicate values, negative values,
> already sorted arrays, and reverse-sorted arrays. Published and hidden tests will run
> on a remote server.

This supersedes everything I assumed earlier in this session (see "Corrections" below).
Bubble sort is **not** part of this problem — it's kept in `Sorting.py` /
`BubbleSortTest.py` only because it was asked for separately.

## Corrections made this turn

1. **Reverted `SortingTest.py` to exactly its originally-supplied content.** Last turn I
   added bubble-sort tests and report-generation code directly into that file, which
   violates "do not alter the supplied test code." Fixed by restoring the file verbatim
   and moving everything else into new, separate files
   (`BubbleSortTest.py`, `generate_comparison_report.py`).
2. **Rewrote `heap_sort`.** It previously built the heap via `n` calls to a
   `MAX-HEAP-INSERT`-style sift-up (based on screenshots of CLRS's priority-queue
   operations `MAX-HEAP-INCREASE-KEY`/`MAX-HEAP-INSERT`/`MAX-HEAP-EXTRACT-MAX`). The
   assignment explicitly asks for `MAX-HEAPIFY`/`HEAPSORT` instead — the classic
   `BUILD-MAX-HEAP` (bottom-up heapify from the last internal node) followed by
   repeated root-extraction. Rewrote `heap_sort` to do exactly that; `_max_heapify`
   (the sift-down helper) was already the standard CLRS `MAX-HEAPIFY` and needed no
   changes. The supplied `test_heap_sort` still passes unchanged — both approaches
   happen to produce identical totals (3 and 7) on those two small inputs — but only
   the `BUILD-MAX-HEAP` version is the algorithm actually specified, so it's the one
   whose comparison counts should generalize correctly to the hidden tests.

## Comparison-counting convention (confirmed against the assignment text)

- **`insertion_sort`**: counts `A[j] > key` (assignment calls the index `i`; the
  supplied `Sorting.py`/CLRS pseudocode calls it `j` — same loop variable) each time
  `j` is a valid index, i.e. inside the `while j >= 0` guard, including the final
  comparison that comes back false and ends the loop.
- **`merge_sort`/`_merge`**: counts `L[i] <= R[j]` once per iteration of the main
  merge loop. Implemented following the no-sentinel `MERGE` from the supplied textbook
  screenshot (explicit `nL`/`nR` bound checks, two trailing copy loops, no `∞` values
  appended to `L`/`R`) rather than the older sentinel-based CLRS edition. This matches
  the supplied test's hardcoded counts exactly (`2` and `4`) — a literal sentinel
  version would produce different (higher) counts, e.g. `5` instead of `2` for
  `[3, 6, 1]`, which would fail the supplied test — so "including comparisons
  involving a sentinel" in the prompt reads as covering *either* textbook edition's
  design, not mandating the sentinel one.
- **`heap_sort`/`_max_heapify`**: counts `A[left] > A[largest]` / `A[right] > A[largest]`
  only when the child index is `< heap_size`; the bound check itself is never counted.

In all three, index/bound comparisons (`j >= 0`, `i < nL`, `left < heap_size`, etc.)
are never counted — only counted once a comparison of two *array values* is actually
evaluated, matching "Do not count comparisons involving only indices, loop bounds,
heap size, or other control variables."

## Files

- `Sorting.py` — `insertion_sort`, `merge_sort`/`_merge`, `heap_sort`/`_max_heapify`
  (the three graded algorithms), plus `bubble_sort`/`bubble_sort_early_termination`
  (not graded here, kept for the separate written analysis in `SOLUTIONS.md`).
- `SortingTest.py` — **untouched**, exactly as supplied.
- `BubbleSortTest.py` — new, bubble-sort-only tests, kept out of `SortingTest.py`.
- `generate_comparison_report.py` — new, standalone script (does not import or modify
  `SortingTest.py`) that runs every algorithm against the supplied test inputs plus the
  assignment's required edge cases (empty, one-element, duplicates, negative values,
  sorted, reverse-sorted) and writes `comparison_count_report.md`.

## Verification

- `python -m unittest SortingTest -v`: all 3 supplied tests pass, unmodified file.
- `python -m unittest BubbleSortTest -v`: all 3 bubble-sort tests pass.
- Edge-case check (empty, one-element, all-duplicates, negatives, sorted,
  reverse-sorted) for `insertion_sort`, `merge_sort`, `heap_sort`: all produce
  `sorted(input)` correctly.
- Randomized check, 300 trials, array sizes 0-20, values in [-15, 14] (duplicates and
  negatives included by construction): all three produce `sorted(input)` correctly.
- `generate_comparison_report.py` output is in `comparison_count_report.md` (42 runs:
  every supplied-test input plus every edge case, for all five implemented algorithms).
