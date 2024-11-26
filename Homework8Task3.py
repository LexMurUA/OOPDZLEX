import pickle 
import json
# shorts = {
#     'short_cut': 'long_cut'
# }
# with open('shop.json', 'w') as f:
#     json.dump(shorts, f, indent=4, ensure_ascii=False)

try:
    with open('shop.pkl', 'rb') as f:
        data_shop = pickle.load(f)

except:
    print('shop.pkl is empty')
    data_shop = {}

def save_data_shop():
    with open('shop.pkl', 'wb') as f:
        pickle.dump(data_shop, f)
