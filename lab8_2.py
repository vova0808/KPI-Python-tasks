def find_fraction(summ):
    if summ <= 2:
        return False
    medium = float(summ) / 2
    if summ % 2 == 0:
        if medium % 2 == 0:
            return int(medium - 1), int(medium + 1)
        else:
            return int(medium - 2), int(medium + 2)
    else:
        return int(medium - 0.5), int(medium + 0.5)








