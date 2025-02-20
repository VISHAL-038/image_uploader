# Image Uploader

## Overview
This is a Django-based image uploader web application that allows users to upload images with captions. The application features a light/dark mode toggle and displays uploaded images in a gallery.

## Features
- Upload images with captions
- Display uploaded images with timestamps
- Dark mode toggle functionality
- Built using Django, Pillow, and SQLite

## Technologies Used
- **Django** (Backend framework)
- **Pillow** (Image processing library)
- **SQLite** (Database)
- **Bootstrap** (Frontend styling)

## Installation & Setup
### Prerequisites
Ensure you have Python installed (recommended version: 3.8 or higher).

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/image-uploader.git
   cd image-uploader
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   Open your browser and go to `http://127.0.0.1:8000/`

## Folder Structure
```
imageuploader/
│── imageuploader/  # Django project settings
│── myapp/          # Django app
│   ├── migrations/  # Database migrations
│   ├── templates/   # HTML templates
│   │   ├── home.html
│   ├── models.py    # Database models
│   ├── views.py     # Backend logic
│   ├── forms.py     # Forms handling
│── media/          # Uploaded images storage
│── db.sqlite3       # SQLite database
│── manage.py       # Django management script
│── README.md       # Project documentation
│── requirements.txt # Dependencies
```

## Requirements
Below are the dependencies required for this project:
```txt
asgiref==3.8.1
Django==5.1.6
pillow==11.1.0
sqlparse==0.5.3
```

## Contributing
Feel free to fork the repository, make improvements, and submit a pull request!

## License
This project is licensed under the MIT License.