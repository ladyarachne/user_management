🆕 User Profile Management Updates
This update introduces new functionality for users to manage their profile information and for managers/admins to upgrade users to professional status.

🔧 New API Endpoints
📄 PUT /profile
Description: Allows an authenticated user to update their profile information.

Request Body Example:

json
Copy
Edit
{
  "name": "Nathanielle Louis",
  "bio": "Software engineer passionate about clean architecture.",
  "location": "New Jersey"
}
Authentication: ✅ Required (Bearer Token)

Response:

json
Copy
Edit
{
  "id": "uuid",
  "email": "user@example.com",
  "name": "Nathanielle Louis",
  "bio": "Software engineer passionate about clean architecture.",
  "location": "New Jersey",
  "is_professional": false
}
🧑‍💼 PUT /admin/upgrade-user
Description: Allows a Manager or Admin to upgrade a user’s account to "Professional" status.

Request Body Example:

json
Copy
Edit
{
  "user_id": "uuid-of-user",
  "professional_status": true
}
Authentication: ✅ Required (Manager or Admin role)

Response:

json
Copy
Edit
{
  "id": "uuid",
  "email": "user@example.com",
  "name": "Nathanielle Louis",
  "is_professional": true
}
📝 New User Profile Fields
Field	Type	Description
bio	string	A short biography or about-me section
location	string	User's current city, state, or region
is_professional	bool	Indicates if the user is a verified professional

🔒 Role-Based Access
Endpoint	Role Required
PUT /profile	Authenticated User
PUT /admin/upgrade-user	Manager or Admin

🔍 Testing Locally
🧪 Using Swagger (FastAPI Interactive Docs)
Start the app with Docker:

bash
Copy
Edit
docker compose up --build
Open your browser and go to:
http://localhost/docs

Authenticate via the /token endpoint to get a JWT token, then click Authorize at the top-right and paste the token as:

php-template
Copy
Edit
Bearer <your_token_here>
Use the /profile and /admin/upgrade-user endpoints to test updates interactively.

🧪 Using Postman
Make sure the server is running:
http://localhost

Set Headers:

http
Copy
Edit
Authorization: Bearer <your_token_here>
Content-Type: application/json
PUT request to /profile:

json
Copy
Edit
{
  "name": "Nathanielle Louis",
  "bio": "FastAPI developer.",
  "location": "NJ"
}
PUT request to /admin/upgrade-user:

json
Copy
Edit
{
  "user_id": "uuid",
  "professional_status": true
}

