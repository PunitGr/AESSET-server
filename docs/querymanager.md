# Query manager

Official documentation for AESSET -- Query manager application

#### 1. Request a Query

* **Request URL:**

    `POST` `/query/`
    

* **Parameters:**

Parameter | Type | Required | Description
:-----------: | :---------: | :---------: | :---------:
student | Integer | ✔ | System ID of the Student
query_type | Char | ✔ | Type of the query
email | Char | ✔ | email id of the student
phone | PhoneNumberField| ✔ | Package is used for taking PhoneNumber as a data type
created_at | DateTimeField | ✕ | Date and time the query was created
modified_at | DateTimeField |  ✕ | Date and time the query was modified after getting regenerated

* **Logic:**

It lets the user generate a query and also, an email will be sent to the user along with the token number that has been alotted with description of time it will take for resolvement of the query.

* **Request:**

```javascript
{
    "student": "2013007016",
    "email" : "isha1234@gmail.com",
    "phone": "+919818675018"
}
```

* **Response:**

```
Email has been sent.
```