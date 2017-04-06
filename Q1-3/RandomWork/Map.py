#Map
squares = []

def square(squares = []):
    for i in range(1000):
        for x in range(0,2):
            squares.append(x**2)
    return squares

print(square())
print(map(square, squares))
