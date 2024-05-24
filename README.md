# Toy Tetragraph Hash

## Overview

Toy Tetragraph Hash is a text transformation tool built using FastAPI for the backend and React for the frontend. The tool processes a user-inputted text, transforms it into a series of 4x4 matrices, and performs various operations on these matrices, ultimately providing a transformed text output.

## Features

- Clean and transform user input text
- Convert text into 4x4 matrices
- Apply transformations and calculate running totals
- Display the transformation steps and final result

## Project Structure

- `backend/`: Contains the FastAPI backend implementation.
- `frontend/`: Contains the React frontend implementation.

## Prerequisites

- Python 3.8 or higher
- Node.js and npm
- Git

## Setup

### Backend

1. **Navigate to the `backend/` directory:**
    ```sh
    cd backend
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the FastAPI server:**
    ```sh
    uvicorn app:app --reload
    ```

### Frontend

1. **Navigate to the `frontend/` directory:**
    ```sh
    cd frontend
    ```

2. **Install the dependencies:**
    ```sh
    npm install
    ```

3. **Run the React development server:**
    ```sh
    npm start
    ```

## Usage

1. **Open your browser and navigate to `http://localhost:3000`.**
2. **Enter the text you want to transform in the text area and submit.**
3. **The transformation steps and final result will be displayed on the page.**

## Development

### Backend

- The main logic is implemented in `main.py`.
- The API endpoints are defined in `app.py`.

### Frontend

- The main React component is `TextTransformation.js` in the `src/pages` directory.
- The CSS styles are defined in `src/App.css`.

## Contributing

1. **Fork the repository.**
2. **Create a new branch (`git checkout -b feature-branch`).**
3. **Commit your changes (`git commit -m 'Add some feature'`).**
4. **Push to the branch (`git push origin feature-branch`).**
5. **Create a new Pull Request.**


