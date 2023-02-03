
class PhoneBook:

    phone_book = []
    path = 'fone_book\phone_book.txt'

    def __init__(self, path: str = 'fone_book\phone_book.txt'):
        self.path = path
        self.open()

    def get(self):
        return self.phone_book

    def get_contact(self, record: str):
        result = []
        for i, contact in enumerate(self.phone_book):
            for field in contact:
                if record in field:
                    result.append((contact, i))
                    break
        if len(result) > 1:
            return False
        elif result == []:
            return result
        else:
            return result[0]


    def open(self):
        with open(self.path, 'r', encoding='UTF-8') as data:
            file = data.readlines()
        for contact in file:
            self.phone_book.append(contact.strip().split(';'))
        

    def save(self):
        pb_str = []
        for contact in self.phone_book:
            pb_str.append(';'.join(contact))
        with open(self.path, 'w', encoding='UTF-8') as data:
            data.write('\n'.join(pb_str))
        

    def new(self, new_contact: list):
        self.phone_book.append(new_contact)


    def search(self, find: str):
        result = []
        for contact in self.phone_book:
            for field in contact:
                if find in field:
                    result.append(contact)
                    break
        return result


    def delete(self, contact: list):
       self.phone_book.remove(contact)


    def change_contact(self, index: int, new: list):
        self.phone_book[index][0] = new[0] if new[0] != '' else self.phone_book[index][0]
        self.phone_book[index][1] = new[0] if new[1] != '' else self.phone_book[index][1]
        self.phone_book[index][2] = new[2] if new[2] != '' else self.phone_book[index][2]

                