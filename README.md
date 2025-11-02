# Chronicles of History ⚔️

A modern Age of Empires IV inspired history blog web application where users can write, edit, and share articles about historical events.

## Features

- 🏰 **Medieval-themed UI** - Beautiful Age of Empires IV inspired design with parchment backgrounds and gold accents
- 📜 **Create Articles** - Write new historical chronicles with a user-friendly form
- ✏️ **Edit Articles** - Modify existing articles with full editing capabilities
- 🗑️ **Delete Articles** - Remove articles with confirmation
- 📚 **View Articles** - Browse all published chronicles in a card-based layout
- 📖 **Read Articles** - View full article details with formatted content
- 🎨 **Responsive Design** - Works on desktop, tablet, and mobile devices

## Technology Stack

- **Backend**: Flask 3.0.0 (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3 (Medieval/AoE4 inspired styling)
- **Security**: Werkzeug 3.0.3 (patched for security vulnerabilities)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kolaricfilip4-glitch/my_python_app.git
cd my_python_app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Set environment variables for security:
```bash
export SECRET_KEY="your-secret-key-here"
export FLASK_DEBUG="false"  # Set to "true" only for development
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Usage

### Creating a New Article
1. Click on "📜 Write New Article" in the navigation
2. Fill in the title, author name, and article content
3. Click "🏛️ Publish Chronicle" to publish

### Viewing Articles
- The homepage displays all articles in chronological order (newest first)
- Click "Read More" or the article title to view the full content

### Editing Articles
1. Open an article
2. Click "✏️ Edit" button
3. Make your changes
4. Click "💾 Save Changes"

### Deleting Articles
1. Open an article
2. Click "🗑️ Delete" button
3. Confirm the deletion

## Project Structure

```
my_python_app/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── history_blog.db        # SQLite database (created automatically)
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Homepage with article list
│   ├── article.html      # Article detail view
│   ├── new_article.html  # Create article form
│   └── edit_article.html # Edit article form
└── static/
    └── css/
        └── style.css      # AoE4-inspired styling

```

## Design Inspiration

The application is inspired by Age of Empires IV's aesthetic:
- Medieval color palette (browns, golds, parchment tones)
- Parchment-like content backgrounds
- Gold borders and accents
- Medieval-themed icons and emojis
- Warm, inviting atmosphere reminiscent of historical chronicles

## Database Schema

### Article Model
- `id`: Integer (Primary Key)
- `title`: String (max 200 characters)
- `author`: String (max 100 characters)
- `content`: Text
- `date_posted`: DateTime (auto-generated)

## License

This project is open source and available for educational purposes.
