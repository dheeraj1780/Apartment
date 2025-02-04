# Apartment Management System

This project is a web application built using Python and MySQL. It provides a layout of homes in an apartment complex, indicating whether a house is free or occupied. Users can choose an empty house, simulate payment, and manage their maintenance costs.

## Features

- **Home Layout Display**: View a graphical representation of all homes, indicating whether each is free or occupied.
- **Home Selection and Payment**: Users can select an available house and simulate payment for it.
- **Admin Dashboard**: An admin can assign maintenance costs to occupants.
- **Maintenance Cost Management**: Occupants can view and pay their maintenance costs through the application.

## Tech Stack

- **Backend**: Python
- **Database**: MySQL
- **Frontend**: HTML/CSS, Tkinter GUI

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/apartment.git
    cd apartment
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MySQL database:

    - Create a new MySQL database.
    - Update the database configuration in `config.py` with your MySQL credentials.
    - Run the migration script to create the necessary tables:

    ```bash
    flask db upgrade
    ```

5. Run the application:

    ```bash
    flask run
    ```

6. Open the application in your web browser at `http://127.0.0.1:5000`.

## Usage

### User Functionality

- **View Home Layout**: Users can see which homes are free or occupied.
- **Select and Pay for a Home**: Users can choose an empty home and make a payment.
- **View Maintenance Costs**: Users can view any assigned maintenance costs.
- **Pay Maintenance Costs**: Users can pay for their maintenance charges through the application.

### Admin Functionality

- **Assign Maintenance Costs**: Admins can set maintenance charges for occupants.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit and push your changes (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.
