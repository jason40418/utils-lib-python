from utils.sample import Sample


def test_get_true_func():
    assert Sample().true_test() is True
