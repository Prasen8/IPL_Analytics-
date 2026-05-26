import pickle
import os

for file in os.listdir():
    if file.endswith(".pkl"):
        try:
            obj = pickle.load(open(file,'rb'))
            print("\n", file)
            print(type(obj))
        except Exception as e:
            print(file, e)