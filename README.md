## HappyCart
 HappyCart is a Django-based application designed to manage customer orders. The application includes features such as customer management, order management, and SMS notifications for order confirmations using Africa's Talking API.

## Table of Contents
- [Features](#features)
- [Apis](#apis)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributions](#contributions)


## Features
- Manage customers and orders through a RESTful API.
- Send SMS notifications to customers upon order creation.
- Authentication and authorization using token-based authentication.
- Continuous integration setup using GitHub Actions.

## Apis
#### Documentation
You can visit the official Postman documentation here [Api-postman-documentation](https://documenter.getpostman.com/view/28088528/2sA3XY7e76).



## Requirements
- Python 3.9 or higher
- Django 3.2 or higher
- Django REST framework
- Africa's Talking API
- SQLite (default database)

## Installation
1. **Clone the repository:**
   ```bash 
   git clone https://github.com/HenrietteDaughtyOloo/Happy-Cart-Project.git
   cd Happy-Cart


## Create a virtual environment:
2. **Create venv:**
   ```bash
   python -m venv myenv
3. **Then activate it:**
   ```bash
   source myenv/bin/activate 
## On Windows, use:
3. **For windows:**
   ```bash
   myenv\Scripts\activate


## Install dependencies:
4. **Then requirements:**
   ```bash
   pip install -r requirements.txt

## Apply migrations:
5. **Migrations:**
   ```bash
   python manage.py migrate

## Run the development server:
6. **Runserver:**
   ```bash
   python manage.py runserver

## Usage
7. **Access API Endpoints:**
#### Remember to create appropriate authorization Headers to use the API
- List all customers: GET /api/customers/
- Retrieve a customer: GET /api/customers/<id>/
- List all orders: GET /api/orders/
- Retrieve an order: GET /api/orders/<id>/


## Authentication:
8. **token-based:**
- Use token-based authentication to access the endpoints. Include the token in the header:
   ```bash
   Authorization: Bearer your_access_token

## Contributions:
9. **To be a contributor:**
Fork the repository:
- Click the "Fork" button at the top right of this repository.

- Clone your fork:
   ```bash
   git clone https://github.com/HenrietteDaughtyOloo/Happy-Cart.git

- navigate to repository
   ```bash
   cd Happy-Cart
- Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name

- Make your changes and commit:
   ```bash
   git commit -am 'Add a feature'
- Push to the branch:
   ```bash
   git push origin feature/your-feature-name

- Create a Pull Request:
Go to the repository on GitHub and click the "New Pull Request" button.