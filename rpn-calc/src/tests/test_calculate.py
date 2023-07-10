from rpn_calc import main


def test_sum():
    commands = ['1', '2', '+']
    assert main(commands) == 3


def test_prod():
    commands = ['3', '2', '*']
    assert main(commands) == 6
