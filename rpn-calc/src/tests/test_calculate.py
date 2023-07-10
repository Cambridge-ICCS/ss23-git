from rpn_calc import main


def test_sum():
    commands = ['1', '2', '+']
    assert main(commands) == 3


def test_prod():
    commands = ['3', '2', '*']
    assert main(commands) == 6


def test_subtract():
    commands = ['2.0', '1.0', '-']
    assert main(commands) == -1.0


def test_modulo():
    commands = ['7.0', '15.0', '%']
    assert main(commands) == 1.0
