import requests
import os

id = 0
base_url = "https://dev.azure.com/Japan-Apps-and-Infra/SOMPO-HD-DevOps/_apis/wit/workitems/"
api_version = "7.1-preview.3"

# authorized_user = "AKIAXXXXXXXXXXXXXXXX"
authorized_user = os.environ.get("AUTHORIZED_USER_PAT")
unauthorized_user = os.environ.get("UNAUTHORIZED_USER_PAT")


def setup_function():
    url = f"{base_url}$product%20backlog%20item?api-version={api_version}"
    headers = {
        "Authorization": f"Basic {authorized_user}",
        "Content-Type": "application/json-patch+json",
    }
    body = [
        {
            "op": "add",
            "path": "/fields/System.Title",
            "value": "PBI for test",
        }
    ]
    response = requests.post(url, headers=headers, json=body)
    global id
    id = response.json()["id"]


def teardown_function():
    url = f"{base_url}{id}?api-version={api_version}"
    headers = {
        "Authorization": f"Basic {authorized_user}"
    }
    requests.delete(url, headers=headers)


def delete_work_item(id, user):
    url = f"{base_url}{id}?api-version={api_version}"
    headers = {"Authorization": f"Basic {user}"}
    response = requests.delete(url, headers=headers)
    return response


def test_delete_work_item_by_authorized_user():
    response = delete_work_item(id, authorized_user)
    assert response.status_code == 200


def test_delete_work_item_by_unauthorized_user():
    response = delete_work_item(id, unauthorized_user)
    assert response.json()["code"] == 404
    assert (
        response.json()["message"]
        == f"VS403145: Insufficient permissions to delete work item {id}."
    )
