import pickle

def load(filename):
    with open(filename, 'rb') as f:
        loaded = pickle.load(f)
    return loaded

def save(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f, protocol=4)
    return
