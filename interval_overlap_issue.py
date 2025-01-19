intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort()  # Sort intervals based on the start time

    merged = [intervals[0]]  # Initialize the merged list with the first interval

    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:  # Check if the current interval overlaps with the last merged interval
            merged[-1][1] = max(merged[-1][1], interval[1])  # Merge the intervals
        else:
            merged.append(interval)  # If no overlap, add the interval to the merged list

    return merged

print(merge_intervals(intervals))
