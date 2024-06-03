from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list_ = list(rows)


def new_contacts(contacts_list):
    contacts = []
    for i in contacts_list[1:]:
        pattern_1 = r"(8|\+7)[\(\s*]?\(?(\d{3})\)?[\s*\-]?(\d{3})[\s*\-]?(\d{2})[\s*\-]?(\d{2})"
        pattern_2 = r"\(?\доб. (\d+)\)?"
        name = ' '.join(i).split(' ')[:3]
        number = ''.join(i[5])
        result_number = re.sub(pattern_1, r"+7(\2)\3-\4-\5", number)
        res = re.sub(pattern_2, r"доб.\1", result_number)
        i[5] = res
        contacts.append(name + i[3::])
    for i in contacts:
        index_ = contacts.index(i)
        for q in contacts[index_+1::]:
            if ' '.join(i[:2]) == ' '.join(q[:2]):
                for y in range(len(q)):
                    if contacts[index_][y] == '':
                        contacts[index_][y] = q[y]
                contacts.pop(contacts.index(q))
    contacts.insert(0, contacts_list_[0])
    return contacts
if __name__ == '__main__':
    with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts(contacts_list_))
        pprint(new_contacts(contacts_list_))