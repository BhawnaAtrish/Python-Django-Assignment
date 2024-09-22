# Django My Shop

This Django project tracks customer spending and provides a method to retrieve the top 5 customers who have spent the most in the last 6 months.

## Features

- Records customer orders with details such as customer name, order date, status, and total amount.
- Retrieves the top 5 customers based on their spending in the last 6 months.

## Installation

1. Clone the repository:

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://localhost:8000/`.

## Usage

- Navigate to `/top-customers/` to view the top 5 customers who have spent the most in the last 6 months.

## Models

- **Order**: Represents customer orders with fields:
  - `customer` (CharField)
  - `order_date` (DateField)
  - `status` (CharField)
  - `total_amount` (DecimalField)

