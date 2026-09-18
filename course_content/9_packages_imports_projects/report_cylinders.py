"""Report the volume of every cylinder listed in the dimensions file."""

from cylinders import cylinder_volume
from dimensions import read_dimensions

cylinders = read_dimensions("data/cylinders.csv")

print("Cylinder volume report")
print("")

for cylinder in cylinders:
    volume_cm3 = cylinder_volume(cylinder["radius_cm"], cylinder["height_cm"])
    print(cylinder["label"] + ": " + str(round(volume_cm3, 1)) + " cm3")
