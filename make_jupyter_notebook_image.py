import os

def train_file(path):
    os.system('python global1.py '+ path)

def test_file(path):
    os.system('python train_test.py ' + path)

def main(train_path,test_path):

    print("\n\nInside Main")
    print(train_path,test_path)

    print('Training....')
    train_file(train_path)

    print('Testing....')
    test_file(test_path)