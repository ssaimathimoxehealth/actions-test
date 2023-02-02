import requests
import pytest

@pytest.mark.for_github_actions_trigger
def test_get_products_list():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
       "https://automationexercise.com/api/productsList",
        headers=headers,
    )

    assert response.status_code == 200