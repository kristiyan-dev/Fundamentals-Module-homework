def fill_shells(electrons):
    filled_shells = []
    shell_position = 1

    while electrons > 0:
        max_electrons_in_shell = 2 * shell_position ** 2

        if electrons >= max_electrons_in_shell:
            filled_shells.append(max_electrons_in_shell)
            electrons -= max_electrons_in_shell
        else:
            filled_shells.append(electrons)
            electrons = 0

        shell_position += 1

    return filled_shells

# Example usage:
electrons = int(input())
result = fill_shells(electrons)
print(result)
