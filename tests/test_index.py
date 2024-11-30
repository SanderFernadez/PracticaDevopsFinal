import requests

def test_index_page():
    response = requests.get("http://localhost:6060")
    assert response.status_code == 200
    assert "Hello World" in response.text
