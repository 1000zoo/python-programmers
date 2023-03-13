def solution(wallpaper):
    answer = []

    x1 = y1 = 50
    x2 = y2 = -1

    for i, line in enumerate(wallpaper):
        for j, file in enumerate(wallpaper):
            if file == '#':
                x1 = min(x1, i)
                y1 = min(y1, j)
                x2 = max(x2, i)
                y2 = max(y2, j)

    return [x1, y1, x2, y2]


k = [".#...", "..#..", "...#."]
solution(k)
