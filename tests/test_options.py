# -*- coding: utf-8 -*-

import pytcm


########
# FLAG #
########
def test_flag_default_returns_empty():
    flag = pytcm.Flag("--test")
    result = flag.parse()

    assert result == ""


def test_flag_True_returns_flag():
    flag = pytcm.Flag("--test", True)
    result = flag.parse()

    assert result == "--test"


def test_flag_False_returns_empty():
    flag = pytcm.Flag("--test", False)
    result = flag.parse()

    assert result == ""


##############
# Positional #
##############
def test_positonal_default_returns_empty():
    positional = pytcm.Positional()
    result = positional.parse()

    assert result == ""


def test_positonal_value_returns_str():
    positional = pytcm.Positional("test")
    result = positional.parse()

    assert result == "test"


############
# Implicit #
############
def test_implicit_default_returns_empty():
    implicit = pytcm.Implicit("--test")
    result = implicit.parse()

    assert result == ""


def test_implicit_value_returns_str():
    implicit = pytcm.Implicit("--test", 12)
    result = implicit.parse()

    assert result == "--test 12"


############
# Explicit #
############
def test_explicit_default_returns_empty():
    explicit = pytcm.Explicit("--test")
    result = explicit.parse()

    assert result == ""


def test_explicit_value_returns_str():
    explicit = pytcm.Explicit("--test", 12)
    result = explicit.parse()

    assert result == "--test=12"
