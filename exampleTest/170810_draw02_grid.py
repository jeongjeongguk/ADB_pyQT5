import sys


def draw_grid(cols, rows, cell_size=4):
    for y in range(rows):
        # draw horizontal line
        sys.stdout.write(('+' + ' - ' * cell_size) * cols + '+\n')
        # draw vertical lines
        sys.stdout.write((('|' + '   ' * cell_size) * cols + '|\n') * cell_size)
    # draw last horizontal line
    sys.stdout.write(('+' + ' - ' * cell_size) * cols + '+\n')


def main():
    if len(sys.argv) < 2:
        print('usage: draw_grid.py <columns> <rows> [cellsize]')
        return
    elif len(sys.argv) == 3:
        cols = int(sys.argv[1])
        rows = int(sys.argv[2])
        if cols < 1 or rows < 1:
            print('<columns> and <rows> number must be > 0!')
            return
        draw_grid(cols, rows)
    elif len(sys.argv) == 4:
        cols = int(sys.argv[1])
        rows = int(sys.argv[2])
        cell_size = int(sys.argv[3])
        if cols < 1 or rows < 1 or cell_size < 1:
            print('<columns>, <rows> and [cellsize] must be > 0!')
            return
        draw_grid(cols, rows, cell_size)

if __name__ == '__main__':
    main()