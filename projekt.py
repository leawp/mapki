#!/usr/bin/python
file = open('labirynt3.txt')
mapa = file.readlines()
mapa = ''.join(mapa)
import pdb; pdb.set_trace()
visited = []
def findpath(mapa):
    mapa = mapa.split("\n")
    size = map(int, mapa[0].split(' '))
    mapa = mapa[1:]
    mapa = map(list, mapa)
    start = None
    for y in range(size[0]):
        for x in range(size[1]):
            if mapa[y][x] == '@':
                start = x,y
                break
        if start != None:
            break
    _findpath(mapa, start[0], start[1])

    visited.remove(start)
    for pos in visited:
        mapa[pos[1]][pos[0]] = '.'


    mapa = map(''.join, mapa)
    print('\n'.join(mapa))




def _findpath(mapa, x,y):
    if mapa[y][x] == '$':
        return True
    visited.append((x,y))
    if mapa[y][x+1] != '#' and (x+1, y) not in visited:
        if _findpath(mapa, x+1, y):
            return True
    if mapa[y-1][x] != '#' and (x, y-1) not in visited:
        if _findpath(mapa, x, y-1):
            return True
    if mapa[y][x-1] != '#' and (x-1, y) not in visited:
        if _findpath(mapa, x-1, y):
            return True
    if mapa[y+1][x] != '#' and (x, y+1) not in visited:
        if _findpath(mapa, x, y+1):
            return True
    return False


findpath(mapa)
