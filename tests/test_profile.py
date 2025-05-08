def test_user_can_update_profile(async_client, user, token):
    response = await async_client.put(
        "/profile",
        headers={"Authorization": f"Bearer {token}"},
        json={"bio": "New Bio", "location": "New York"},
    )
    assert response.status_code == 200
    assert response.json()["bio"] == "New Bio"


def test_admin_can_upgrade_user(async_client, admin_token, user):
    response = await async_client.put(
        "/admin/upgrade-user",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"user_id": str(user.id), "professional_status": True},
    )
    assert response.status_code == 200
    assert response.json()["professional_status"] is True
