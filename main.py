import random
from sphere import Sphere
from cube import Cube
from cylinder import Cylinder

shapes = []

for _ in range(10):
    shape_type = random.choice(['sphere', 'cylinder', 'cube'])
    
    if shape_type == 'sphere':
        r = random.randint(1, 10)
        shapes.append(Sphere(r))
    elif shape_type == 'cylinder':
        r = random.randint(1, 10)
        h = random.randint(5, 20)
        shapes.append(Cylinder(r, h))
    elif shape_type == 'cube':
        a = random.randint(1, 10)
        shapes.append(Cube(a))

# Вывод
for shape in shapes:
    print(f"{shape}")
    print(f"  Surface Area: {shape.surface_area():.2f}")
    print(f"  Volume: {shape.volume():.2f}")
    print()
