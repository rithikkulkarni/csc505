# HW1 — Problem 1: Bubble sort and loop invariants

Working notes / draft for the typeset submission. Uses the textbook (CLRS) pseudocode
for `BUBBLESORT`, 1-indexed:

```
BUBBLESORT(A)
1  for i = 1 to A.length - 1
2      for j = A.length downto i + 1
3          if A[j] < A[j-1]
4              exchange A[j] with A[j-1]
```

`n = A.length` throughout.

## (a) What else must be proved?

Proving the output `A'` satisfies `A'[1] ≤ A'[2] ≤ ... ≤ A'[n]` (inequality 2.3) is not
enough to prove `BUBBLESORT` *sorts*: a procedure that just overwrote every entry with
the same constant would also satisfy that inequality. To show `BUBBLESORT` actually sorts
`A`, we additionally need to prove:

- **Termination** — the two `for` loops each run a bounded, decreasing number of
  iterations, so the algorithm terminates. (Immediate from the loop bounds.)
- **`A'` is a permutation of `A`** — the output contains exactly the same multiset of
  elements as the input, just reordered. This is the fact that rules out the
  constant-array counterexample above, and it's what the loop-invariant proofs below
  establish alongside sortedness.

## (b) Inner loop (lines 2–4) invariant

**What the loop does:** for a fixed `i`, this loop scans the subarray `A[i..n]` from
right to left, swapping each adjacent out-of-order pair, which has the effect of
carrying the smallest element of `A[i..n]` down to position `i`.

**Loop invariant.** At the start of each iteration of the `for j` loop:
1. `A[j..n]` is a permutation of the values that occupied `A[j..n]` when this inner
   loop began (i.e., at the start of the current outer iteration `i`), and
2. `A[j] = min(A[j..n])` (the minimum over the *current* contents of that subarray).

- **Initialization.** Before the first iteration, `j = n`, so `A[j..n] = A[n..n]` is a
  single element — trivially a permutation of itself, and trivially its own minimum.

- **Maintenance.** Assume the invariant holds at the start of an iteration for some `j`.
  Because no earlier iteration of this inner loop touches any index `< j`, `A[j-1]`
  still holds its original value from the start of this outer iteration.
  - *No swap* (`A[j] ≥ A[j-1]`): `A[j-1]` is unchanged and, since
    `A[j-1] ≤ A[j] = min(A[j..n])`, `A[j-1]` is `≤` every element of `A[j..n]`, so
    `A[j-1] = min(A[(j-1)..n])`. The multiset `A[(j-1)..n] = {A[j-1]} ∪ A[j..n]` is
    unchanged, hence still a permutation of the original `A[(j-1)..n]`.
  - *Swap* (`A[j] < A[j-1]`): after exchanging, the new `A[j-1]` is the old `A[j]`
    (`= min(A[j..n])`) and the new `A[j]` is the old `A[j-1]`. The new `A[j-1]` is `≤`
    the new `A[j]` and `≤` every element of `A[j+1..n]` (a subset of the old
    `A[j..n]`), so it equals `min(A[(j-1)..n])`. The exchange doesn't change which
    elements occupy `A[(j-1)..n]`, only their order, so the permutation property is
    preserved.
  - Either way, the invariant holds at `j-1`, the next iteration's value.

- **Termination.** The loop ends when `j` has been decremented past `i+1`, i.e., the
  invariant's last confirmed state is effectively "at `j = i`": `A[i..n]` is a
  permutation of the subarray as it stood at the start of this outer iteration, and
  `A[i] = min(A[i..n])`. This is exactly the fact part (c) needs.

## (c) Outer loop (lines 1–4) invariant

**What the loop does:** it repeatedly extracts the smallest remaining element and
places it at the front of the unsorted suffix, growing a sorted, correctly-positioned
prefix `A[1..i-1]` one element at a time until the whole array is sorted.

**Loop invariant.** At the start of each iteration of the `for i` loop:
1. `A[1..i-1]` is sorted in nondecreasing order,
2. every element of `A[1..i-1]` is `≤` every element of `A[i..n]`, and
3. `A[i..n]` is a permutation of the original input's `A[i..n]`.

- **Initialization.** `i = 1`: `A[1..0]` is empty, so (1) and (2) hold vacuously, and
  (3) holds because `A[1..n]` is still exactly the (untouched) original array.

