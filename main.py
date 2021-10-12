# Problema 3: Numerele au semne alternante
'''
2 -3 4 -2 -2 4 5
'''


def get_longest_alternating_signs(lst: list[int]):
    return_list = []
    semn = -1
    if lst[0] > 0:
        semn = 1

    start, end = 0, 0
    start_current, end_current, maxim = 0, 0, 0

    for index in range(1, len(lst)):
        if semn < 0 and lst[index] > 0:
            end = index
            semn *= -1
        elif semn > 0 and lst[index] < 0:
            end = index
            semn *= -1
        else:
            if maxim < end - start + 1:
                maxim = end - start + 1
                start_current = start
                end_current = end
            start = index

    if maxim < end - start + 1:
        start_current = start
        end_current = end

    return_list = lst[start_current: end_current+1]

    return return_list


def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs(
        [2, -3, 2, 5, -2, -2, 1]) == [2, -3, 2]
    assert get_longest_alternating_signs(
        [-1, 2, -1, 2, -1, -1, 2, -5, 2, -5, 2]) == [-1, 2, -5, 2, -5, 2]
    assert get_longest_alternating_signs([-1, -1, -1, -1, 2]) == [-1, 2]
    assert get_longest_alternating_signs(
        [-2, 2, -2, 2, 2, -2, 2]) == [-2, 2, -2, 2]


test_get_longest_alternating_signs()


def solve_longest_alternating_sign():
    n = int(input("Scrie numarul de elemente din lista: "))
    lst = []
    for index in range(n):
        el = int(input(f"Scrie elementul {index}: "))
        lst.append(el)
    print(
        f"Cea mai lunga subsecventa cu numere care au semne alternante este: {get_longest_alternating_signs(lst)}")


# Problema 11: Toate numerele au același număr de biți de 1 în reprezentarea binară.

def get_longest_same_bit_counts(lst: list[int]):
    return_list = []
    start, end = 0, 0
    start_current, end_current, maxim = 0, 0, 0

    number_of_1s = 0
    current_number = lst[0]
    while current_number:
        number_of_1s += current_number & 1
        current_number >>= 1

    for index in range(1, len(lst)):
        current_number = lst[index]
        current_number_of_1s = 0
        while current_number:
            current_number_of_1s += current_number & 1
            current_number >>= 1

        if current_number_of_1s == number_of_1s:
            end = index

        else:
            if maxim < end - start + 1:
                maxim = end - start + 1
                start_current = start
                end_current = end
            number_of_1s = current_number_of_1s
            start = index

    if maxim < end - start + 1:
        start_current = start
        end_current = end

    return_list = lst[start_current: end_current+1]

    return return_list


def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts(
        [14, 7, 11, 5, 2, 4, 16, 64]) == [2, 4, 16, 64]
    assert get_longest_same_bit_counts([2, 14, 7, 9, 5, 12]) == [9, 5, 12]
    assert get_longest_same_bit_counts(
        [45, 37, 24, 101, 30, 23]) == [101, 30, 23]


test_get_longest_same_bit_counts()


def solve_get_longest_same_bit_counts():
    n = int(input("Scrie numarul de elemente din lista: "))
    lst = []
    for index in range(n):
        el = int(input(f"Scrie elementul {index}: "))
        lst.append(el)

    print(
        f"Cea mai lunga subsecventa cu numere care au acelasi numar de biti 1 este: {get_longest_same_bit_counts(lst)}")


def main():

    isrunning = True
    while isrunning:
        meniu = "Proprietatea 1: Numerele au semne alternante.\nProprietatea 2: Toate numerele au același număr de biți de 1 în reprezentarea binară.\nx - program incheiat"
        print("Meniu:\n" + meniu)
        proprietatea = input("Scrie numarul prorietatii: ")

        if proprietatea == "1":
            print("Ai ales proprietatea 1: Numerele au semne alternante.")
            solve_longest_alternating_sign()
        elif proprietatea == "2":
            print(
                "Ai ales proprietatea 2: Toate numerele au același număr de biți de 1 în reprezentarea binară.")
            solve_get_longest_same_bit_counts()
        elif proprietatea == 'x':
            print("Program incheiat!")
            isrunning = False
        else:
            print("Ai scris o comanda invalida, incearca din nou!")


if __name__ == "__main__":
    main()
