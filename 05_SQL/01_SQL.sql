DROP DATABASE IF EXISTS ai_ml_database;
CREATE DATABASE ai_ml_database;
USE ai_ml_database;

-- ============================================================
-- 1. COMMON DATA TYPES (REFERENCE)
-- ============================================================
-- CHAR(n)      fixed-length string
-- VARCHAR(n)   variable-length string
-- BLOB         binary large object
-- INT          integer
-- TINYINT      small integer
-- BIGINT       large integer
-- BIT(n)       bit values
-- FLOAT        approximate decimal
-- DOUBLE       approximate decimal
-- BOOLEAN      TRUE/FALSE (MySQL represents it as TINYINT)
-- DATE         YYYY-MM-DD
-- TIME         HH:MM:SS
-- YEAR         four-digit year
-- UNSIGNED     non-negative numeric values

-- ============================================================
-- 2. DDL — DATA DEFINITION LANGUAGE
-- ============================================================

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    email VARCHAR(100),
    manager_id INT
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    city VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(100),
    order_date DATE,
    amount DECIMAL(10,2),
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL
);

-- ALTER TABLE examples
ALTER TABLE employees ADD COLUMN phone VARCHAR(20);
ALTER TABLE employees MODIFY COLUMN phone VARCHAR(25);
ALTER TABLE employees RENAME COLUMN phone TO phone_number;
ALTER TABLE employees DROP COLUMN phone_number;

-- Indexes
CREATE INDEX idx_employee_name ON employees(first_name);
CREATE INDEX idx_customer_country ON customers(country);
DROP INDEX idx_employee_name ON employees;

-- Constraint patterns (reference):
-- ALTER TABLE orders ADD CONSTRAINT fk_customer
-- FOREIGN KEY (customer_id) REFERENCES customers(customer_id);
-- ALTER TABLE orders DROP FOREIGN KEY fk_orders_customer;

-- TRUNCATE removes rows but keeps table structure:
-- TRUNCATE TABLE table_name;

-- ============================================================
-- 3. SAMPLE DATA
-- ============================================================

INSERT INTO customers (customer_id, customer_name, country, city, email) VALUES
(1,'Alice','India','Ahmedabad','alice@example.com'),
(2,'Bob','India','Vadodara','bob@example.com'),
(3,'Carol','USA','New York',NULL),
(4,'David','India','Mumbai','david@example.com'),
(5,'Eva','USA','Chicago',NULL);

INSERT INTO employees
(employee_id,first_name,last_name,department,salary,email,manager_id) VALUES
(1,'Alice','Shah','Sales',50000,'alice@company.com',3),
(2,'Bob','Patel','Sales',60000,'bob@company.com',3),
(3,'Carol','Mehta','Management',90000,'carol@company.com',NULL),
(4,'David','Joshi','IT',75000,'david@company.com',1),
(5,'Eva','Desai','IT',65000,'eva@company.com',3),
(6,'Frank','Shah','HR',55000,'frank@company.com',NULL);

INSERT INTO orders (order_id,customer_id,product,order_date,amount) VALUES
(101,1,'Laptop','2023-01-10',1000),
(102,3,'Smartphone','2023-05-20',500),
(103,2,'Headphones','2023-06-30',50),
(104,4,'Monitor','2023-07-15',300);

INSERT INTO products (product_id,product_name,category,price) VALUES
(1,'Laptop','Electronics',1000),
(2,'Smartphone','Electronics',500),
(3,'Headphones','Accessories',50),
(4,'Monitor','Electronics',300);

INSERT INTO suppliers (supplier_id,supplier_name) VALUES
(101,'SupplierA'),(102,'SupplierB');

-- ============================================================
-- 4. DQL / DRL — SELECT AND FILTERING
-- ============================================================

SELECT first_name, last_name FROM employees;
SELECT * FROM customers;

