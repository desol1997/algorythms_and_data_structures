# Given n segments.
# You need to find a set of points of minimum size for which each of the segments contains at least one of the points.

# The first line contains the number 1 <= n <= 100 segments.
# Each of the following n lines contains two numbers 0 <= l <= r <= 10^9 defining the beginning and end of the segment.
# Output the optimal number of m points and the m points themselves.
# If there are several such sets of points, print any of them.


def cover_segments(segments_list):
    segments_sorted = sorted(segments_list, key=lambda x: x[1])

    points_list = []
    for i, s in enumerate(segments_sorted):
        if i == 0:
            points_list.append(s[1])
        elif points_list[-1] < s[0]:
            points_list.append(s[1])

    return points_list


def main():
    n = int(input())

    segments = []
    for _ in range(n):
        segment = map(int, input().split())
        segments.append(tuple(segment))

    points = cover_segments(segments)
    print(len(points))
    print(' '.join([str(point) for point in points]))


if __name__ == '__main__':
    main()
