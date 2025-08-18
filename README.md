# Restaurant Management System (Django + Django REST Framework)

This is a Django-based backend system that manages restaurant operations, including user profiles, restaurant menus, orders (guest and registered), customer data, and a simple frontend interface using templates. It also includes a RESTful API for integrations or external frontend applications.

---

## Features

1. **User Profiles & Staff Login**
   * Staff login via email and password
   * User profile management with full name and phone number
   * Profile auto-created when a new user registers

2. **Restaurant & Menu Management**
   * CRUD operations for restaurants
   * CRUD operations for menu items linked to a restaurant
   * Simple hardcoded menu option for demo/testing

3. **Order System**
   * Guest and authenticated customer order support
   * Customer record auto-creation for guests
   * Many-to-many relation between orders and menu items
   * View orders by customer or logged-in user

4. **Frontend Templates (Basic)**
   * Homepage with styled menu display
   * About Us page
   * Contact Us page
   * Custom 404 page
   * Inline and external CSS support

5. **REST API (Django REST Framework)**
   * Modular APIs for account, products, and orders
   * Browsable API via DRF interface

---

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite (default database)
* HTML5, CSS3 (inline + static)
* Postman (API testing)

---

## Project Structure

```

restaurant_management_project/
│
├── account/             # Handles user login and profile
├── products/            # Restaurant and menu item models
├── orders/              # Orders and customer tracking
├── home/                # Frontend template pages
    |__ templates/           # Custom 404 and shared templates
├── manage.py
├── requirements.txt
└── README.md

````

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Praveen7-C/restaurant_management_project.git
   cd restaurant_management_project
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
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**

   ```bash
   python manage.py runserver
   ```

   Then visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## API Endpoints

Base URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

**Account**

* `POST /api/account/staff-login/`            (Login with email & password)
* `GET /api/account/me/profile/`              (View profile)
* `PUT /api/account/me/profile/`              (Update profile)

**Products**

* `GET/POST /api/products/restaurants/`       (List or create restaurants)
* `GET/PUT/DELETE /api/products/restaurants/<id>/`
* `GET/POST /api/products/menuitems/`         (List or create menu items)
* `GET/PUT/DELETE /api/products/menuitems/<id>/`

**Orders**

* `POST /api/orders/customers/`               (Create guest customer)
* `POST /api/orders/orders/create/`           (Place an order)
* `GET /api/orders/orders/?customer_id=1`     (List guest orders)
* `GET /api/orders/orders/`                   (List orders for logged-in user)

---

## Frontend Routes

* `/`                  → Homepage with menu
* `/about/`            → About Us page
* `/contact/`          → Contact Us page

---

## Admin Panel

* Visit: `/admin/`
* Login with the superuser created earlier
* Manage Users, Restaurants, Menu Items, Orders, and Customers

---

## Requirements

Example `requirements.txt`:

```
Django
djangorestframework
```

---

## License

This project is licensed under the MIT License.

