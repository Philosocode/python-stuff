import pickle

my_dict = {1: "6", 2: "2", 3: "f"}

pickle_out = open("dict.pickle", "wb")
pickle.dump(my_dict, pickle_out)
pickle_out.close()
