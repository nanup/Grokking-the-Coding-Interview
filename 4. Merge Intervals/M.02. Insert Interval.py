def insert(intervals, new_interval):
  intervals.append(new_interval)

  intervals.sort(key = lambda x: x[0])

  return merge_intervals(intervals)

def merge_intervals(intervals):
  if len(intervals) < 2:
    return intervals

  mergedIntervals = []

  start = intervals[0][0]
  end = intervals[0][1]

  for i in range(1, len(intervals)):
    interval = intervals[i]

    if interval[0] <= end:
      end = max(end, interval[1])

    else:
      mergedIntervals.append([start, end])
      start = interval[0]
      end = interval[1]

  mergedIntervals.append([start, end])

  return mergedIntervals


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()