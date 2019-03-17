import random


def generate_sentence(length=10):
    words = ['one', 'two', 'three', 'four', 'five', 'blue', 'red',
             'green', 'yellow', 'brown', 'black', 'in', 'a', 'on']

    bag_of_words = []

    for i in range(length):
        bag_of_words.append(random.choice(words))

    sent = ' '.join(bag_of_words).capitalize()

    return sent


def generate_text(num_of_sentences=100, sent_len=10):
    path = './text'
    with open(path, mode='w') as file:
        for i in range(num_of_sentences):
            file.write(generate_sentence(sent_len))
            file.write('.\n')

        file.close()


def main():
    generate_text(100000000, 40)


if __name__ == '__main__':
    main()
