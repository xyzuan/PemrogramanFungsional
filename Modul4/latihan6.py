x1 = 1
y1 = 4
m = 7

def point(x, y):
    return x, y

def line_equation_of(x1, y1, M):
    C = y1 - M * x1
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (1,4) dan bergradien 7:")
print(line_equation_of(x1, y1, m))


print(f"C = {y1 - ( m * x1 )}")
print(f"M = {m}")
