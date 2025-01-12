def merge(intervals):
    #sort based on start of each interval
    intervals.sort(key = lambda i: i[0])

    merged_intervals = [intervals[0]]

    #for each interval in intervals, check previous entry in merged intervals to see if there is overlap
    for start, end in intervals[1:]: 
        
        if merged_intervals[-1][1] >= start:
            merged_intervals[-1][1] = max(end, merged_intervals[-1][1])
        
        else:
            merged_intervals.append([start, end])

    return merged_intervals


intervals = [[1,7],[4,5]]
print(merge(intervals))