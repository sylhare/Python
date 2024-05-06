import pytest

from src.examples.Interview.questions.binary_tree import in_order, deserialize_tree, height, level_order, post_order, \
    top_view, top_view_recursive, pre_order


@pytest.mark.parametrize("function", [in_order, pre_order, level_order, post_order, top_view, top_view_recursive])
@pytest.mark.parametrize("tree", [
    "1 2 5 3 4 6",
    "2 1 3 4 5 6",
    "5 1 3 6 2 4",
    "5 1 6 2 4 3",
    "6 2 5 3 8 1 9",
    "33 21 20 35 34 54",
    "12 6 6 5 4 2 6 2 12 3"
])
def test_order(function, tree):
    function(deserialize_tree(tree).root)


def test_height():
    assert height(deserialize_tree("1 2 5 3 4 6").root) == 4
    assert height(deserialize_tree("5 1 3 6 2 4").root) == 3
