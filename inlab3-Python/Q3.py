import os

os.mkdir('./Data/Survivors_of_Snap')
def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

#https://stackoverflow.com/questions/13259288/returning-a-list-of-words-after-reading-a-file-in-python

Heroes = read_words('./Data/Heroes.txt')

for word in Heroes:
    for file in os.listdir('./Data/Avengers_Universe'):
        with open('./Data/Avengers_Universe/%s' % file) as f:
            if word in f.read():
               os.rename('./Data/Avengers_Universe/%s' % file,'./Data/Survivors_of_Snap/%s' % file)
