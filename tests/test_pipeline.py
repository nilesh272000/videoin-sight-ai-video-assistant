from core.pipeline import build_insights

def test_insights():
    r = build_insights("The team agreed to delay the launch. Maya will prepare the checklist by Friday.")
    assert "summary" in r
    assert r["action_items"]
