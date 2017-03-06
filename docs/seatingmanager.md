# Seating Manager

Official documentation for AESSET - Seating Manger application.

#### 1. Create/List Student
* **Request URL:**

    `POST` `GET` `/seating/studentlist/`
    
* **Parameters:**

Parameter | Type | Required | Description
:------------: | :-------------: | :------------: | :------------: |
roll_no | Integer | ✓ | Roll number of the Student
system_id | Integer | ✓ | System Id of the Student
name | String | ✓ | Name of the Student
branch | String | ✓ | Branch of the Student
year | String | ✕ | Year of the student in which he is currently studying
semester | String | ✓ | Current semester of the student
subject | Student Object | ✓ | Subjects student is enrolled in

* **Logic:**

Create a student object using all the paramenters required ofr creating a student entry. ALso, it list all the students who have entry in the database.

* **Request:**

```javascript
{
    "roll_no": "130101128",
    "system_id": "2013012180",
    "name": "Punit",
    "branch": "CSE",
    "year": "4",
    "semester": "8",
    "subject": [
        "CSE421", 
        "CSE201"
    ]
}
```

* **Response:**

```javascript
[
  {
    "roll_no": 130101126,
    "system_id": 2013012150,
    "name": "Punit Grover",
    "branch": "CSE",
    "year": "4",
    "semester": "8",
    "subject": [
      "CSE321",
      "CSE401"
    ]
  },
  {
    "roll_no": 130101081,
    "system_id": 2013007016,
    "name": "Isha",
    "branch": "CSE",
    "year": "4",
    "semester": "8",
    "subject": [
      "CSE321",
      "CSE401",
      "CSE311"
    ]
  },
  {
    "roll_no": 130101111,
    "system_id": 2013012159,
    "name": "xyz",
    "branch": "CSE",
    "year": "4",
    "semester": "8",
    "subject": [
      "CSE401"
    ]
  }
]
```
