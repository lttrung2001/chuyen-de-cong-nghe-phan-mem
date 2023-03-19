from vb_code import *
from read_inverse_index import read_inverse_index
from entities.InverseIndex import InverseIndex
import pickle

def compress():
    d = read_inverse_index()
    res_dict = {k: InverseIndex(v.freq, list(map(lambda i: vb_encode(i), v.s))) for k, v in d.items()}
    return res_dict

def extract():
    d = read_compress()
    res_dict = {k: InverseIndex(v.freq, set(map(lambda i: int(''.join([str(i) for i in vb_decode(i)])), v.s))) for k, v in d.items()}
    return res_dict


def write_compress():
    with open('vb-compress-data.pkl', 'wb') as f:
        pickle.dump(compress(), f, protocol=pickle.HIGHEST_PROTOCOL)

def read_compress():
    with open('vb-compress-data.pkl', 'rb') as f:
        return pickle.load(f)

if __name__ == '__main__':
    d = extract()
    print(d)