-- WHERE + comparison operators (=, >, <, >=, <=, <>)
SELECT * FROM customers WHERE country = 'India';
SELECT * FROM employees WHERE salary > 60000;

-- AND / OR / NOT
SELECT * FROM customers
WHERE country = 'India' AND city = 'Vadodara';

SELECT * FROM customers
WHERE country = 'USA' OR city = 'Mumbai';

SELECT * FROM customers
WHERE NOT country = 'India';

-- DISTINCT
SELECT DISTINCT country FROM customers;
SELECT DISTINCT department FROM employees;

-- LIKE: % = zero or more characters, _ = one character
SELECT * FROM employees WHERE first_name LIKE 'J%';
SELECT * FROM employees WHERE first_name LIKE '%a';
SELECT * FROM employees WHERE first_name LIKE '%a%';
SELECT * FROM employees WHERE first_name LIKE '_a%';
SELECT * FROM employees WHERE first_name LIKE 'A_';
SELECT * FROM employees WHERE first_name LIKE 'A__%';
SELECT * FROM customers WHERE customer_name LIKE 'a%o';

-- IN
SELECT * FROM products
WHERE category IN ('Electronics','Accessories');

-- BETWEEN
SELECT * FROM orders
WHERE order_date BETWEEN '2023-01-01' AND '2023-06-30';

SELECT * FROM employees WHERE salary BETWEEN 50000 AND 70000;

-- IS NULL
SELECT * FROM customers WHERE email IS NULL;
SELECT * FROM employees WHERE manager_id IS NULL;

-- AS (aliases)
SELECT first_name AS 'First Name', last_name AS 'Last Name'
FROM employees;

SELECT product_name AS Product,
       price * 1.10 AS DiscountedPrice
FROM products;

-- ORDER BY
SELECT * FROM products ORDER BY price;
SELECT * FROM products ORDER BY price ASC;
SELECT * FROM products ORDER BY price DESC;
SELECT * FROM employees ORDER BY department, salary DESC;
SELECT product_name, price, price * 1.10 AS adjusted_price
FROM products ORDER BY adjusted_price DESC;
SELECT product_name, price FROM products ORDER BY 2 DESC, 1 ASC;

-- ============================================================
-- 5. GROUP BY, AGGREGATES, HAVING
-- ============================================================

SELECT department, AVG(salary) AS average_salary
FROM employees GROUP BY department;

SELECT COUNT(*) AS total_employees FROM employees;
SELECT SUM(salary) AS total_salary FROM employees;
SELECT AVG(salary) AS average_salary FROM employees;
SELECT MAX(salary) AS maximum_salary FROM employees;
SELECT MIN(salary) AS minimum_salary FROM employees;

SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
ORDER BY employee_count DESC;

-- ============================================================
-- 6. DML — INSERT, UPDATE, DELETE
-- ============================================================

INSERT INTO employees
(employee_id,first_name,last_name,department,salary,email)
VALUES (7,'John','Doe','Sales',50000,'john@example.com');

UPDATE employees
SET salary = 55000
WHERE first_name = 'John';

DELETE FROM employees
WHERE first_name = 'John';

-- ============================================================
-- 7. DCL — GRANT / REVOKE (REFERENCE)
-- ============================================================
-- These commands require suitable privileges and are intentionally
-- commented out so this learning file does not change server access.
--
-- GRANT SELECT ON Employees TO Analyst;
-- REVOKE SELECT ON Employees FROM Analyst;

-- ============================================================
-- 8. TCL — COMMIT, ROLLBACK, SAVEPOINT
-- ============================================================

START TRANSACTION;
UPDATE employees SET salary = salary * 1.10 WHERE department = 'Sales';
COMMIT;

START TRANSACTION;
UPDATE employees SET salary = salary - 1000 WHERE department = 'IT';
ROLLBACK;

START TRANSACTION;
UPDATE employees SET salary = salary - 100 WHERE employee_id = 1;
SAVEPOINT before_second_update;
UPDATE employees SET salary = salary + 100 WHERE employee_id = 2;
ROLLBACK TO SAVEPOINT before_second_update;
COMMIT;

