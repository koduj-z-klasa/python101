#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def fib_iter1(n):  # definicja funkcji
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą while.
    """
    pwyrazy = (0, 1)  # dwa pierwsze wyrazy ciągu zapisane w tupli
    a, b = pwyrazy  # przypisanie wielokrotne, rozpakowanie tupli
    print(a, end=" ")
    while n > 1:
        print(b, end=" ")
        a, b = b, a + b  # przypisanie wielokrotne
        n -= 1


def fib_iter2(n):
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą for.
    """
    a, b = 0, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n - 1):
        # wynik = a + b
        a, b = b, a + b
        print("wyraz", i + 2, b)

    print()  # wiersz odstępu
    return b


def fib_rek(n):
    """
        Funkcja zwraca n-ty wyraz ciągu Fibonacciego.
        Wersja rekurencyjna.
    """
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2)


def main(args):
    n = int(input("Podaj nr wyrazu: "))
    fib_iter1(n)
    print()
    print("=" * 40)
    fib_iter2(n)
    print("=" * 40)
    print(fib_rek(n - 1))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
