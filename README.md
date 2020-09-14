# Student Registration Portal

This is an open source project which lets you create student management system in fast, clean, scalable manner and can be used for different types of registrations in any environment.


## Setup Environment

 Open source projects used:

* [Python](https://www.python.org/) - god's language
* [Flask](https://palletsprojects.com/p/flask/) - awesome web-framework
* [Materialize CSS](https://materializecss.com/getting-started.html) - great UI boilerplate for modern web apps


## Installation

Requires [pyhton](https://www.python.org/downloads/) v3+ to run.

Install the dependencies and devDependencies and start the server.

```sh
pip install flask
pip install request
pip install pandas
python app.py
```

## Database
Currently using csv (flat file) database.

| **Field** | **Interface type** | **Data Type** | **Length** | **Remarks** |
| --- | --- | --- | --- | --- |
| Registration ID | - | integer | - | _system generated id._ |
| First Name | Text box | string | 20 | user input |
| Last Name | Text box | string | 20 | user input |
| Email | Text box | string | 20 | user input |
| Phone Number | Text box | integer | 10 | user input |
| Date of Birth | Date Picker | string | 10 | user input |
| Gender | Radio Button | string | 5 | user input |
| City | Text box | string | 20 | user input |
| State | Text box | string | 20 | user input |
| ZIP / Postal Code | Text box | integer | 6 | user input |
| **Masters**  **details** | Label | - | - | _for interface display only_ |
| University | Text box | string | 50 | user input |
| Field | Text box | string | 20 | user input |
| Year | Text box | integer | 4 | user input |


Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:5000
```

## Todos

 - Write MORE Tests

**Free Software, Hell Yeah!**
