###### Authentication and Permissions Documentation
#### 1. What is Authentication?
Authentication is the process of verifying a user's identity. In a web API, this means confirming that a request is coming from a known user.

In this project, i've implemented Token Authentication. This is a modern, stateless method where a user exchanges their username and password for a unique, random string called a token.  This token then acts as their digital key. For every subsequent request to a protected part of the API, the user includes this token in the request headers instead of their username and password. The API simply checks if the token is valid, which is a very secure and efficient way to handle authentication.

The endpoint for obtaining a token is located at:
http://127.0.0.1:8000/api-token-auth/

#### 2. What are Permissions?
Permissions control what an authenticated user is allowed to do. While authentication confirms who a user is, permissions determine what they can access or modify.

In this project, i've used both built-in DRF permissions and a custom one to define these rules. The permission classes are applied to the ViewSet classes.

#### 3. Permissions in the API
I've configured the API with the following rules:

BookViewSet:

Authentication: TokenAuthentication

Permissions: IsAuthenticated

Rule: This means that to perform any action (read, create, update, or delete) on a Book resource, a user must be authenticated with a valid token. Unauthenticated users cannot view or interact with this data.

AuthorViewSet:

Authentication: TokenAuthentication

Permissions: IsAdminUser

Rule: This sets a much stricter rule. To perform any action on an Author resource, a user must not only be authenticated with a valid token, but they must also be an admin user. This is a great way to protect sensitive data and restrict it to staff members.

4. How It All Works Together
A client (like a mobile app) sends a POST request with a username and password to the token endpoint (/api-token-auth/).

If the credentials are correct, the API returns a unique token to the client.

For subsequent requests to a protected endpoint (e.g., /api/books_all/), the client sends a GET request and includes the token in the Authorization header.

Django REST Framework's TokenAuthentication checks if the token is valid.

If the token is valid, the request proceeds, and the permission_classes on the BookViewSet (IsAuthenticated) check if the user is allowed to perform the requested action.

The request is then processed, and the user gets the correct data or is allowed to perform the action. If any of these steps fail, the API returns an appropriate error (401 Unauthorized or 403 Forbidden).
