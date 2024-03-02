def increment_version(version):

    parts = list(map(int, version.split('.')))

    parts[2] += 1

    if parts[2] > 9:
        parts[2] = 0
        parts[1] += 1

    if parts[1] > 9:
        parts[1] = 0
        parts[0] += 1

    next_version = '.'.join(map(str, parts))
    return next_version

current_version = input()
next_version = increment_version(current_version)
print(next_version)
