from validBraces import validBraces

def test_validraces():
    assert validBraces('(((([{}]))))') == 'Сбалансированно'
    assert validBraces('[([])((([[[]]])))]{()}') == 'Сбалансированно'
    assert validBraces('{{[()]}}') == 'Сбалансированно'
    assert validBraces('}{}') == 'Несбалансированно'
    assert validBraces('{{[(])]}}') == 'Несбалансированно'
    assert validBraces('[[{())}]') == 'Несбалансированно'