# *Roam&Write*

<img src="static/images/site-screenshot.png" alt="Roam&Write" width="600"/>

Plan less, share more — a travel blog web application where users can document and share their travel experiences with readers and fellow adventurers.

## About

Roam&Write was built with the idea that every journey has a story worth sharing. Users can create an account, publish travel posts, browse stories from others, and engage through comments.

## Features

- **User authentication** — register, log in, and log out securely with hashed passwords
- **Create posts** — document a trip with a title, subtitle, destination, body, star rating, visit count, and an optional image
- **Edit & delete posts** — authors can update or remove their own posts
- **Comments** — authenticated users can leave comments on any post; comment authors can delete their own comments
- **Contact form** — visitors can send a message directly through the site
- **About page** — overview of the platform and its purpose
- **Responsive design** — layout adapts across desktop, tablet, and mobile screen sizes

## Tech Stack

- **Backend:** Python, Flask, Flask-Login, Flask-WTF, SQLAlchemy
- **Frontend:** Jinja2, Bootstrap 5, Bootstrap-Flask
- **Database:** SQLite
- **Security:** Werkzeug password hashing (PBKDF2)

## Getting Started

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   python main.py
   ```
4. Open your browser and navigate to `http://localhost:5001`

## Pages

| Page | Route | Description |
|------|-------|-------------|
| Home | `/` | Browse all travel posts |
| Post | `/post/<id>` | Read a post and leave a comment |
| Add Post | `/add-post` | Create a new travel post (login required) |
| Edit Post | `/edit-post/<id>` | Edit an existing post (login required) |
| Register | `/register` | Create a new account |
| Login | `/login` | Log in to your account |
| About | `/about` | Learn about Roam&Write |
| Contact | `/contact` | Send a message |

## Author

Developed by **[Kateleen Issa](https://www.linkedin.com/in/kjicodes)**