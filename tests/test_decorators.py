import pytest

import os

from src.decorators import log
from config import path

def test_log_console_ok(capsys):

    @log()
    def example_func(a, b):
        return a + b

    example_func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "example_func ok\n"


def test_log_console_error(capsys):

    @log()
    def example_func(a, b):
        return a + b

    example_func([], {})
    captured = capsys.readouterr()
    assert captured.out == """example_func error: can only concatenate list (not "dict") to list. Inputs: ([], {}), {}\n"""


def test_log_file_ok():
    @log("test.txt")
    def example_func(a, b):
        return a + b

    example_func(1, 2)
    with open(os.path.join(path, "test.txt"), "r", encoding="utf-8") as f:
        data = f.read().split("\n")[:-1]
        assert data[-1] == "example_func ok"


def test_log_file_error():
    @log("test.txt")
    def example_func(a, b):
        return a + b

    example_func([], {})
    with open(os.path.join(path, "test.txt"), "r", encoding="utf-8") as f:
        data = f.read().split("\n")[:-1]
        assert data[-1] == """example_func error: can only concatenate list (not "dict") to list. Inputs: ([], {}), {}"""
