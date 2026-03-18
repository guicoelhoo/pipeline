from app import quiz

def test_quiz_certo():
    assert quiz("palmeiras") == "certo"

def test_quiz_errado():
    assert quiz("flamengo") == "errado"
