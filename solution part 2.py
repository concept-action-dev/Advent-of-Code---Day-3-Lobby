# solution.py
# Reads lines from input.txt, selects the lexicographically largest subsequence of length k (12),
# converts it to an integer, and sums across all lines.

K = 12  # number of batteries to choose per bank (part two)

def max_k_subsequence(s: str, k: int) -> str:
    """
    Return the lexicographically largest subsequence of length k from string s (digits),
    preserving the original order.
    """
    n = len(s)
    if k >= n:
        # If length is <= k, return the whole string (or pad if you prefer).
        return s[:k]
    stack = []
    for i, ch in enumerate(s):
        # number of characters remaining including current
        remaining = n - i
        # while we can pop (have something smaller on stack), and even after popping we can still
        # fill to k using remaining chars, pop to allow ch to be earlier.
        while stack and len(stack) + remaining > k and stack[-1] < ch:
            stack.pop()
        # push if we still need more digits
        if len(stack) < k:
            stack.append(ch)
    # stack may be longer than k in some implementations; slice to k
    return ''.join(stack[:k])

def total_output_from_file(filename: str, k: int) -> int:
    total = 0
    with open(filename, 'r') as f:
        for line in f:
            bank = line.strip()
            if not bank:
                continue
            if len(bank) < k:
                raise ValueError(f"Bank has fewer than {k} batteries: '{bank}'")
            best = max_k_subsequence(bank, k)
            total += int(best)
    return total

if __name__ == "__main__":
    answer = total_output_from_file("input.txt", K)
    print("Total output joltage:", answer)

