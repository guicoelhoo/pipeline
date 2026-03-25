from app import quiz

def test_quiz_certo():
    assert quiz("sao paulo") == "certo"

def test_quiz_errado():
    assert quiz("flamengo") == "errado"
