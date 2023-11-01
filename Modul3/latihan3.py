random_list = [3.1, 2.7, 5.5, 105, 737, 412, 'Hello', 'Python', 'world', 'AI']

float_data = list(filter(lambda val: isinstance(val, float), random_list))
int_data = list(filter(lambda val: isinstance(val, int), random_list))
string_data = list(filter(lambda val: isinstance(val, str), random_list))

intdata_mapped = list(map(lambda x: {'ratusan': x // 100, 'puluhan': (x % 100) // 10, 'satuan': x % 10}, int_data))

print("Data Float:")
print(float_data)
print("Data Int:")
for item in intdata_mapped:
    print(item)
print("Data String:")
print(string_data)