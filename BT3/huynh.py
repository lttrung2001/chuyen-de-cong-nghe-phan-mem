# Chuỗi ký tự dài (Huỳnh)
file = open('inverse-index-data.txt', 'r')
chuoi_ky_tu_dai = ''
my_list = []
for line in file:
    [term, freq, postings_list] = line.split('::')
    my_list.append((freq, len(chuoi_ky_tu_dai)))
    chuoi_ky_tu_dai += term
print(chuoi_ky_tu_dai[:10])
print(my_list)