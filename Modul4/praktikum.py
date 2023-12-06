import math

def transformasiDecorator(transformasi_func, rotasi_func, scale_func):
    def decorator(func):
        def wrapper(x, y):
            hasilTransformasi = transformasi_func(x, y)
            hasilRotasi = rotasi_func(*hasilTransformasi)
            hasilSkala = scale_func(*hasilRotasi)
            return func(*hasilSkala)
        return wrapper
    return decorator

def translasi(tx, ty):
    return lambda x, y: (x + tx, y + ty)

def rotasi(sudut):
    return lambda x, y: (
        x * math.cos(math.radians(sudut)) - y * math.sin(math.radians(sudut)),
        x * math.sin(math.radians(sudut)) + y * math.cos(math.radians(sudut))
    )

def dilatasi(sx, sy):
    return lambda x, y: (x * sx, y * sy)

def lineEquation(x, y, M):
    C = y - M * x
    return f"y = {M:.2f}x + {C:.2f}"

def main(translasi, rotasi, dilatasi, equation):
    x = float(input("Masukkan nilai x titik A: "))
    y = float(input("Masukkan nilai y titik A: "))
    gradient_awal = float(input("Masukkan gradien awal: "))
    tx = float(input("Masukkan nilai translasi tx: "))
    ty = float(input("Masukkan nilai translasi ty: "))
    rotate = float(input("Masukkan nilai sudut rotasi: "))
    scale_x = float(input("Masukkan nilai skala pada sumbu x: "))
    scale_y = float(input("Masukkan nilai skala pada sumbu y: "))
    
    @transformasiDecorator(translasi(tx, ty), rotasi(rotate), dilatasi(scale_x, scale_y))
    def transformed_line_equation(x, y):
        return equation(x, y, gradient_awal)

    result_equation = transformed_line_equation(x, y)

    print(f"Persamaan garis yang melalui titik ({x},{y}) dan bergradien {gradient_awal:.2f}:")
    print(equation(x, y, gradient_awal))
    print("Persamaan garis baru setelah transformasi:")
    print(result_equation)

if __name__ == "__main__":
    main(translasi, rotasi, dilatasi, lineEquation)