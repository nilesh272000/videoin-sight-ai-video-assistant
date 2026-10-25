from core.retriever import retrieve

def test_retrieve():
    text = "The payment integration has a critical bug. Maya will prepare the launch checklist."
    result = retrieve("payment bug", text)
    assert result
    assert "payment" in result[0].lower()
