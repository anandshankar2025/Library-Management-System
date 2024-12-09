# Library Management System

This is a simple **Library Management System** built with **Flask**, where an admin can log in to perform various operations like:

- Add Book
- View Books
- Search Books
- Add Member
- View Members
- Logout

## Features:
1. **Admin Login**: Admin can log in with a username and password.
2. **Add Book**: Admin can add a new book to the library collection.
3. **View Books**: Admin can view a list of all available books.
4. **Search Books**: Admin can search books by title or author.
5. **Add Member**: Admin can add a new member to the library.
6. **View Members**: Admin can view a list of all library members.
7. **Logout**: Admin can log out and return to the login page.

## Prerequisites

Before you begin, ensure you have the following:

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Flask**: A web framework for Python used to build this application.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/library-management-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd library-management-system
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Once the dependencies are installed, run the application:
   ```bash
   python app.py
   ```

2. Open a web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Log in with the admin credentials:
   - **Username**: admin
   - **Password**: password123

## Application Flow

1. The first page will prompt you to log in. Once logged in, you'll be redirected to the **home page** where you can:
   - Add Book
   - View Books
   - Search Books
   - Add Member
   - View Members
   - Logout

2. After performing any operation, you will be able to navigate back to the home page.

## Technologies Used

- **Python 3.x**
- **Flask**: Web framework for building the application
- **HTML/CSS**: For front-end templates
- **UUID**: For generating session tokens

## Future Enhancements

- Implement user authentication with more secure password management.
- Add database integration (e.g., SQLite or MySQL) for persistent storage of books and members.
- Improve the front-end design with CSS frameworks like Bootstrap.

## License

This project is open source and available under the MIT License.
