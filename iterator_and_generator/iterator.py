class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list


    def __iter__(self):
        self.cursor = 0
        self.nest_cursor = 0
        return self

    def __next__(self):

        if self.nest_cursor >= len(self.list_of_list[self.cursor]):
            self.cursor += 1
            self.nest_cursor = 0
        if self.cursor == len(self.list_of_list):
            raise StopIteration
        self.nest_cursor += 1
        return self.list_of_list[self.cursor][self.nest_cursor - 1]


def test_1():

    list_of_lists_1 = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1),
                                              ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        assert flat_iterator_item == check_item

        assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
if __name__ == '__main__':
    test_1()
