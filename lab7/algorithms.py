from patientClass import Patient


class Dictionary(object):
    data = dict()

    def __init__(self, file_name):
        self.GetDataFromFile(file_name)

    def GetDataFromFile(self, file_name):
        file = open(file_name, 'r')

        for line in file:
            arr = line.split(';')
            key = arr[1]
            self.data[key] = Patient(arr[2],
                                     float(arr[3]), arr[4], arr[5], int(arr[6]))
        # print(self.data)

        file.close()

    def Log(self):
        for elem in self.data:
            print(elem)
            print(self.data.setdefault(elem))

    def __getitem__(self, key):
        return self.data.get(key)

    def sorting_by_keys(self):
        new_dict = dict()
        list_keys = list(self.data.keys())
        list_keys.sort()

        for i in list_keys:
            new_dict[i] = self.data[i]

        return new_dict

    def sorting_by_values(self, data):
        new_dict = dict()

        list_d = list(data.items())
        list_d.sort(key=lambda i: i[1], reverse=True)
        for x in list_d:
            new_dict[x[0]] = x[1]

        return new_dict

    def BruteForceSearch(self, key):
        for x in self.data:
            if key == x:
                return self.data[x]
        return -1

    def BinarySearch(self, key, list_keys):
        left, right = 0, len(list_keys) - 1

        while left <= right:
            middle = (right + left) // 2  
            x = list_keys[middle]

            if x == key:
                return self.data[x]

            elif x < key:
                left = middle + 1

            else:
                right = middle - 1

        return -1

    def NewDictCreation(self):
        count_dict = {i: 0 for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        
        for key in self.data:
            count_dict[key[0]] += 1

        count_dict = self.sorting_by_values(count_dict)

        new_dict = {i: dict() for i in count_dict}

        for key in self.data:
            new_dict[key[0]].update({key: self.data[key]})

        return new_dict

    def Search(self, key, new_dict):
        for letter in new_dict:
            if key[0] == letter:
                for x in new_dict[letter]:
                    if x == key:
                        return new_dict[letter][x]
                return -1

        return -1
