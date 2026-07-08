import pytest
from utils import checking_balance_brackets


params = (
    ('(((([{}]))))', 'Balanced'),
    ('[([])((([[[]]])))]{()}', 'Balanced'),
    ('{{[()]}}', 'Balanced'),
    ('}{}', 'Unbalanced'),
    ('{{[(])]}}', 'Unbalanced'),
    ('[[{())}]', 'Unbalanced'),
)


@pytest.mark.parametrize(
    'string, expected',
    params
)


def test_checking_balance_brackets(string, expected):
    assert checking_balance_brackets(string) == expected
