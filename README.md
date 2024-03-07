## Flask Application Design for MBTI Dating App

### Problem Analysis
**MBTI Dating App:** A web application that facilitates dating based on Myers-Briggs Type Indicator (MBTI) personality types. The app allows users to create profiles, view potential matches based on their MBTI compatibility, and initiate conversations.

### HTML Files
- **index.html:** The main page of the app, containing the registration form and login form.
- **profile.html:** The profile page, displaying user information, MBTI type, and potential matches.
- **matches.html:** The page listing potential matches based on MBTI compatibility.
- **chat.html:** The chat window page, allowing users to communicate with their matches.

### Routes
- **Registration Route (registration.html):**
  - POST route to handle user registration, storing user data and MBTI type in the database.
- **Login Route (login.html):**
  - POST route to validate user credentials and allow login to the application.
- **Profile Route (profile.html):**
  - GET route to display the user's profile information, including MBTI type and potential matches.
- **Matches Route (matches.html):**
  - GET route to fetch and display potential matches for the user based on MBTI compatibility.
- **Chat Route (chat.html):**
  - GET route to open a chat window with a selected match.