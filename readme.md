## 🆕 User Profile Management Updates

This update introduces functionality for users to manage their profile information and for managers/admins to upgrade users to professional status.

---

### 🔧 New API Endpoints

#### 📄 `PUT /profile`
**Description**: Allows an authenticated user to update their profile information.

**Request Body Example**:

\`\`\`json
{
  "name": "Nathanielle Louis",
  "bio": "Software engineer passionate about clean architecture.",
  "location": "New Jersey"
}
\`\`\`

**Authentication**: ✅ Required (Bearer Token)

**Response**:

\`\`\`json
{
  "id": "uuid",
  "email": "user@example.com",
  "name": "Nathanielle Louis",
  "bio": "Software engineer passionate about clean architecture.",
  "location": "New Jersey",
  "is_professional": false
}
\`\`\`

---

#### 🧑‍💼 `PUT /admin/upgrade-user`
**Description**: Allows a Manager or Admin to upgrade a user’s account to "Professional" status.

**Request Body Example**:

\`\`\`json
{
  "user_id": "uuid-of-user",
  "professional_status": true
}
\`\`\`

**Authentication**: ✅ Required (Manager or Admin role)

**Response**:

\`\`\`json
{
  "id": "uuid",
  "email": "user@example.com",
  "name": "Nathanielle Louis",
  "is_professional": true
}
\`\`\`

---

### 📝 New User Profile Fields

| Field             | Type   | Description                                 |
|------------------|--------|---------------------------------------------|
| `bio`            | string | A short biography or about-me section       |
| `location`       | string | User's current city, state, or region       |
| `is_professional`| bool   | Indicates if the user is a verified professional |

---

### 🔒 Role-Based Access

| Endpoint                   | Role Required       |
|---------------------------|---------------------|
| `PUT /profile`            | Authenticated User  |
| `PUT /admin/upgrade-user` | Manager or Admin    |

---

### 🔍 Testing Locally

#### 🧪 Using Swagger (FastAPI Interactive Docs)

1. Start the app with Docker:

   \`\`\`bash
   docker compose up --build
   \`\`\`

2. Open your browser and visit:

   \`http://localhost/docs\`

3. Authenticate using the `/token` endpoint to get a JWT token.

4. Click the **Authorize** button and paste your token like:

   \`\`\`
   Bearer <your_token_here>
   \`\`\`

5. Test `/profile` and `/admin/upgrade-user` endpoints interactively.

---

#### 🧪 Using Postman

1. Make sure the server is running:

   \`\`\`
   http://localhost
   \`\`\`

2. Set request headers:

   \`\`\`
   Authorization: Bearer <your_token_here>
   Content-Type: application/json
   \`\`\`

3. **PUT** to `/profile`:

   \`\`\`json
   {
     "name": "Nathanielle Louis",
     "bio": "FastAPI developer.",
     "location": "NJ"
   }
   \`\`\`

4. **PUT** to `/admin/upgrade-user`:

   \`\`\`json
   {
     "user_id": "uuid",
     "professional_status": true
   }
   \`\`\`

---
