from rpn_calc import main


def test_sum():
    commands = ['1.0', '2.0', '+']
    assert main(commands) == 3.0


def test_prod():
    commands = ['3.0', '2.0', '*']
    assert main(commands) == 6.0


def test_subtract():
    commands = ['2.0', '1.0', '-']
    assert main(commands) == 1.0
