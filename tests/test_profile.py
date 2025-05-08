async def test_user_can_update_profile(async_client, user, token):
    response = await async_client.put(
        "/profile",
        headers={"Authorization": f"Bearer {token}"},
        json={"bio": "New Bio", "location": "New York"},
    )
    assert response.status_code == 200
    assert response.json()["bio"] == "New Bio"


async def test_bio_too_long(async_client, token):
    long_bio = "x" * 501  # Exceeds the 500 character limit
    response = await async_client.put(
        "/profile",
        headers={"Authorization": f"Bearer {token}"},
        json={"bio": long_bio},
    )
    assert response.status_code == 422


async def test_location_too_long(async_client, token):
    long_location = "x" * 256  # Exceeds the 255 character limit
    response = await async_client.put(
        "/profile",
        headers={"Authorization": f"Bearer {token}"},
        json={"location": long_location},
    )
    assert response.status_code == 422


async def test_unauthorized_profile_update(async_client):
    response = await async_client.put(
        "/profile",
        json={"bio": "New Bio", "location": "New York"},
    )
    assert response.status_code == 401  # Unauthorized


async def test_profile_update_with_empty_payload(async_client, token):
    response = await async_client.put(
        "/profile",
        headers={"Authorization": f"Bearer {token}"},
        json={},
    )
    assert response.status_code == 200
    # The profile should keep its existing values


async def test_default_values_in_new_profile(async_client, token):
    # First get the current user profile
    response = await async_client.get(
        "/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    user_data = response.json()
    
    # Check that bio and location have default empty string values
    assert user_data["bio"] == "" or user_data["bio"] is None
    assert user_data["location"] == "" or user_data["location"] is None


async def test_profile_fields_visible_in_me(async_client, token):
    response = await async_client.get(
        "/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    user_data = response.json()
    
    # Check that all profile fields are present
    assert "bio" in user_data
    assert "location" in user_data
    assert "is_professional" in user_data
    assert "professional_status" in user_data

async def test_db_rollback_if_invalid_input(async_client, token):
    # First update with valid data
    response = await async_client.put(
        "/profile",
        headers={"Authorization": f"Bearer {token}"},
        json={"bio": "Valid Bio", "location": "Valid Location"},
    )
    assert response.status_code == 200
    
    # Now try to update with invalid data
    long_bio = "x" * 501  # Exceeds the 500 character limit
    response = await async_client.put(
        "/profile",
        headers={"Authorization": f"Bearer {token}"},
        json={"bio": long_bio, "location": "New Location"},
    )
    assert response.status_code == 422
    
    # Verify the data wasn't changed
    response = await async_client.get(
        "/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["bio"] == "Valid Bio"
    assert user_data["location"] == "Valid Location"



async def test_admin_can_upgrade_user(async_client, admin_token, user):
    response = await async_client.put(
        "/admin/upgrade-user",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"user_id": str(user.id), "professional_status": True},
    )
    assert response.status_code == 200
    assert response.json()["professional_status"] is True


async def test_non_admin_cannot_upgrade_users(async_client, token, user):
    response = await async_client.put(
        "/admin/upgrade-user",
        headers={"Authorization": f"Bearer {token}"},
        json={"user_id": str(user.id), "professional_status": True},
    )
    assert response.status_code == 403  # Forbidden
