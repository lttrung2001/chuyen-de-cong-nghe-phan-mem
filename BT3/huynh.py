# Chuỗi ký tự dài (Huỳnh)
# file = open('inverse-index-data.txt', 'r')
import pickle
with open('sorted-inverse-index-data.pkl', 'rb') as file:
    my_list = pickle.load(file)
    chuoi_ky_tu_dai = ''
    print(my_list)
    # print("=======================\n\n\n\n\n\n")
    miss_like = []
    for line in my_list:
        # [freq, postings_list, term] = line.split(',')
        # miss_like.append((freq,postings_list, len(chuoi_ky_tu_dai)))
        # chuoi_ky_tu_dai += term
        thistuple = (line[0], line[1], len(chuoi_ky_tu_dai))
        chuoi_ky_tu_dai += line[2]
        miss_like.append(thistuple)
    print(miss_like)    
    