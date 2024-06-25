## HappyCart
 HappyCart is a Django-based application designed to manage customer orders. The application includes features such as customer management, order management, and SMS notifications for order confirmations using Africa's Talking API.

## Table of Contents
- [Features](#features)
- [Documentation] (#documentation)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributions](#contributions)


## Features
- Manage customers and orders through a RESTful API.
- Send SMS notifications to customers upon order creation.
- Authentication and authorization using token-based authentication.
- Continuous integration setup using GitHub Actions.

## Documentation
Link- `https://documenter.getpostman.com/view/28088528/2sA3XY7e76`


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
 `python -m venv myenv`
 ## Then activate it
 `source myenv/bin/activate`

 
## On Windows, use:
`myenv\Scripts\activate`


## Install dependencies:
 `pip install -r requirements.txt `

## Apply migrations:
 `python manage.py migrate `

## Run the development server:

 `python manage.py runserver `

## Usage
Access API Endpoints:

- List all customers: GET /api/customers/
- Retrieve a customer: GET /api/customers/<id>/
- List all orders: GET /api/orders/
- Retrieve an order: GET /api/orders/<id>/

### Authentication:
Use token-based authentication to access the endpoints. Include the token in the header:
 `Authorization: Bearer your_access_token `

## Contributions
Fork the repository:
- Click the "Fork" button at the top right of this repository.

- Clone your fork:

  `git clone https://github.com/HenrietteDaughtyOloo/Happy-Cart.git`
- navigate to repository
    `cd Happy-Cart`
- Create a new branch:

 `git checkout -b feature/your-feature-name `

- Make your changes and commit:

 `git commit -am 'Add some feature' `
- Push to the branch:

 `git push origin feature/your-feature-name `
- Create a Pull Request:
Go to the repository on GitHub and click the "New Pull Request" button.