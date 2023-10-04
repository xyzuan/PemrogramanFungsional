random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

float_tuple = ()
str_list = []
int_dict = {}

for value in random_list:
    if isinstance(value, int):
        satuan = value % 10
        puluhan = (value // 10) % 10
        ratusan = value // 100
        int_dict[value] = {
            "satuan"    : satuan,
            "puluhan"   : puluhan,
            "ratusan"   : ratusan,
        }
    elif isinstance(value, float):
        float_tuple += (value,)
    elif isinstance(value, str):
        str_list.append(value)

print('float:', float_tuple)
print('str:', str_list)
print('int:', int_dict)
