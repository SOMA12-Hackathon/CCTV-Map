import pickle


print(1)

def get_cctv_list():
    with open('cctv_list.p', 'rb') as f:
        cctv_list = pickle.load(f)
    return cctv_list

x = get_cctv_list()

for i in x[:30]:
    print(i)