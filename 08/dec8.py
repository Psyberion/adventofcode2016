#!/usr/bin/env python3
import sys

w=50
h=6

display = [ ['.' for i in range(w)] for i in range(h)]

def read_data(fileName : str) -> list:
    lines = []
    try:
        with open(fileName) as f:
            for l in f.read().splitlines():
                lines.append(l)
    except IOError:
        print("Something went wrong, check filename")
        sys.exit(1)
    return lines

def process_data(data):
    for line in data:
        info = line.split(" ")
        if "rect" == info[0]:
            [h,w] = info[1].split("x")
            rect(int(h),int(w))
        elif "rotate" == info[0]:
            try:
                i = int(info[2].split("=")[1])
                n = int(info[4])
                if info[1] == "row":
                    h_rotate(i,n)
                else:
                    v_rotate(i,n)
            except IndexError:
                print(line)
                sys.exit(1)

def rotate(data : list, n : int) -> list:
    return data[-n:] + data[:-n]

def h_rotate(row : int, n : int) -> None:
    display[row] = rotate(display[row],n)

def v_rotate(col : int, n : int) -> None:
    column = []
    for row in display:
        column.append(row[col])
    column = rotate(column,n)
    for i in range(len(display)):
        display[i][col] = column[i]

def rect(w : int, h : int) -> None:
    for i in range(h):
        for j in range(w):
            display[i][j] = "#"

def print_display() -> int:
    global display
    n = 0
    for row in display:
        for col in row:
            if col == "#":
                n += 1
            sys.stdout.write("{} ".format(col))
        print("")
    return n

if len(sys.argv) < 2:
    print("No data-file supplied")
    sys.exit(1)

process_data(read_data(sys.argv[1]))
print("Nr px: {}".format(print_display()))
