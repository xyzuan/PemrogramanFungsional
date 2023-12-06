import math

def translasi(x, y):
    def inner(tx, ty):
        new_x = x + tx
        new_y = y + ty
        return new_x, new_y
    return inner

def dilatasi(x, y):
    def inner(sx, sy):
        new_x = x * sx
        new_y = y * sy
        return new_x, new_y
    return inner

def rotasi_formatter(function):
    def innner(*args, **kwargs):
        rotasi = function(*args, **kwargs)
        return f"{rotasi[0]:.2f}, {rotasi[1]:.2f}"
    return innner

@rotasi_formatter
def rotasi(x, y, sudut):
    radian = math.radians(sudut)
    new_x = x * math.cos(radian) - y * math.sin(radian)
    new_y = x * math.sin(radian) + y * math.cos(radian)
    return new_x, new_y

def main():
    titik_P = (3, 5)

    titik_setelah_translasi = translasi(titik_P[0], titik_P[1])(2, -1)
    print("Koordinat setelah translasi:", titik_setelah_translasi)

    titik_setelah_dilatasi = dilatasi(titik_P[0], titik_P[1])(2, -1)
    print("Koordinat setelah dilatasi:", titik_setelah_dilatasi)

    titik_setelah_rotasi = rotasi(*titik_P, 30)
    print("Koordinat setelah rotasi:", titik_setelah_rotasi)

if __name__ == "__main__":
    main()