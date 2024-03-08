import pytest


def remove_leading_spaces(s: str) -> str:
    return s.lstrip()

@pytest.mark.parametrize("test_input,expected", [
    ("  leading spaces", "leading spaces"),
    ("leading spaces  ", "leading spaces  "),
    ("\tleading tab", "leading tab"),
    ("   \t mixed spaces and tab", "mixed spaces and tab"),
    ("no_leading_space", "no_leading_space"),
    ("　全角スペース", "全角スペース"),
    ("\t　 全角スペース", "全角スペース")
])
def test_remove_leading_whitespace(test_input, expected):
    assert remove_leading_spaces(test_input) == expected
