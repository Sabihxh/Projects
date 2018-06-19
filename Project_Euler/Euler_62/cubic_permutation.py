def cubic_perms():
    cubes_count = {}
    cubes = set()
    sorted_cube_map = {}
    for x in xrange(9999, 1, -1):
        x_cubed = x**3
        xcubed_sorted = ''.join(sorted(str(x_cubed)))
        if xcubed_sorted not in cubes:
            cubes.add(xcubed_sorted)
        else:
            sorted_cube_map[x] = xcubed_sorted
            if xcubed_sorted not in cubes_count:
                cubes_count[xcubed_sorted] = 2
            else:
                cubes_count[xcubed_sorted] += 1

    for key, value in cubes_count.iteritems():
        if value == 5:
            print key, value
            print '---'*20
            for x, y in sorted_cube_map.iteritems():
                if y == key:
                    print x, y
            print '***'*20

cubic_perms()

