"""Reading cylinder dimensions from a file."""


def read_dimensions(path):
    """Read cylinder dimensions from a CSV file.

    The first line is a header and is ignored. Every other line holds a
    label, a radius and a height, separated by commas. Returns a list of
    dictionaries, one per cylinder.
    """
    cylinders = []

    with open(path) as dimensions_file:
        lines = dimensions_file.readlines()

    for line in lines[1:]:
        line = line.strip()

        if line != "":
            parts = line.split(",")
            cylinders.append({
                "label": parts[0],
                "radius_cm": float(parts[1]),
                "height_cm": float(parts[2]),
            })

    return cylinders
