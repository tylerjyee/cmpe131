def cacti_number(plot):
    count = 0
    x_bounds = (0, len(plot[0])-1)
    y_bounds = (0, len(plot)-1)

    for x in range(len(plot[0])):
        for y in range(len(plot)):
            if plot[y][x] == 0:
                step = 1
                if not (x_bounds[0] > x+1 or x_bounds[1] < x+1):
                    if plot[y][x+1] == 1:
                        step = 0
                if not (x_bounds[0] > x-1 or x_bounds[1] < x-1):
                    if plot[y][x-1] == 1:
                        step = 0
                if not (y_bounds[0] > y+1 or y_bounds[1] < y+1):
                    if plot[y+1][x] == 1:
                        step = 0
                if not (y_bounds[0] > y-1 or y_bounds[1] < y-1):
                    if plot[y-1][x] == 1:
                        step = 0
                if step:
                    count += 1
                    plot[y][x] = 1
    return count