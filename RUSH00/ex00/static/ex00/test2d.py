
def make_grid(width, position):
    grid = []
    for y in range (0, width):
        new = []
        for x in range (0, width):
            if (x == position['x']) and (y == position['y']):
                new.append('Y')
            else:
                new.append('X')
        grid.append(new)
    return grid

def worldmap(request):
    print("hey new game?")
    width = 3
    position = { 'x' : width-1, 'y' : width-1 }
    return render(request, "ex00/worldmap.html", { 'grid': grid })

if __name__ == "__main__":
    width = 5
    position = { 'x' : width-1, 'y' : width-1 }
    print(make_grid(width, position))
    position = { 'x' : 2, 'y' : 2 }
    print(make_grid(width, position))
    position = { 'x' : 0, 'y' : 0 }
    print(make_grid(width, position))
