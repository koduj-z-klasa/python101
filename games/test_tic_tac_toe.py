# coding=utf-8
# Copyright 2014 Janusz Skonieczny

"""
Testy jednostkowe dla modułu tic_tac_toe.py
"""

from unittest import TestCase
from ticatactoe import check_win, Ai


class WinTests(TestCase):
    def test_win1(self):
        markers = [
            'X', 'O', 'O',
            'O', 'X', 'X',
            'O', 'O', 'X'
        ]
        self.assertTrue(check_win(markers, True))

    def test_win2(self):
        markers = [
            'X', 'O', 'O',
            'O', 'O', 'X',
            'X', 'X', 'X'
        ]
        self.assertTrue(check_win(markers, True))

    def test_win3(self):
        markers = [
            'X', 'O', 'X',
            'O', 'O', 'X',
            'O', 'X', 'X'
        ]
        self.assertTrue(check_win(markers, True))

    def test_win4(self):
        markers = [
            'X', 'O', 'X',
            'X', None, 'X',
            'X', 'X', None
        ]
        self.assertTrue(check_win(markers, True))

    def test_draw(self):
        markers = [
            'X', 'O', 'X',
            'O', 'O', 'X',
            'X', 'X', 'O'
        ]
        self.assertFalse(check_win(markers, True))


class NextMoveTest(TestCase):
    def test_move1(self):
        markers = [
            'X', None, 'O',
            'O', 'O', 'X',
            'X', None, 'X'
        ]
        self.assertEqual(7, Ai.next_move(markers))

    def test_move2(self):
        markers = [
            'X', None, 'X',
            'O', 'O', 'X',
            'X', None, 'O'
        ]
        self.assertEqual(1, Ai.next_move(markers))

    def test_move3(self):
        markers = [
            'X', None, 'X',
            'O', 'O', 'X',
            'X', None, 'O'
        ]
        self.assertEqual(1, Ai.next_move(markers))
