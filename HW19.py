class Building:
    total = 0

    def __init__(self):
        Building.total += 1


b = Building()
for i in range(40):
    b = Building()
    print(b)
