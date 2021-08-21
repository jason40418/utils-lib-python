from utils.convert.convert_string import ConvertString


def test_empty_string():
    test_list = list()
    cs = ConvertString()
    result = cs.list_to_string(test_list, '|')
    assert result == ''


def test_default_seperator():
    test_list = [10, 'eng', '0']
    cs = ConvertString()
    result = cs.list_to_string(test_list)
    assert result == '10|eng|0'


def test_comma_seperator():
    test_list = [10, 'eng', '0']
    cs = ConvertString()
    result = cs.list_to_string(test_list, ',')
    assert result == '10,eng,0'
