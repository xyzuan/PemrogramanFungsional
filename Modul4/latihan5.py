def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    M = (p2[1] - p1[1]) / (p2[0] - p1[0])
    C = p1[1] - M * p1[0]

    return f"y = {M:.2f}x + {C:.2f}"


def main():
    print("Persamaan garis yang melalui titik A dan B:")
    print(line_equation_of(point(1,1),point(4,7)))

if __name__ == "__main__":
    main()