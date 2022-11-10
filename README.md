# Book Store API Web Application Project

## Index  
- [R1 - Identification of the problem you are trying to solve by building this particular app](#r1---identification-of-the-problem-you-are-trying-to-solve-by-building-this-particular-app)  
- [R2 - Why is it a problem that needs solving](#r2-–-why-is-it-a-problem-that-needs-solving)  
- [R3 - Why have you chosen this database system. What are the drawbacks compared to others?](#r3---why-have-you-chosen-this-database-system-what-are-the-drawbacks-compared-to-others)  
- [R4 - Identify and discuss the key functionalities and benefits of an ORM](#r4---identify-and-discuss-the-key-functionalities-and-benefits-of-an-orm)  
- [R5 - Document all endpoints for the API](#r5---document-all-endpoints-for-the-api)  
  - [Authorisation Endpoints](#authorisation) 
  - [Authors Endpoints](#authors) 
  - [Books Endpoints](#books) 
  - [Categories Endpoints](#categories) 
  - [Comments Endpoints](#comments) 
  - [Users Endpoints](#users) 
- [R6 - Make an ERD for the app](#r6---make-an-erd-for-the-app)  
- [R8 - Discuss the database relations to be implemented in your application](#r8---discuss-the-database-relations-to-be-implemented-in-your-application)  
- [R10 - Describe the way tasks are allocated and tracked in your project](#r10---describe-the-way-tasks-are-allocated-and-tracked-in-your-project)

## R1 - Identification of the problem you are trying to solve by building this particular app.

A book store requires a inventory system that will allow employees to easily find books within the stores inventory, using several methods to find the correct book for a customer. The employees will be able to search for a books availability by simply searching for it’s title, but they will also be able to look up any available books by using other criteria such as author or style (crime, fantasy, romance, etc..). Having these extra search methods will allow employees to suggest appropriate books to customers based on their interests. An internal review system, by way of comments assigned to books, will allow employees to gain a quick understanding of a book so they can explain a title to a customer, without having read the book, as it would be nearly impossible to read all of the books in the store. The internal review system is based off similar systems like tasting notes in a wine store or product reviews in an appliance store. The inventory system will assign employees logins and passwords that will have certain privileges associated, such as creating a new book entry, and adding new reviews. Managers will get administrator credentials that will give them more extensive privileges such as deleting book entries and reviews, as well as altering the inventory numbers, along with the same privileges that the employees have. All inventory users will be able to use all the search functions. 

## R2 – Why is it a problem that needs solving?

The inventory system is needed to help employees save time when serving customers in many different ways. Employees will be able to quickly find specific books when customers inquire if it is in stock, and if it is not in stock, they will be able to quickly recommend similar books to the customer, based on other titles by the same author, or similar books in the same style. Employees will also be able to give customers a quick overview of a book from the internal review system. This will not only reduce the work load on the employees, it will also add to the customer experience, without needing the employee to read and memorise all of the titles within the store. Managers tasks will be made easier as they will be able to check inventory levels along with being able to disseminating talking points throughout the staff that they would like to emphasise on certain titles to increase sales using the review system.  

An API may seem like overkill for a book store's internal inventory system, but having access from anywhere is essential with todays hybrid working environments. If a manager is checking inventory while ordering new titles, they can now do it from their home office. This is only one of the many examples that could crop up that having a web based inventory can solve.  

## R3 -  Why have you chosen this database system. What are the drawbacks compared to others?

I have chosen to use PostgreSQL as my database system for several reason which I will go into. To begin with, PostgreSQL an advanced, fully open sourced SQL database system, unlike Oracle, SQL Server and even MySQL which have fee which can get very expensive. Though MySQL is still technically an open sourced database system, they were partially bought by Oracle and since then certain features and services have been hidden away behind a paywall. MySQL it is still a very capable database system in it’s free, open sourced version, it is not quite as ‘free’ as PostgreSQL depending on your circumstance. Oracle can get very expensive if you decide to really scale up, as Amazon found out when they started to grow into one of the worlds largest companies. The cost had become so high that Amazon eventually switched their systems over to PostgreSQL. Some other tech giants that utilise PostgreSQL are Apple and Cisco, and I can imagine the cost might have a big part to play in their decisions. 

PostgreSQL will work on pretty much any machine or operating system, while systems like SQL Server will only run on Microsoft or Linux software. PostgreSQL mainly relies on it’s community for support as it is an open source software system, but this is not an issue as it has been around for over 20 years and the community is very large and active. PostgreSQL scales easily and is highly customisable as it has access to a near endless amount of plugin libraries, such as psycopg2 for python, which we will be using for our web application. 

From a more technical view, PostgreSQL uses Multiversion Concurrency Control (MVCC) which allows parallelisation so your queries can use multiple cores on the machine that is hosting your database, increasing power and speeding up query time. MySQL as PostgreSQL’s main open source competitor does not have this. PostgreSQL is able to use almost any data type and any index which gives it a huge amount of flexibility. Postgresql is more SQL complainant than MySQL, so in a strange turn of events if you ever wanted to take your project into a closed source environment like Oracle, PostgreSQL would make the transition better than MySQL, which is partially owned by Oracle. Lastly, PostgreSQL is very popular for web applications exactly like what we intend to make in this project, so it is perfect for us. 

## R4 - Identify and discuss the key functionalities and benefits of an ORM

An ORM (Object Relational Mapping) tool is used to map relational databases to objects in you preferred object-oriented programming language. There are many ORMs for many programming languages but the core functionalities are all basically the same. The main function of an ORM is that it abstracts SQL into objects of the language you are working in. This allows us to use objects from a certain language instead of needing to rely on direct SQL query statements. An ORM will all so parse the results that are returned from the query and give them back to us. This helps to improves readability, as direct SQL can be very dense and hard to decipher. This can also help reduce errors and speeds up production as it reduces the amount of code you have to work with. This will usually mean decreased costs associated with the development of an application. 

ORMs can make accessing data much easier. They map out how certain objects will relate to different tables within your database, then use these relationships to create SQL queries such as the basic CRUD operations, Create (or Insert), Read, Update and Delete. These terms may differ between languages and databases, but they all perform the same basic tasks needed to use your database. Of course an ORM tool will allow for much, much more complex SQL queries, but will still keep them fairly concise and readable for the development team. 

Another very important and welcome feature of an ORM is that it increases your databases security, reducing the possibility of SQL injection threats. This is because of the layer of abstraction an ORM gives a database, forcing outside queries through the ORM before it can make it to the database itself. Of course, this is not perfect and ORM injection can happen. 

Some issues with ORMs are that it can slow down the execution of queries compared to using SQL directly, as the ORM will usually produce a lot of it’s own code along side the minimum SQL needed. Another issue is ORMs themselves must be learned and implemented, which can be difficult and time consuming. The latter argument is usually overshadowed by the overall increase in productivity once an ORM is learned and implemented, and the former will depend on the projects needs and there are cases where this will be negligible or even non existent. Finally, a last issue that can effect a project is an ORM can be limiting, and you may need to resort to using direct SQL at some point. Many ORMs offer this feature though, but not all.  

---

## R5 - Document all endpoints for the API

---

## **AUTHORISATION**

---

## */auth/login*

### Description
- Login with email and password to recieve a bearer token with a 24 hour expiry time
- This end point will return the comment body and comment ID, and nested attributes from the book (title), including nested attributes from the book's author (first name and last name), and user associated with the comment (Id, first name and last name)

### Authorisation and Authentication: 
 - Authentication not needed 
 - Authorisation as admin not needed
 - Bearer token issued upon login with a 24 hour expiry time

### METHOD
 - POST

### EXAMPLE
 - /auth/login

### ARGUMENTS
 - None

### REQUIRED DATA
 - Email address - (user.email, String)
 - Password - (user.password, String)

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE 

```py
{
    "email":"steve@email.com",
    "password":"12345Aa!"
}
```
  
### RESPONSE BODY EXAMPLE 

```py
{
    "email": "steve@email.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2Nzk0NjE0MywianRpIjoiMmU2MjM4ZmEtZTk1Mi00NTNlLTgwYTItNTFjMjRkYTBiNGQ0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE2Njc5NDYxNDMsImV4cCI6MTY2ODAzMjU0M30.1C7qQ0hZX4lc7a81Cl60Qy8GI8tZUU-tP4cRRc4h2KE",
    "is_admin": true
}
```

### RETURN STATUS
- 200 OK

---

## */auth/register*

### Description
- Admin user can register a new user with their email, password, first name, last name and admin status. 
- This endpoint will return the new users id, first name, last name, email and their admin status. 

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin required through JWT Bearer Token

### METHOD
 - POST

### EXAMPLE
 - /auth/register

### ARGUMENTS
 - None
  
### REQUIRED DATA
 - First name (user.first_name, String)
 - Email address - (user.email, String)
 - Password - (user.password, String)

### OPTIONAL DATA
 - Last name (user.last_name, String)
 - Is Admin True/ False (user.is_admin, Boolean, default=False)

### REQUEST BODY EXAMPLE 

```py
{
    "email" : "test@test.com",
    "password" : "123456!Aa",
    "first_name" : "Test",
    "last_name" : "Tester"
}
```
  
### RESPONSE BODY EXAMPLE 

```py
{
    "id": 6,
    "first_name": "Test",
    "last_name": "Tester",
    "email": "test@test.com",
    "is_admin": false
}
```

### RETURN STATUS
- 201 CREATED

---

## **AUTHORS**

---

## */author*

### Description
- Return a list of all authors in the database.
- This end point will return every author's information including the id, first name, last name, about, accolades and a nested list including any books they have written that are also in the database. The books nested list included the attributes title, inventory numbers and book id.
  
### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not needed

### METHOD
 - GET

### EXAMPLE
 - /author

### ARGUMENTS
 - None

### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE 
 - None
  
### RESPONSE BODY EXAMPLE 

```py
[
    {
        "id": 1,
        "first_name": "Patrick",
        "last_name": "Rothfuss",
        "about": "Patrick James Rothfuss is an American author.",
        "accolades": "Patrick has won several awards.",
        "books": [
            {
                "title": "The Name of the Wind",
                "in_store": 0,
                "id": 1
            },
            {
                "title": "The Wise Man's Fear",
                "in_store": 2,
                "id": 2
            }
        ]
    },
    {
        "id": 2,
        "first_name": "Brandon",
        "last_name": "Sanderson",
        "about": "Brandon Sanderson is an American author of epic fantasy and science fiction.",
        "accolades": "Sanderson has been nominated for and also won multiple awards.",
        "books": [
            {
                "title": "The Way of Kings",
                "in_store": 4,
                "id": 3
            }
        ]
    },
```

### RETURN STATUS
- 200 OK

---

## */author/\<int:id\>*

### Description
- Return an authors in the database by ID.
- This end point will return an author's information including the id, first name, last name, about, accolades and a nested list including any books they have written that are also in the database. The books nested list included the attributes title, inventory numbers and book id.
  
### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not needed

### METHOD
 - GET

### EXAMPLE
 - /author/1

### ARGUMENTS
 - id (author.id, Integer)

### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE 
 - None
  
### RESPONSE BODY EXAMPLE 

```py
{
    "id": 1,
    "first_name": "Patrick",
    "last_name": "Rothfuss",
    "about": "Patrick James Rothfuss is an American author.",
    "accolades": "Patrick has won several awards.",
    "books": [
        {
            "title": "The Name of the Wind",
            "in_store": 0,
            "id": 1
        },
        {
            "title": "The Wise Man's Fear",
            "in_store": 2,
            "id": 2
        }
    ]
},
```

### RETURN STATUS
- 200 OK

---

## */author/first_name*

### Description
- Return a list of authors in the database by their first name.
- This end point will return any author's information that have the same first name that was queried. Returned information includes the id, first name, last name, about, accolades and a nested list including any books they have written that are also in the database. The books nested list included the attributes title, inventory numbers and book id.
  
### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not needed

### METHOD
 - GET

### EXAMPLE
 - /author/first_name/Patrick

### ARGUMENTS
 - First name (author.first_name, String)

### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE 
 - None
  
### RESPONSE BODY EXAMPLE 

```py
[
    {
        "id": 1,
        "first_name": "Patrick",
        "last_name": "Rothfuss",
        "about": "Patrick James Rothfuss is an American author.",
        "accolades": "Patrick has won several awards.",
        "books": [
            {
                "title": "The Name of the Wind",
                "in_store": 0,
                "id": 1
            },
            {
                "title": "The Wise Man's Fear",
                "in_store": 2,
                "id": 2
            }
        ]
    }
]
```

### RETURN STATUS
- 200 OK

---

## */author/last_name*

### Description
- Return a list of authors in the database by their last name.
- This end point will return any author's information that have the same last name that was queried. Returned information includes the id, first name, last name, about, accolades and a nested list including any books they have written that are also in the database. The books nested list included the attributes title, inventory numbers and book id.
  
### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not needed

### METHOD
 - GET

### EXAMPLE
 - /author/last_name/Seuss

### ARGUMENTS
 - Last name (author.last_name, String)

### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE 
 - None
  
### RESPONSE BODY EXAMPLE 

```py
[
    {
        "id": 3,
        "first_name": "Dr",
        "last_name": "Seuss",
        "about": "Theodor Seuss Geisel was an American children's author and cartoonist.",
        "accolades": "His work includes many of the most popular children's books of all time.",
        "books": [
            {
                "title": "Cat in the Hat",
                "in_store": 5,
                "id": 6
            }
        ]
    }
]
```

### RETURN STATUS
- 200 OK

---

## */author*

### Description
- Create a new author resource in your database.
- This end point will create a new author entity using the required fields, first name and last name, and can include the optional fields of about and accolades. Returned information includes the new author's id, first name, last name, about, accolades fields. A nested list including any books they have written that are also in the database. The books nested list included the attributes title, inventory numbers and book id. This will be empty on author creation as books require an author ID to be created, so need to be created after the books author is already in the database.  
  
### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token
 - Authorisation as admin required through JWT Bearer Token  

### METHOD
 - POST

### EXAMPLE
 - /author

### ARGUMENTS
 - None

### REQUIRED DATA
 - First name (author.first_name, String)
 - Last name (author.last_name, String)

### OPTIONAL DATA
 - About (author.about, Text)
 - Accolades (author.accolades, Text)

### REQUEST BODY EXAMPLE 

```py
{
    "first_name": "Test",
    "last_name": "Tester",
    "about": "Test author",
    "accolades": "Test Author of 2022"
}
```
  
### RESPONSE BODY EXAMPLE 

```py
{
    "id": 7,
    "first_name": "Test",
    "last_name": "Tester",
    "about": "Test author",
    "accolades": "Test Author of 2022",
    "books": []
}
```

### RETURN STATUS
- 201 CREATED

---

## */author/\<int:id\>*

### Description
- Update an author resource in your database.
- This end point will update an existing author entity using any of the fields, first name, last name, about and accolades. Returned information includes the updated author's id, first name, last name, about, accolades fields. A nested list including any books they have written that are also in the database. The books nested list included the attributes title, inventory numbers and book id.  
  
### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token
 - Authorisation as admin required through JWT Bearer Token  

### METHOD
 - POST, PATCH

### EXAMPLE
 - /author/7

### ARGUMENTS
 - id (author.id, Integer)

### REQUIRED DATA
 - None

### OPTIONAL DATA
 - First name (author.first_name, String)
 - Last name (author.last_name, String)
 - About (author.about, Text)
 - Accolades (author.accolades, Text)

### REQUEST BODY EXAMPLE 

```py
{
    "last_name": "Newer"
}
```
  
### RESPONSE BODY EXAMPLE 

```py
{
    "id": 7,
    "first_name": "Test",
    "last_name": "Newer",
    "about": "Test author",
    "accolades": "Test Author of 2022",
    "books": []
}
```

### RETURN STATUS
- 200 OK

---

## */author/\<int:id\>*

### Description
- Delete an author resource in your database, inlcuding all of their books.
- This end point will delete an existing author entity, including any books they have written that are linked by the Author ID, as book entities require an Author ID. Returned information is a response message informing successful deletion.  
  
### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token
 - Authorisation as admin required through JWT Bearer Token  

### METHOD
 - DELETE

### EXAMPLE
 - /author/7

### ARGUMENTS
 - id (author.id, Integer)

### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE 
 - None

### RESPONSE BODY EXAMPLE 

```py
{
    "message": "Author 'Test Newer' deleted successfully"
}
```

### RETURN STATUS
- 200 OK

---

## **BOOKS**

---

## */books*

### Description
- Return a list of all the book entities in the database. 
- This endpoint will return every book entity with the book ID, title, a nested list of attributes of the author with the author ID, author first name and author last name, a nested attribute of the category with the category ID and category name. It will show if the book is fiction or not and the in store inventory number. Lastly, it will return a nested list of attributes of any comments made about the book, including the attributes comment ID, comment body, and a further nested attribute of the user that made the comment with the users ID, user first_name and user Last_name.  
 
### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - GET

### EXAMPLE
 - /books

### ARGUMENTS
 - None
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None
  
### RESPONSE BODY EXAMPLE 

```py
[
    {
        "id": 1,
        "title": "The Name of the Wind",
        "author": {
            "id": 1,
            "first_name": "Patrick",
            "last_name": "Rothfuss"
        },
        "category": {
            "id": 1,
            "name": "Fantasy"
        },
        "is_fiction": true,
        "in_store": 0,
        "comments": [
            {
                "id": 1,
                "body": "Name of the Wind is a fantastic take on the young hero trope",
                "user": {
                    "id": 2,
                    "first_name": "Denna",
                    "last_name": "Thomas"
                }
            }
        ]
    },
    {
        "id": 2,
        "title": "The Wise Man's Fear",
        "author": {
            "id": 1,
            "first_name": "Patrick",
            "last_name": "Rothfuss"
        },
        "category": {
            "id": 1,
            "name": "Fantasy"
        },
        "is_fiction": true,
        "in_store": 2,
        "comments": [
            {
                "id": 2,
                "body": "Book 2 of 3 in The Kingkiller Chronicles",
                "user": {
                    "id": 1,
                    "first_name": "Steve",
                    "last_name": "Todorovic"
                }
            }
        ]
    },
```

### RETURN STATUS
- 200 OK

---

## */books/\<int:id\>*

### Description
- Return a book entity using it's ID. 
- This endpoint will return a book entity with the book ID, title, a nested list of attributes of the author with the author ID, author first name and author last name, a nested attribute of the category with the category ID and category name. It will show if the book is fiction or not and the in store inventory number. Lastly, it will return a nested list of attributes of any comments made about the book, including the attributes comment ID, comment body, and a further nested attribute of the user that made the comment with the users ID, user first_name and user Last_name.  

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - GET

### EXAMPLE
 - /books/1

### ARGUMENTS
 - Book ID (books.id, Integer)
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None
  
### RESPONSE BODY EXAMPLE 

```py
{
    "id": 1,
    "title": "The Name of the Wind",
    "author": {
        "id": 1,
        "first_name": "Patrick",
        "last_name": "Rothfuss"
    },
    "category": {
        "id": 1,
        "name": "Fantasy"
    },
    "is_fiction": true,
    "in_store": 0,
    "comments": [
        {
            "id": 1,
            "body": "Name of the Wind is a fantastic take on the young hero trope",
            "user": {
                "id": 2,
                "first_name": "Denna",
                "last_name": "Thomas"
            }
        }
    ]
}
```

### RETURN STATUS
- 200 OK

---

## */books/\<string:name\>*

### Description
- Return a book entity using it's Title. 
- This endpoint will return a book entity with the book ID, title, a nested list of attributes of the author with the author ID, author first name and author last name, a nested attribute of the category with the category ID and category name. It will show if the book is fiction or not and the in store inventory number. Lastly, it will return a nested list of attributes of any comments made about the book, including the attributes comment ID, comment body, and a further nested attribute of the user that made the comment with the users ID, user first_name and user Last_name. 

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - GET

### EXAMPLE
 - /books/The%20Name%20of%20the%20Wind

### ARGUMENTS
 - Book Title (books.title, String)
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None
  
### RESPONSE BODY EXAMPLE 

```py
{
    "id": 1,
    "title": "The Name of the Wind",
    "author": {
        "id": 1,
        "first_name": "Patrick",
        "last_name": "Rothfuss"
    },
    "category": {
        "id": 1,
        "name": "Fantasy"
    },
    "is_fiction": true,
    "in_store": 0,
    "comments": [
        {
            "id": 1,
            "body": "Name of the Wind is a fantastic take on the young hero trope",
            "user": {
                "id": 2,
                "first_name": "Denna",
                "last_name": "Thomas"
            }
        }
    ]
}
```

### RETURN STATUS
- 200 OK

---

## */books/author/\<int:author.id\>*

### Description
- Return all book entities by an author using the author ID. 
- This endpoint will return all book entities by a specific author with the book ID, title, a nested attribute of the category with the category id and the category name. It will show if the book is fiction or not and the in store inventory number.

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - GET

### EXAMPLE
 - /books/author/1

### ARGUMENTS
 - Author ID (author.id, Integer)
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None
  
### RESPONSE BODY EXAMPLE 

```py
[
    {
        "id": 1,
        "title": "The Name of the Wind",
        "category": {
            "id": 1,
            "name": "Fantasy"
        },
        "is_fiction": true,
        "in_store": 0
    },
    {
        "id": 2,
        "title": "The Wise Man's Fear",
        "category": {
            "id": 1,
            "name": "Fantasy"
        },
        "is_fiction": true,
        "in_store": 2
    }
]
```

### RETURN STATUS
- 200 OK

---
## */books/category/\<int:category.id\>*

### Description
- Return all book entities by category using the category ID. 
- This endpoint will return all book entities with the book ID, title, a nested list of attributes of the author with the author ID, author first name and author last name. It will return if the book is fiction or not and the in store inventory number.

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - GET

### EXAMPLE
 - /books/category/1

### ARGUMENTS
 - Category ID (category.id, Integer)
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None
  
### RESPONSE BODY EXAMPLE 

```py
[
    {
        "id": 1,
        "title": "The Name of the Wind",
        "author": {
            "id": 1,
            "first_name": "Patrick",
            "last_name": "Rothfuss"
        },
        "is_fiction": true,
        "in_store": 0
    },
    {
        "id": 2,
        "title": "The Wise Man's Fear",
        "author": {
            "id": 1,
            "first_name": "Patrick",
            "last_name": "Rothfuss"
        },
        "is_fiction": true,
        "in_store": 2
    },
    {
        "id": 3,
        "title": "The Way of Kings",
        "author": {
            "id": 2,
            "first_name": "Brandon",
            "last_name": "Sanderson"
        },
        "is_fiction": true,
        "in_store": 4
    }
]
```

### RETURN STATUS
- 200 OK

---

## */books/fiction/\<string:is_fiction\>*

### Description
- Return all book entities classed as Fiction or Non Fiction depending on aurgument sent. 
- This endpoint will return every book entity that is either Fiction or Non Fiction with the book ID, title, a nested list of attributes of the author with the author ID, author first name and author last name, a nested attribute of the category with the category ID and category name. It will show the books in store inventory number. Lastly, it will return a nested list of attributes of any comments made about the book, including the attributes comment ID, comment body, and a further nested attribute of the user that made the comment with the users ID, user first_name and user Last_name. 
  
### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - GET

### EXAMPLE
 - /books/fiction/False  
  OR
 - /books/fiction/false  
  OR
 - /books/fiction/0

### ARGUMENTS
 - Is Fiction: True (1) or False (0) (books.is_fiction, Boolean)
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None
  
### RESPONSE BODY EXAMPLE 

```py
[
    {
        "id": 7,
        "title": "Automate the Boring Stuff with Python",
        "author_id": 6,
        "author": {
            "id": 6,
            "first_name": "Al",
            "last_name": "Sweigart"
        },
        "category_id": 5,
        "category": {
            "id": 5,
            "name": "Educational"
        },
        "in_store": 1,
        "comments": []
    }
]
```

### RETURN STATUS
- 200 OK
  
---

## */books*

### Description
- Create a new book entity. 
- This endpoint will return the new book entity with the book ID, title, a nested list of attributes of the author with the author ID, author first name and author last name, a nested list of attributes of the category with the category ID and category name. It will return if the book is fiction or not and the in store inventory number.

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - POST

### EXAMPLE
 - /books

### ARGUMENTS
 - None
  
### REQUIRED DATA
 - Title (book.title, String)
 - Author ID (author.id, Integer)
 - Category ID (category.id, Integer)
 - Is Fiction Indicator (book.is_fiction, Boolean)
 - In Store Number (book.in_store, Integer)

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE

```py
{
    "title": "Fox in Socks",
    "is_fiction": true,
    "in_store": 7,
    "author_id": 3,
    "category_id": 3
}
```
  
### RESPONSE BODY EXAMPLE 

```py
{
    "id": 12,
    "title": "Fox in Socks",
    "author": {
        "id": 3,
        "first_name": "Dr",
        "last_name": "Seuss"
    },
    "category": {
        "id": 3,
        "name": "Children"
    },
    "is_fiction": true,
    "in_store": 7
}
```

### RETURN STATUS
- 201 CREATED

---

## */books/\<int:books.id>*

### Description
- Updates a book entities attributes. 
- This endpoint will return the updated book entity with the book ID, title, a nested list of attributes of the author with the author ID, author first name and author last name, a nested attribute of the category with the category ID and category name. It will show if the book is fiction or not and the in store inventory number. Lastly, it will return a nested list of attributes of any comments made about the book, including the attributes comment ID, comment body, and a further nested attribute of the user that made the comment with the users ID, user first_name and user Last_name.  
 

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin required through JWT Bearer Token

### METHOD
 - POST

### EXAMPLE
 - /books/4

### ARGUMENTS
 - Book ID (books.id, Integer)
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - Title (book.title, String)
 - Author ID (author.id, Integer)
 - Category ID (category.id, Integer)
 - Is Fiction Indicator (book.is_fiction, Boolean)
 - In Store Number (book.in_store, Integer)
 - 
### REQUEST BODY EXAMPLE

```py
{
    "in_store": 4,
    "is_fiction": 1
}
```
  
### RESPONSE BODY EXAMPLE 

```py
{
    "id": 4,
    "title": "Catch 22",
    "author": {
        "id": 4,
        "first_name": "Joseph",
        "last_name": "Heller"
    },
    "category": {
        "id": 4,
        "name": "Satirical"
    },
    "is_fiction": true,
    "in_store": 4,
    "comments": [
        {
            "id": 4,
            "body": "Hilarious and harrowing at the same time!",
            "user": {
                "id": 3,
                "first_name": "Sebastian",
                "last_name": "Townsend"
            }
        }
    ]
}
```

### RETURN STATUS
- 200 OK

---

## */books/comment/\<int:book.id\>*

### Description
- Create a comment entity linked to a book by the book ID. 
- This endpoint will return the comment entity including the comment id, the comment body, a nested list of attributes from the linked book including book title. A further nested list of attributes from the book's author including author id, author first name and author last name. Finally it will return a nested list of attributes from the user who created the comment including user id, user first name and user last name. 

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token
 - Authorisation as admin required through JWT Bearer Token

### METHOD
 - POST, PATCH

### EXAMPLE
 - /categories/6

### ARGUMENTS
 - None
  
### REQUIRED DATA
- None

### OPTIONAL DATA
 - Category Name (category.name, String)
 - Description (category.description, String)

### REQUEST BODY EXAMPLE

```py
{
    "name": "Another name",
    "description": "Another description"
}
```

### RESPONSE BODY EXAMPLE 

```py
{
    "id": 6,
    "name": "Another name",
    "description": "Another description"
}
```

### RETURN STATUS
- 200 OK

---

## */categories\<int:id\>*

### Description
- Delete a category entity in the database using it's ID. 
- This endpoint will return a response message informing the client of a successful deletion.  

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token
 - Authorisation as admin required through JWT Bearer Token

### METHOD
 - DELETE

### EXAMPLE
 - /categories/6

### ARGUMENTS
 - None
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None

### RESPONSE BODY EXAMPLE 

```py
{
    "message": "Category 'Another name' deleted successfully"
}
```

### RETURN STATUS
- 200 OK

---

## **CATEGORIES**

---

## */categories*

### Description
- Return a list of all the category entities in the database. 
- This endpoint will return the category id, the category name, and a description of the category.  

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - GET

### EXAMPLE
 - /categories

### ARGUMENTS
 - None
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None
  
### RESPONSE BODY EXAMPLE 

```py
[
    {
        "id": 1,
        "name": "Fantasy",
        "description": "Imaginative fiction dependent for effect on strangeness of setting (such as other worlds or times) and of characters (such as supernatural or unnatural beings)."
    },
    {
        "id": 2,
        "name": "Sci-Fi",
        "description": "Science fiction, also often known as \"sci-fi\", is a genre of literature that is imaginative and based around science. It relies heavily on scientific facts, theories, and principles as support for its settings, characters, themes, and plot."
    },
    {
        "id": 3,
        "name": "Children",
        "description": "Children's books are everything from Young Adult down to board books for your teething kiddo, however, a book is considered a children's book when it's intended for an audience between 0-8 years old."
    },
```

### RETURN STATUS
- 200 OK

---

## */categories/\<int:id\>*

### Description
- Return a category entity stored in the database from it's ID. 
- This endpoint will return the category id, the category name, and a description of the category.  

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - GET

### EXAMPLE
 - /categories/1

### ARGUMENTS
 - None
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None
  
### RESPONSE BODY EXAMPLE 

```py
{
    "id": 1,
    "name": "Fantasy",
    "description": "Imaginative fiction dependent for effect on strangeness of setting (such as other worlds or times) and of characters (such as supernatural or unnatural beings)."
}
```

### RETURN STATUS
- 200 OK

---

## */categories/\<string:name\>*

### Description
- Return a category entity stored in the database from it's name. 
- This endpoint will return the category id, the category name, and a description of the category.  

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - GET

### EXAMPLE
 - /categories/Fantasy

### ARGUMENTS
 - None
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None
  
### RESPONSE BODY EXAMPLE 

```py
{
    "id": 1,
    "name": "Fantasy",
    "description": "Imaginative fiction dependent for effect on strangeness of setting (such as other worlds or times) and of characters (such as supernatural or unnatural beings)."
}
```

### RETURN STATUS
- 200 OK

---

## */categories*

### Description
- Create a new category entity in the database. 
- This endpoint will return the new category id, the category name, and a description of the category.  

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token
 - Authorisation as admin required through JWT Bearer Token

### METHOD
 - POST

### EXAMPLE
 - /categories

### ARGUMENTS
 - None
  
### REQUIRED DATA
 - Category Name (category.name, String)
 - Description (category.description, String)

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE

```py
{
    "name": "Test Categpry",
    "description": "Test category description"
}
```

### RESPONSE BODY EXAMPLE 

```py
{
    "id": 6,
    "name": "Test Categpry",
    "description": "Test category description"
}
```

### RETURN STATUS
- 201 CREATED

---

## */categories\<int:id\>*

### Description
- Update a category entity in the database using it's ID. 
- This endpoint will return the updated category entity including the category id, the category name, and a description of the category.  

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token
 - Authorisation as admin required through JWT Bearer Token

### METHOD
 - POST, PATCH

### EXAMPLE
 - /categories/6

### ARGUMENTS
 - None
  
### REQUIRED DATA
- None

### OPTIONAL DATA
 - Category Name (category.name, String)
 - Description (category.description, String)

### REQUEST BODY EXAMPLE

```py
{
    "name": "Another name",
    "description": "Another description"
}
```

### RESPONSE BODY EXAMPLE 

```py
{
    "id": 6,
    "name": "Another name",
    "description": "Another description"
}
```

### RETURN STATUS
- 200 OK

---

## */categories\<int:id\>*

### Description
- Delete a category entity in the database using it's ID. 
- This endpoint will return a response message informing the client of a successful deletion.  

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token
 - Authorisation as admin required through JWT Bearer Token

### METHOD
 - DELETE

### EXAMPLE
 - /categories/6

### ARGUMENTS
 - None
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None

### RESPONSE BODY EXAMPLE 

```py
{
    "message": "Category 'Another name' deleted successfully"
}
```

### RETURN STATUS
- 200 OK

---

## **COMMENTS**

---

## */comments*

### Description
- Return all comments made by all users.
- This end point will return the comment body and comment ID, and nested attributes from the book (title), including nested attributes from the book's author (first name and last name), and user associated with the comment (Id, first name and last name)

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not needed

### METHOD
 - GET

### EXAMPLE
 - /comments

### ARGUMENTS
 - None
    
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE 
 - None
  
### RESPONSE BODY EXAMPLE 
```py
[
    {
        "id": 1,
        "body": "Name of the Wind is a fantastic take on the young hero trope",
        "book": {
            "title": "The Name of the Wind",
            "author": {
                "first_name": "Patrick",
                "last_name": "Rothfuss"
            }
        },
        "user": {
            "id": 2,
            "first_name": "Steve",
            "last_name": "Thomas"
        }
    },
    {
        "id": 2,
        "body": "Book 2 of 3 in The Kingkiller Chronicles",
        "book": {
            "title": "The Wise Man's Fear",
            "author": {
                "first_name": "Patrick",
                "last_name": "Rothfuss"
            }
        },
        "user": {
            "id": 1,
            "first_name": "Steve",
            "last_name": "Todorovic"
        }
    },
```

### RETURN STATUS
- 200 OK

---

## */comments/\<int:id\>*

### Description
- Return a specific comment by ID.
- This end point will return the typical comment schema for a specific comment, identified by the comment ID.

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not needed

### METHOD
 - GET

### EXAMPLE
 - /comments/1

### ARGUMENTS
 - Comment ID (comment.id, Integer)
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE 
 - None
  
### RESPONSE BODY EXAMPLE 
```py
{
    "id": 1,
    "body": "Name of the Wind is a fantastic take on the young hero trope",
    "book": {
        "title": "The Name of the Wind",
        "author": {
            "first_name": "Patrick",
            "last_name": "Rothfuss"
        }
    },
    "user": {
        "id": 2,
        "first_name": "Steve",
        "last_name": "Thomas"
    }
}
```

### RETURN STATUS
- 200 OK

---

## */comments/user/\<int:user_id\>*

### Description
- Return all comments made by a specific user.
- This end point will return the typical comment schema from a specific user, identified by their User ID.

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not needed

### METHOD
 - GET

### EXAMPLE
 - /comments/user/1

### ARGUMENTS
 - User ID (comment.user_id, Integer)
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None
 - 
### REQUEST BODY EXAMPLE 
 - None
  
### RESPONSE BODY EXAMPLE 
```py
{
    "id": 1,
    "body": "Name of the Wind is a fantastic take on the young hero trope",
    "book": {
        "title": "The Name of the Wind",
        "author": {
            "first_name": "Patrick",
            "last_name": "Rothfuss"
        }
    },
    "user": {
        "id": 2,
        "first_name": "Steve",
        "last_name": "Thomas"
    }
}
```

### RETURN STATUS
- 200 OK
  
---

## */comments/\<int:id\>*

### Description
- Update the body text of a specific comment, by ID.
- This end point will return the typical comment schema with an updated comment body.

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not needed

### METHOD
 - PUT / PATCH

### EXAMPLE
 - /comments/3

### ARGUMENTS
 - Comment ID (comment.id, Integer)
  
### REQUIRED DATA
 - Comment Body (comment.body, Text)

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE 
```py
{
    "body": "Updated comment body"
}
```
  
### RESPONSE BODY EXAMPLE 
```py
{
    "id": 3,
    "body": "Updated comment body",
    "book": {
        "title": "The Way of Kings",
        "author": {
            "first_name": "Brandon",
            "last_name": "Sanderson"
        }
    },
    "user": {
        "id": 3,
        "first_name": "Sebastian",
        "last_name": "Townsend"
    }
}
```

### RETURN STATUS
- 200 OK
  
---

## */comments/\<int:id\>*

### Description
- Delete a specific comment, by ID.

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin required through JWT Bearer Token  
  
### METHOD
 - DELETE

### EXAMPLE
 - /comments/1

### ARGUMENTS
 - Comment ID (comment.id, Integer)
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE 
 - None

### RESPONSE BODY EXAMPLE 
```py
{
    "message": "Comment No.1 deleted successfully"
}
```

### RETURN STATUS
- 200 OK

--- 
## Create comments endpoint found [here]() in Books endpoints

---

## **USERS**

---

## */users*

### Description
- Return a list of all the user entities in the database. 
- This endpoint will return the user id, first name, last name, email address and their admin status.

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - GET

### EXAMPLE
 - /users

### ARGUMENTS
 - None
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None

### RESPONSE BODY EXAMPLE 

```py
[
    {
        "id": 1,
        "first_name": "Steve",
        "last_name": "Todorovic",
        "email": "steve@email.com",
        "is_admin": true
    },
    {
        "id": 2,
        "first_name": "Sebastian",
        "last_name": "Townsend",
        "email": "bast@email.com",
        "is_admin": false
    },
```

### RETURN STATUS
- 200 OK

---
---

## */users/\<int:id\>*

### Description
- Return a user entity stored in the database from it's ID. 
- This endpoint will return the user id, first name, last name, email address and their admin status.  

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - GET

### EXAMPLE
 - /users/1

### ARGUMENTS
 - None
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None
  
### RESPONSE BODY EXAMPLE 

```py
{
    "id": 1,
    "first_name": "Steve",
    "last_name": "Todorovic",
    "email": "steve@email.com",
    "is_admin": true
}
```

### RETURN STATUS
- 200 OK

---

## */users/first_name/\<string:name\>*

### Description
- Return a user entity stored in the database from it's first name. 
- This endpoint will return the user id, first name, last name, email address and their admin status.  

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - GET

### EXAMPLE
 - /user/first_name/Steve

### ARGUMENTS
 - First Name (user.first_name, String)
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None
  
### RESPONSE BODY EXAMPLE 

```py
{
    "id": 1,
    "first_name": "Steve",
    "last_name": "Todorovic",
    "email": "steve@email.com",
    "is_admin": true
}
```

### RETURN STATUS
- 200 OK

---

## */users/last_name/\<string:name\>*

### Description
- Return a user entity stored in the database from it's last name. 
- This endpoint will return the user id, first name, last name, email address and their admin status.  

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token 
 - Authorisation as admin not required

### METHOD
 - GET

### EXAMPLE
 - /user/last_name/Todorovic

### ARGUMENTS
 - Last Name (user.last_name, String)
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None
  
### RESPONSE BODY EXAMPLE 

```py
{
    "id": 1,
    "first_name": "Steve",
    "last_name": "Todorovic",
    "email": "steve@email.com",
    "is_admin": true
}
```

### RETURN STATUS
- 200 OK

---

## For **creating a new user**, the endpoint can be found [here](#authregister) in the Auth documentation

---

## */users\<int:id\>*

### Description
- Update a user entity in the database using it's ID. 
- This endpoint will return the updated user id, first name, last name, email address and their admin status.  

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token
 - Authorisation as admin required through JWT Bearer Token

### METHOD
 - POST, PATCH

### EXAMPLE
 - /user/1

### ARGUMENTS
 - User ID (user.id, Integer)
 - 
### REQUIRED DATA
- None
  
### OPTIONAL DATA
 - First Name (user.first_name, String)
 - Last Name (user.last_name, String)
 - Email Address (user.email, String)
 - Password (user.password, String)

### REQUEST BODY EXAMPLE

```py
{
    "email": "new@email.com"
}
```

### RESPONSE BODY EXAMPLE 

```py
{
    "id": 1,
    "first_name": "Steve",
    "last_name": "Todorovic",
    "email": "new@email.com",
    "is_admin": true
}
```

### RETURN STATUS
- 200 OK

---

## */users\<int:id\>*

### Description
- Delete a user entity in the database using it's ID. 
- This endpoint will return a response message informing the client of a successful deletion.  

### Authorisation and Authentication: 
 - Authentication required through JWT Bearer Token
 - Authorisation as admin required through JWT Bearer Token

### METHOD
 - DELETE

### EXAMPLE
 - /users/1

### ARGUMENTS
 - None
  
### REQUIRED DATA
 - None

### OPTIONAL DATA
 - None

### REQUEST BODY EXAMPLE
 - None

### RESPONSE BODY EXAMPLE 

```py
{
    "message": "User 'Steve Todorovic' deleted successfully"
}
```

### RETURN STATUS
- 200 OK

---


## R6 - Make an ERD for the app
This is my ERD for my Book Store application.  
![Book_Store_ERD](Images/book_store_ERD4.png)

## R9 - Discuss the database relations to be implemented in your application

My book store database will be tracking several entities which I will describe here. It will have a ‘Users’ table, which will contain attributes such as the table’s Primary Key, the unique User ID (Integer, NOT NULL), the users first name (String, varchar(50), NOT NULL), last name (String, varchar(50)), the users email address which must be unique (String, NOT NULL, unique=True), a password (String, NOT NULL) and whether the user has Admin access or not (Boolean, NOT NULL, Default=FALSE).  

The second table will be ‘Books’, with attributes such as the table’s Primary Key, the unique Book ID (Integer, NOT NULL), the books title (String, varchar(200), NOT NULL), if it is fiction (Boolean), if it is kid friendly (Boolean) and the number of copies in store (Integer). The ‘Books’ table will also have two Foreign Keys, an Author ID (Integer, NOT NULL), which will connect to a table called ‘Authors’ with a one and only one on the authors side to an optional many on the books side, and a Category ID (Integer, NOT NULL), which will connect to a table called ‘Categories’ with a one and only one on the categories side to an optional many on the books side.  

The ‘Authors’ table will contain the attributes about the author, such as the table’s Primary Key, the unique Author ID (Integer, NOT NULL), the author’s first name (String, varchar(50), NOT NULL), last name (String, varchar(50), NOT NULL), any accolades they may have garnered (Text) and a short description called ‘about’ (Text).  

The ‘Categories’ table will contain attributes such as the table’s Primary Key, the unique Category ID (Integer, NOT NULL), the category name (String, varchar(100), NOT NULL) and a short description about the category called ‘description’ (Text).  

The final table is a joining table between the ‘Books’ table and the ‘Users’ table, called ‘Comments’. The ‘Comments’ table will contain attributes such as the table’s Primary Key, the unique Comment ID (Integer, NOT NULL), the comment body (Text), and two foreign keys, the User ID (Integer, NOT NULL) of the user that has created the comment, and the Book ID (Integer, NOT NULL) of the book the comment is about. The ‘Comments’ table will connect to the ‘Users’ table with a one and only one on the users side to an optional many on the comments side, and it will connect to the ‘Books’ table with a one and only one on the books side to an optional many on the comments side.  

## R10 - Describe the way tasks are allocated and tracked in your project

Link to my Trello Board used for this project:  
[API Project Trello Board](https://trello.com/b/muUAZRzW/api-assignment)  
