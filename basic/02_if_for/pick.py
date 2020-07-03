import pickle

data = {1:'pythoh', 2:'you need'}

print(type(data))

with open("test.pickle", "wb") as f:
    pickle.dump(data, f)

with open("test.pickle", "rb") as f:
    data = pickle.load(f)
    print(data)