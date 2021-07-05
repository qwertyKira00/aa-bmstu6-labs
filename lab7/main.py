from algorithms import Dictionary
from time import time

COUNT = 10000

def main():
    data = Dictionary('person.csv')

    try:
        key = input("Введите ключ, по котрому будет осуществляться поиск: ")
    except:
        print("Ошибка ввода!")
        return

    if key == '':
        return

    print("\nValue:\n{0}\n".format(data.BruteForceSearch(key)))

    print("Time characteristics: \n")
    t1 = time()
    for _ in range(COUNT):
        data.BruteForceSearch(key)
    t2 = time()
    print("Brute force search: {0}".format(t2 - t1))

    t1 = time()
    new_dict = data.sorting_by_keys()
    list_keys = list(new_dict.keys())
    t2 = time()

    t1 = time()
    for _ in range(COUNT):
        data.BinarySearch(key, list_keys)
    t2 = time()
    print("Binary search time: {0}".format(t2 - t1))

    new_dict = data.NewDictCreation()

    t1 = time()
    for _ in range(COUNT):
        data.Search(key, new_dict)
    t2 = time()
    print("Frequency Analysis search: {0}".format(t2 - t1))


if __name__ == "__main__":
    main()
