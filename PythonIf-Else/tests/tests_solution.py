import pytest
import os
import sys
sys.path.append(os.path.abspath(".."))

from solution import solution_if_else


def test_solution_on_odd(capfd):
    n = 5
    solution_if_else(n)

    captured = capfd.readouterr()

    assert captured.out.strip() == "Weird"

def test_solution_on_even_between_2_5(capfd):
    n = 4
    solution_if_else(n)

    captured = capfd.readouterr()

    assert captured.out.strip() == "Not Weird"

def test_solution_on_even_between_6_20(capfd):
    n = 10
    solution_if_else(n)

    captured = capfd.readouterr()

    assert captured.out.strip() == "Weird"

def test_solution_on_even_between_6_20(capfd):
    n = 34
    solution_if_else(n)

    captured = capfd.readouterr()

    assert captured.out.strip() == "Not Weird"