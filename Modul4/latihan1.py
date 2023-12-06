def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

def main():
    print(perkalian(2)(3))

    multiplier_by_5 = perkalian(2)
    result = multiplier_by_5(3) 

    print(result)

if __name__ == "__main__":
    main()