# Chuỗi ký tự dài (Huỳnh)
import pickle
with open('sorted-inverse-index-data.pkl', 'rb') as file:
    my_list = pickle.load(file)
    file.close()
    chuoi_ky_tu_dai = ''
    miss_like = []
    for line in my_list:
        # [freq, postings_list, term] = line.split(',')
        # miss_like.append((freq,postings_list, len(chuoi_ky_tu_dai)))
        # chuoi_ky_tu_dai += term
        thistuple = (line[0], line[1], len(chuoi_ky_tu_dai))
        chuoi_ky_tu_dai += line[2]
        miss_like.append(thistuple)
    print(miss_like)    
    