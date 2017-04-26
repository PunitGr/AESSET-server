# Query manager API Endpoints

Official documentation for AESSET -- Query manager application

#### 1. Request a Query

* **Request URL:**

    `POST` `/query/`
    

* **Parameters:**

Parameter | Type | Required | Description
:-----------: | :---------: | :---------: | :---------:
student | Integer | ✓ | System ID of the Student
query_type | Char | ✕ | Type of the query
email | Char | ✓ | email id of the student
phone | PhoneNumberField| ✓ | Package is used for taking PhoneNumber as a data type
date | DateField | ✓ | Appointment date
time | Char | ✓ | Appointment time slot
status | Boolean |  ✕ | status to check if query has been resolved or not
token_id | Char | ✕ | token of the appointment
slot | Foreign Key | ✕ | Mapped with TimeSlot Table

* **Logic:**

It lets the user select a date and time slot for query resolvement. An email will be sent to the user along with the token number that has been alotted with description of time it will take for resolvement of the query.

* **Request:**

```javascript
{
    "student": "2010122150",
    "email": "groov9@gmail.com",
    "phone": "+919900138142",
    "date": "2017-2-6",
    "time": "10:00"
}
```

* **Response:**

```
{
  "status": "success",
  "data": {
    "id": 30,
    "student": 2010122150,
    "query_type": "Exam",
    "email": "groov9@gmail.com",
    "phone": "+919900138142",
    "date": "2017-02-06",
    "time": "10:00",
    "status": false,
    "token_id": "SU1700011",
    "slot": "1000-2017-02-06"
  }
}
```
</br>

#### 2. List Queries
* **Request URL:**

	`GET` `/querylist/`
	
* **Request URL Parameters and Logic:**

Request | Description 
:-----------: | ---------
`/querylist?status=0&date=2017-09-07`| It returns all the queriess requested on `2017-09-07` and whose status is unresolved.
`/querylist?status=1`| It returns all the queries whose status is resolved.
`/querylist?date=2017-09-07` | It returns all the queries which were requested on `2017-09-07`.
`/querylist/` | List all the queries.

* **Response:**

```javascript
[
  {
    "id": 20,
    "student": 2010012150,
    "query_type": "Exam",
    "email": "groo9@gmail.com",
    "phone": "+919801138142",
    "date": "2017-08-17",
    "time": "10:00",
    "status": false,
    "token_id": "SU1700001",
    "slot": "1000-2017-08-17"
  },
  {
    "id": 21,
    "student": 2010012150,
    "query_type": "Exam",
    "email": "groo9@gmail.com",
    "phone": "+919801138142",
    "date": "2017-08-07",
    "time": "10:00",
    "status": false,
    "token_id": "SU1700002",
    "slot": "1000-2017-08-07"
  },
  {
    "id": 22,
    "student": 2010012150,
    "query_type": "Exam",
    "email": "groo9@gmail.com",
    "phone": "+919801138142",
    "date": "2017-08-07",
    "time": "10:00",
    "status": false,
    "token_id": "SU1700003",
    "slot": "1000-2017-08-07"
  },
  {
    "id": 23,
    "student": 2010012150,
    "query_type": "Exam",
    "email": "groo9@gmail.com",
    "phone": "+919801138142",
    "date": "2017-08-07",
    "time": "10:00",
    "status": false,
    "token_id": "SU1700004",
    "slot": "1000-2017-08-07"
  },
  {
    "id": 24,
    "student": 2010012150,
    "query_type": "Exam",
    "email": "groo9@gmail.com",
    "phone": "+919801138142",
    "date": "2017-08-07",
    "time": "10:00",
    "status": false,
    "token_id": "SU1700005",
    "slot": "1000-2017-08-07"
  },
  {
    "id": 25,
    "student": 2010012150,
    "query_type": "Exam",
    "email": "groo9@gmail.com",
    "phone": "+919801138142",
    "date": "2017-08-06",
    "time": "10:00",
    "status": false,
    "token_id": "SU1700006",
    "slot": "1000-2017-08-06"
  },
  {
    "id": 26,
    "student": 2010012150,
    "query_type": "Exam",
    "email": "groo9@gmail.com",
    "phone": "+919801138142",
    "date": "2017-08-06",
    "time": "10:00",
    "status": false,
    "token_id": "SU1700007",
    "slot": "1000-2017-08-06"
  },
  {
    "id": 27,
    "student": 2010012150,
    "query_type": "Exam",
    "email": "groo9@gmail.com",
    "phone": "+919801138142",
    "date": "2017-08-06",
    "time": "10:00",
    "status": false,
    "token_id": "SU1700008",
    "slot": "1000-2017-08-06"
  },
  {
    "id": 28,
    "student": 2010012150,
    "query_type": "Exam",
    "email": "groo9@gmail.com",
    "phone": "+919801138142",
    "date": "2017-08-06",
    "time": "10:00",
    "status": false,
    "token_id": "SU1700009",
    "slot": "1000-2017-08-06"
  },
  {
    "id": 29,
    "student": 2010012150,
    "query_type": "Exam",
    "email": "groo9@gmail.com",
    "phone": "+919801138142",
    "date": "2017-02-06",
    "time": "10:00",
    "status": false,
    "token_id": "SU1700010",
    "slot": "1000-2017-02-06"
  },
  {
    "id": 30,
    "student": 2010012150,
    "query_type": "Exam",
    "email": "groo9@gmail.com",
    "phone": "+919801138142",
    "date": "2017-02-06",
    "time": "10:00",
    "status": false,
    "token_id": "SU1700011",
    "slot": "1000-2017-02-06"
  }
]
```