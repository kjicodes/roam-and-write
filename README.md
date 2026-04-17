# *Roam&Write*

<img src="static/images/site-screenshot.png" alt="Roam&Write" width="600"/>

Plan less, share more — a travel blog web application where users can document and share their travel experiences with readers and fellow adventurers.

## About

Roam&Write was built with the idea that every journey has a story worth sharing. Users can create an account, publish travel posts, browse stories from others, and engage through comments.

## Features

- **User authentication** — register, log in, and log out securely with hashed passwords
- **Email verification** — new accounts require email verification before logging in
- **Route protection** — custom `admin_or_owner` decorator enforces ownership and role checks; unauthenticated users are redirected to login with user-friendly flash messages
- **Create posts** — document a trip with a title, subtitle, destination, body, star rating, visit count, and an optional image
- **Edit & delete posts** — authors can update or remove their own posts; admins can delete any post
- **Comments** — authenticated users can leave comments on any post; only the comment author or an admin can delete the comment
- **Contact form** — visitors can send a message directly through the site 
- **About page** — overview of the platform and its purpose
- **Responsive design** — layout adapts across desktop, tablet, and mobile screen sizes

## Tech Stack

- **Backend:** Python, Flask, Flask-Login, Flask-Mail, Flask-WTF, SQLAlchemy, itsdangerous
- **Frontend:** HTML, CSS, Bootstrap, Bootstrap-Flask
- **Database:** SQLite (development) / PostgreSQL (production)
- **Deployment:** Heroku

## Getting Started

 Access the web application here:
 [Roam&Write](https://roam-and-write-aafc68872502.herokuapp.com/)    

## Running Locally

1. Clone the repository and create a virtual environment
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root

   ```
   SECRET_KEY=your-secret-key
   MAIL_SERVER=chosen-mail-server
   MAIL_USERNAME=your-username-or-email
   MAIL_PASSWORD=your-app-password
   ```

4. Run the development server
   ```bash
   python main.py
   ```

5. Visit `http://localhost:5001`

## Author

Developed by **[Kateleen Issa](https://www.linkedin.com/in/kjicodes)**