-- ============================================================
-- 9. JOINS
-- ============================================================

-- INNER JOIN
SELECT c.customer_name, o.product
FROM customers AS c
INNER JOIN orders AS o
ON c.customer_id = o.customer_id;

-- LEFT JOIN
SELECT c.customer_name, o.product
FROM customers AS c
LEFT JOIN orders AS o
ON c.customer_id = o.customer_id;

-- RIGHT JOIN
SELECT c.customer_name, o.product
FROM customers AS c
RIGHT JOIN orders AS o
ON c.customer_id = o.customer_id;

-- FULL OUTER JOIN concept from the notes.
-- MySQL has no direct FULL OUTER JOIN syntax, so a common
-- workaround is LEFT JOIN UNION RIGHT JOIN:
SELECT c.customer_name, o.product
FROM customers AS c
LEFT JOIN orders AS o ON c.customer_id = o.customer_id
UNION
SELECT c.customer_name, o.product
FROM customers AS c
RIGHT JOIN orders AS o ON c.customer_id = o.customer_id;

-- CROSS JOIN
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);

INSERT INTO students VALUES (1,'Alice'),(2,'Bob');
INSERT INTO courses VALUES (101,'Maths'),(102,'Science');

SELECT s.student_name, c.course_name
FROM students AS s
CROSS JOIN courses AS c;

-- SELF JOIN
SELECT e1.first_name AS Employee,
       e2.first_name AS Manager
FROM employees AS e1
JOIN employees AS e2
ON e1.manager_id = e2.employee_id;

-- ============================================================
-- 10. SET OPERATIONS
-- ============================================================

-- UNION removes duplicates.
SELECT customer_name AS name FROM customers
UNION
SELECT supplier_name AS name FROM suppliers;

-- INTERSECT returns common rows (supported in MySQL 8.0.31+).
SELECT customer_name AS name FROM customers
INTERSECT
SELECT supplier_name AS name FROM suppliers;

-- EXCEPT returns rows from the first query absent in the second
-- (supported in MySQL 8.0.31+).
SELECT customer_name AS name FROM customers
EXCEPT
SELECT supplier_name AS name FROM suppliers;

-- UNION ALL keeps duplicates.
SELECT customer_name AS name FROM customers
UNION ALL
SELECT supplier_name AS name FROM suppliers;

-- ============================================================
-- 11. SUBQUERIES
-- ============================================================

-- Products whose price is above the average product price.
SELECT product_name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products);

-- A subquery can also provide a set of values for IN.
SELECT *
FROM employees
WHERE department IN (
    SELECT department
    FROM employees
    WHERE salary > 80000
);

-- General pattern:
-- SELECT columns
-- FROM table
-- WHERE column OPERATOR
--       (SELECT column FROM table WHERE condition);

-- ============================================================
-- 12. SUBQUERIES VS JOINS — QUICK REFERENCE
-- ============================================================
-- Subqueries: useful for filtering/comparison/calculation based
-- on the result of another query.
-- Joins: useful for combining related data from multiple tables.

-- JOIN example:
SELECT c.customer_name, o.product
FROM customers AS c
JOIN orders AS o
ON c.customer_id = o.customer_id;

-- SUBQUERY example:
SELECT product_name
FROM products
WHERE price > (SELECT AVG(price) FROM products);

-- ============================================================
-- 13. SQL CLAUSE ORDER — QUICK REVISION
-- ============================================================
-- SELECT
-- FROM
-- WHERE
-- GROUP BY
-- HAVING
-- ORDER BY

SELECT department,
       COUNT(*) AS employee_count,
       AVG(salary) AS average_salary
FROM employees
WHERE salary >= 50000
GROUP BY department
HAVING COUNT(*) >= 1
ORDER BY average_salary DESC;
