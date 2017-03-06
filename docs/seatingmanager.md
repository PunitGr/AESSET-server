# Seating Manager

Official documentation for AESSET - Seating Manger application.

#### 1. Create Student
* **Request URL:**

    `POST` `/seating/studentlist/`
    
* **Parameters:**

Parameter | Type | Required | Description
:------------: | :-------------: | :------------: | :------------: |
roll_no (pk) | Integer | ✓ | Roll number of the Student
system_id | Integer | ✓ | System Id of the Student
name | String | ✓ | Name of the Student
branch | String | ✓ | Branch of the Student
year | String | ✕ | Year of the student in which he is currently studying
semester | String | ✓ | Current semester of the student
subject | Student Object | ✓ | Subjects student is enrolled in

* **Logic:**

	Create a student entry using all the parameters required for creating a student entry. Also, it list all the students who exists in the database.

* **Request:**

```javascript
{
  "roll_no": "130101128",
  "system_id": "2013012180",
  "name": "Punit",
  "branch": "CSE",
  "semester": "8",
  "subject": [
      "CSE421", 
      "CSE201"
  ]
}
```

* **Response:**


```javascript
{
  "roll_no": "130101128",
  "system_id": "2013012180",
  "name": "Punit",
  "branch": "CSE",
  "year": "",
  "semester": "8",
  "subject": [
      "CSE421", 
      "CSE201"
  ]
}
```

</br>

#### 2. List Students
* **Request URL:**

    `GET` `/seating/studentlist/`

* **Logic:**

	List all the student entries who exists in the database.

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

</br>


#### 3. Create Subjects
* **Request URL:**

    `POST`  `/seating/subjectlist/`
    
* **Parameters:**

Parameter | Type | Required | Description
:------------: | :-------------: | :------------: | :------------: |
subject_id | String | ✓ | Subject code
subject_name | String | ✕ | Subject name
department | String | ✕ | Department under which the subject comes
paper_code | String | ✓ | Paper code of the subject (unique)

* **Logic:**

	Create a subject entry using all the parameters required for creating a subject entry. Also, list all the subjects and the student enrolled in them.

* **Request:**

```javascript
{
  "subject_id": "CS150",
  "subject_name": "DAA",
  "paper_code": "1234"
}
```

* **Response:**

```javascript
{
  "subject_id": "CS150",
  "subject_name": "DAA",
  "department": "CSE",
  "paper_code": "12334",
  "students": []
}
```

</br>


#### 4. List Subjects
* **Request URL:**

    `GET`  `/seating/subjectlist/`
    
* **Logic:**

	List all the subjects and the student enrolled in them.

* **Response:**

```javascript
[
  {
    "subject_id": "CSE321",
    "subject_name": "Java",
    "department": "CSE",
    "paper_code": "20134",
    "students": [
      {
        "roll_no": 130101126,
        "system_id": 2013012150,
        "branch": "CSE",
        "year": "4"
      },
      {
        "roll_no": 130101081,
        "system_id": 2013007016,
        "branch": "CSE",
        "year": "4"
      }
    ]
  },
  {
    "subject_id": "CSE401",
    "subject_name": "Artificial Intelligence",
    "department": "CSE",
    "paper_code": "32454",
    "students": [
      {
        "roll_no": 130101126,
        "system_id": 2013012150,
        "branch": "CSE",
        "year": "4"
      },
      {
        "roll_no": 130101081,
        "system_id": 2013007016,
        "branch": "CSE",
        "year": "4"
      },
      {
        "roll_no": 130101111,
        "system_id": 2013012159,
        "branch": "CSE",
        "year": "4"
      }
    ]
  },
  {
    "subject_id": "CSE311",
    "subject_name": "Advanced Java",
    "department": "CSE",
    "paper_code": "20934",
    "students": [
      {
        "roll_no": 130101081,
        "system_id": 2013007016,
        "branch": "CSE",
        "year": "4"
      }
    ]
  },
  {
    "subject_id": "CS321",
    "subject_name": "Jaa",
    "department": "CSE",
    "paper_code": "2034",
    "students": []
  },
  {
    "subject_id": "CS150",
    "subject_name": "DAA",
    "department": "CSE",
    "paper_code": "1234",
    "students": []
  }
]
```

</br>

#### 5. List Datesheet
* **Request URL:**

    `GET` `/seating/datesheet/`
    
* **Logic:**

	List the datesheet with student enrolled in that subject.


* **Response:**


```javascript
[
  {
    "subject_id": "CSE321",
    "students": [
      {
        "roll_no": 130101126
      },
      {
        "roll_no": 130101081
      }
    ],
    "exam": [
      {
        "id": 6,
        "exam_date": "2017-03-28"
      }
    ]
  },
  {
    "subject_id": "CSE401",
    "students": [
      {
        "roll_no": 130101126
      },
      {
        "roll_no": 130101081
      },
      {
        "roll_no": 130101111
      }
    ],
    "exam": [
      {
        "id": 5,
        "exam_date": "2017-03-14"
      }
    ]
  },
  {
    "subject_id": "CSE311",
    "students": [
      {
        "roll_no": 130101081
      }
    ],
    "exam": []
  },
  {
    "subject_id": "CS321",
    "students": [],
    "exam": [
      {
        "id": 5,
        "exam_date": "2017-03-14"
      }
    ]
  },
  {
    "subject_id": "CS150",
    "students": [],
    "exam": [
      {
        "id": 6,
        "exam_date": "2017-03-28"
      }
    ]
  },
  {
    "subject_id": "CS50",
    "students": [],
    "exam": [
      {
        "id": 4,
        "exam_date": "2017-03-06"
      }
    ]
  }
]
```

</br>

</br>

#### 6. Create room entry
* **Request URL:**

    `POST` `/seating/roomlist/`
    
* **Parameters:**

Parameter | Type | Required | Description
:------------: | :-------------: | :------------: | :------------: |
room_number | Integer | ✓ | Room number
room_type | ChoiceField | ✕ | Room type i.e Audi/Classroom
capacity | Integer | ✓ | Capacity if classroom
block_number | Integer | ✓ | Block number where the room is.
building_name | String | ✓ | Name of the building


* **Logic:**

	Create a room entry using all the parameters required for creating a room entry.

* **Request:**

```javascript
{
  "room_number": "301",
  "block_number": "1",
  "building_name": "SET"
}
```

* **Response:**

```javascript
{
  "id": 2,
  "room_number": 301,
  "room_type": "Classroom",
  "capacity": 64,
  "block_number": 1,
  "building_name": "SET"
}
```

</br>

#### 6. List room details

* **Request URL:**

    `GET` `/seating/roomlist/`
    
* **Logic:**

	List all the room entries.

* **Response:**

```javascript
[
  {
    "id": 1,
    "room_number": 201,
    "room_type": "Classroom",
    "capacity": 64,
    "block_number": 1,
    "building_name": "SET-1"
  },
  {
    "id": 2,
    "room_number": 301,
    "room_type": "Classroom",
    "capacity": 64,
    "block_number": 1,
    "building_name": "SET"
  }
]
```

</br>



