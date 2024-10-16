








def count_non_intersecting_segments(segments):


    segments.sort()

    count = 0
    prev_end = 0

    for start, end in segments:
        if start >= prev_end:
            count += 1
            prev_end = end

    return count

# Example usage
segments = [(1, 4), (2, 5), (3, 1), (4, 5), (5, 6)]
result = count_non_intersecting_segments(segments)
print(result)  # Output: 3

