from stack import Stack


def test_new_stack_is_empty():
    s = Stack()
    assert s.is_empty()


def test_when_pushing_item_stack_is_not_empty():
    s = Stack()
    s.push(1)
    assert not s.is_empty()


def test_popping_from_one_element_stack_is_empty_stack():
    s = Stack()
    s.push(1)
    s.pop()
    assert s.is_empty()


def test_popping_from_one_element_stack_returns_the_pushed_element():
    s = Stack()
    s.push(1)
    item = s.pop()
    assert item == 1


def test_stack_behaves_as_first_in_last_out():
    s = Stack()
    s.push(1)
    s.push(3)
    item = s.pop()
    assert item == 1
    item = s.pop()
    assert item == 3


def test_stack_is_iterable_while_preserving_filo_beh():
    # Given a stack with 3 elements
    s = Stack()
    s.push(1)
    s.push(5)
    s.push(3)

    # When popping the 3 elements
    iterator = iter(s)
    item = next(iterator)
    assert item == 1
    item = next(iterator)
    assert item == 5
    item = next(iterator)
    assert item == 3

    # if next outside the last StopIteration is raised
    try:
        next(iterator)
    except Exception as e:
        assert isinstance(e, StopIteration)

    # then the stack is empty
    assert s.is_empty()


# s = [3, 5, 7]
# s.pop() == 3
# [5, 7]
# s.push(2)
# [2, 5, 7]
# s.pop() == 2
# s.push(4)
# s.push(6)
# [6, 4, 5, 7]

def test():
    s = Stack()
    s.push(4)
    s.push(3)
    item = s.pop()
    assert item == 4