- **Maintenance.** Assume the invariant holds at the start of outer iteration `i`. By
  part (b), after the inner loop runs, `A[i..n]` is a permutation of its value at the
  start of this outer iteration (so, by the outer IH, a permutation of the *original*
  `A[i..n]`), and the new `A[i] = min(A[i..n])`. Combined with the outer IH
  (`A[1..i-1] ≤` every element of the old `A[i..n]`, which has the same elements as the
  new `A[i..n]`), we get: `A[1..i-1]` followed by the new `A[i]` is sorted, and the new
  `A[i]` is `≤` every element of `A[i+1..n]` (since it's the min of `A[i..n]`). So at
  the start of iteration `i+1`, `A[1..i]` is sorted and `≤` everything in `A[i+1..n]`,
  and `A[i+1..n]` is a permutation of the original `A[i+1..n]` — the invariant holds
  for `i+1`.

- **Termination.** The loop ends after `i = n-1` is processed, i.e., with the invariant
  holding "at `i = n`": `A[1..n-1]` is sorted and `≤` `A[n]`, so `A[1..n]` is sorted —
  establishing inequality (2.3) — and (from part (a)'s requirement) the whole array has
  only ever been permuted, never had values invented or dropped, at every step of both
  loops. Together this proves `BUBBLESORT` correctly sorts `A`.

## (d) Running time (using `<` as the only basic operation)

The single comparison `A[j] < A[j-1]` on line 3 executes exactly once per inner-loop
iteration, **regardless of whether a swap happens**. Total comparisons:

```
sum_{i=1}^{n-1} sum_{j=i+1}^{n} 1  =  sum_{i=1}^{n-1} (n-i)  =  n(n-1)/2
```

This count does not depend on the input values at all — it's a function of `n` only.
So for the textbook `BUBBLESORT`:

- **Worst case:** `n(n-1)/2` comparisons → **Θ(n²)**.
- **Best case:** also exactly `n(n-1)/2` comparisons → **Θ(n²)** — there is no
  best-case speedup, because the loop bounds never depend on the data.

Compare to insertion sort: worst case (reverse-sorted input) is also `n(n-1)/2`
comparisons (Θ(n²)), but best case (already-sorted input) is only `n-1` comparisons
(Θ(n)), because each inner `while` exits after a single failed comparison.

**Preference: insertion sort.** Its worst case matches bubble sort's, but it is
*adaptive* — nearly-sorted input runs close to Θ(n) — while the textbook bubble sort
above always pays the full Θ(n²) no matter how sorted the input already is. Part (e)'s
early-termination variant closes part of this gap, but even then bubble sort still does
more element movement per pass and has worse practical constants, so insertion sort
remains the better default choice.

## (e) Early-termination variant

Modify the outer loop: after a complete inner-loop pass for a given `i`, if that pass
performed **zero** swaps, terminate the algorithm immediately.

**Correctness.** A pass for index `i` compares each adjacent pair `(A[j-1], A[j])` for
`j = i+1, ..., n`. If none of these comparisons trigger a swap, then
`A[j] ≥ A[j-1]` held for every such pair, which means `A[i] ≤ A[i+1] ≤ ... ≤ A[n]` —
the subarray `A[i..n]` is already sorted. By the outer-loop invariant from part (c),
`A[1..i-1]` is already sorted and every one of its elements is `≤` every element of
`A[i..n]`. A sorted prefix followed by a sorted suffix whose smallest element is `≥`
the prefix's largest element means the *entire* array `A[1..n]` is already sorted.
Continuing to run further passes would find no more out-of-order pairs and change
nothing, so stopping here is correct — it still satisfies inequality (2.3), and the
array has only ever been permuted, never corrupted.

**Comparison counts.**
- **Best case (already sorted):** the very first pass (`i=1`) finds zero swaps, so the
  algorithm terminates after exactly one pass: `n-1` comparisons → **Θ(n)**.
- **Worst case (e.g., reverse-sorted):** every pass except the very last one contains
  at least one swap, so early termination never triggers before the array is fully
  sorted; the count matches the unmodified algorithm: `n(n-1)/2` comparisons →
  **Θ(n²)**.

(Empirically verified in [hw_2/Sorting.py](Sorting.py): for `n=10`, the early-termination
variant takes `9 = n-1` comparisons on sorted input but `45 = n(n-1)/2` on reverse-sorted
input, while the standard variant always takes `45` — see
[report.md](report.md) for the verification run.)
