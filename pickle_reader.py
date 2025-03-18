import pickle

file_path = 'final_model/preprocessor.pkl'

try:
    with open(file_path, 'rb') as f:
     data = pickle.load(f)
    print(data)

except EOFError:

  print("File is empty")
