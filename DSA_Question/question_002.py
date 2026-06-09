def calculate_pairs(n, arr):
    """
    Write your logic here.
    Parameters:
        n (int): The size of the array
        arr (list): List of integers representing the elements of the array
    Returns:
        int: The required number of pairs based on the problem statement
    """

    from collections import defaultdict
    import bisect

    # Store all subarrays having the same sum
    sums = defaultdict(list)

    # Generate all subarrays
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]

            # Store as (start, end)
            sums[curr_sum].append((i, j))

    answer = 0

    # Process each sum separately
    for intervals in sums.values():

        # Sort by ending index
        intervals.sort(key=lambda x: x[1])

        ends = []

        for start, end in intervals:

            # Count intervals ending before this one starts
            count = bisect.bisect_left(ends, start)

            answer += count

            bisect.insort(ends, end)

    return answer


def main():
    import sys
    input = sys.stdin.read

    data = input().strip().split()

    n = int(data[0])  # The first line of input, integer N
    arr = list(map(int, data[1:n+1]))  # The second line of input

    result = calculate_pairs(n, arr)

    print(result)


if __name__ == "__main__":
    main()