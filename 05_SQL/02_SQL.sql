-- ============================================================
-- 1. TRANSACTIONS
-- ============================================================

-- A transaction is a sequence of SQL statements treated as a unit.

-- ACID PROPERTIES
--
-- Atomicity  : All statements succeed or none succeed.
-- Consistency : Data moves from one valid state to another.
-- Isolation  : Parallel transactions do not interfere.
-- Durability : Committed data is permanently saved.


-- ============================================================
-- 2. AUTOCOMMIT
-- ============================================================

-- Disable autocommit:
SET autocommit = 0;

-- Enable autocommit:
SET autocommit = 1;


-- ============================================================
-- 3. START TRANSACTION + COMMIT
-- ============================================================

-- Example transaction:
--
-- START TRANSACTION;
--
-- UPDATE accounts
-- SET balance = balance - 50
-- WHERE id = 1;
--
-- UPDATE accounts
-- SET balance = balance + 50
-- WHERE id = 2;
--
-- COMMIT;


-- ============================================================
-- 4. ROLLBACK
-- ============================================================

-- ROLLBACK undoes changes made during the current transaction
-- that have not yet been committed.
--
-- Example:
--
-- START TRANSACTION;
--
-- UPDATE accounts
-- SET balance = balance - 100
-- WHERE id = 1;
--
-- UPDATE accounts
-- SET balance = balance + 100
-- WHERE id = 3;
--
-- ROLLBACK;


-- ============================================================
-- 5. SAVEPOINT
-- ============================================================

-- A SAVEPOINT creates a named point inside a transaction.
-- You can roll back to that point without undoing the entire
-- transaction.

-- Example from the class:
--
-- START TRANSACTION;
--
-- UPDATE accounts
-- SET balance = balance + 1000
-- WHERE id = 1;
--
-- SAVEPOINT after_wallet_topup;
--
-- UPDATE accounts
-- SET balance = balance + 10
-- WHERE id = 1;
--
-- ROLLBACK TO after_wallet_topup;
--
-- COMMIT;


-- ============================================================
-- 6. TRANSACTION PRACTICE SETUP
-- ============================================================

CREATE TABLE IF NOT EXISTS accounts (
    id INT PRIMARY KEY,
    balance DECIMAL(10, 2) NOT NULL
);

INSERT INTO accounts (id, balance)
VALUES
    (1, 5000.00),
    (2, 3000.00),
    (3, 7000.00)
ON DUPLICATE KEY UPDATE
    balance = VALUES(balance);

-- Check account balances:
SELECT * FROM accounts;


-- ============================================================
-- 7. TRANSACTION PRACTICE
-- ============================================================

START TRANSACTION;

UPDATE accounts
SET balance = balance - 50
WHERE id = 1;

UPDATE accounts
SET balance = balance + 50
WHERE id = 2;

COMMIT;

SELECT * FROM accounts;


-- ============================================================
-- 8. ROLLBACK PRACTICE
-- ============================================================

START TRANSACTION;

UPDATE accounts
SET balance = balance - 100
WHERE id = 1;

UPDATE accounts
SET balance = balance + 100
WHERE id = 3;

-- Undo both changes:
ROLLBACK;

SELECT * FROM accounts;


-- ============================================================
-- 9. SAVEPOINT PRACTICE
-- ============================================================

START TRANSACTION;

UPDATE accounts
SET balance = balance + 1000
WHERE id = 1;

SAVEPOINT after_wallet_topup;

UPDATE accounts
SET balance = balance + 10
WHERE id = 1;

-- Undo only the change made after the savepoint:
ROLLBACK TO after_wallet_topup;

COMMIT;

SELECT * FROM accounts;


-- ============================================================
-- 10. JOINS
-- ============================================================

-- JOINs are used to combine rows from two or more tables
-- based on a related column between them.
--
-- Types covered in the class:
-- 1. INNER JOIN
-- 2. LEFT JOIN
-- 3. RIGHT JOIN
-- 4. OUTER JOIN
-- 5. CROSS JOIN
-- 6. SELF JOIN


-- ============================================================
-- 11. INNER JOIN
-- ============================================================

-- General syntax:
--
-- SELECT column(s)
-- FROM tableA
-- INNER JOIN tableB
-- ON tableA.column_name = tableB.column_name;

SELECT
    c.customer_name,
    o.order_id,
    o.amount
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id;


-- ============================================================
-- 12. LEFT JOIN
-- ============================================================

-- General syntax:
--
-- SELECT column(s)
-- FROM tableA
-- LEFT JOIN tableB
-- ON tableA.column_name = tableB.column_name;

SELECT *
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id;


-- ============================================================
-- 13. RIGHT JOIN
-- ============================================================

-- General syntax:
--
-- SELECT column(s)
-- FROM tableA
-- RIGHT JOIN tableB
-- ON tableA.column_name = tableB.column_name;

SELECT *
FROM customers AS c
RIGHT JOIN orders AS o
    ON c.customer_id = o.customer_id;


-- ============================================================
-- 14. OUTER JOIN
-- ============================================================

-- The class notes show an OUTER JOIN as the combination of:
-- LEFT JOIN UNION RIGHT JOIN.
--
-- MySQL does not provide a direct FULL OUTER JOIN syntax,
-- so the class approach can be represented using UNION.

SELECT *
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id

UNION

SELECT *
FROM customers AS c
RIGHT JOIN orders AS o
    ON c.customer_id = o.customer_id;


-- ============================================================
-- 15. CROSS JOIN
-- ============================================================

-- A CROSS JOIN produces combinations between every row
-- of the first table and every row of the second table.

SELECT *
FROM customers AS c
CROSS JOIN orders AS o;


-- ============================================================
-- 16. SELF JOIN
-- ============================================================

-- A SELF JOIN is a regular JOIN in which a table is joined
-- with itself.

-- General syntax:
--
-- SELECT column(s)
-- FROM table AS a
-- JOIN table AS b
-- ON a.column_name = b.column_name;

-- Employee / manager example:
SELECT
    e1.first_name AS employee,
    e2.first_name AS manager
FROM employees AS e1
JOIN employees AS e2
    ON e1.manager_id = e2.employee_id;


-- ============================================================
-- 17. EXCLUSIVE JOINS
-- ============================================================

-- LEFT EXCLUSIVE JOIN:
-- Rows present in the left table but without a match
-- in the right table.

SELECT *
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL;


-- RIGHT EXCLUSIVE JOIN:
-- Rows present in the right table but without a match
-- in the left table.

SELECT *
FROM customers AS c
RIGHT JOIN orders AS o
    ON c.customer_id = o.customer_id
WHERE c.customer_id IS NULL;


-- ============================================================
-- 18. SUBQUERIES
-- ============================================================

-- A subquery (inner query / nested query) is a query
-- inside another SQL query.
--
-- It involves two SELECT statements.

-- General syntax:
--
-- SELECT column(s)
-- FROM table_name
-- WHERE col_name operator
-- (subquery);


-- ============================================================
-- 19. SUBQUERY WITH WHERE
-- ============================================================

-- Find orders whose amount is greater than the average
-- order amount.

SELECT *
FROM orders
WHERE amount > (
    SELECT AVG(amount)
    FROM orders
);


-- ============================================================
-- 20. SUBQUERY WITH SELECT
-- ============================================================

-- The class demonstrates a correlated subquery in the SELECT
-- list to count orders for each customer.

SELECT
    c.customer_name,
    (
        SELECT COUNT(*)
        FROM orders AS o
        WHERE o.customer_id = c.customer_id
    ) AS order_count
FROM customers AS c;


-- ============================================================
-- 21. SUBQUERY WITH FROM
-- ============================================================

-- A subquery can be used as a derived table in the FROM clause.

SELECT
    summary.customer_id,
    summary.avg_amount
FROM (
    SELECT
        customer_id,
        AVG(amount) AS avg_amount
    FROM orders
    GROUP BY customer_id
) AS summary;


-- ============================================================
-- 22. VIEWS IN SQL
-- ============================================================

-- A view is a virtual table based on the result-set
-- of an SQL statement.

-- General syntax:
--
-- CREATE VIEW view_name AS
-- SELECT col1, col2
-- FROM table_name;


-- Create a view:
CREATE OR REPLACE VIEW customer_orders AS
SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.amount
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id;


-- Query the view like a table:
SELECT *
FROM customer_orders;


-- A view can be used in SELECT, JOIN, and WHERE clauses
-- like a normal table.

-- Example:
SELECT *
FROM customer_orders
WHERE amount > 100;


-- Views show up-to-date data.
-- The database engine recreates the view result whenever
-- a user queries it.
--
-- The class notes also mention that data is not stored
-- physically unless it is a materialized view in databases
-- that support materialized views.
--
-- A view can include columns from one or more tables.
-- Views can help with security by exposing only selected
-- columns to users.


-- Drop the view when no longer needed:
DROP VIEW IF EXISTS customer_orders;


-- ============================================================
-- 23. INDEXES IN SQL
-- ============================================================

-- Indexes are special database objects that make
-- data retrieval faster.

-- ------------------------------------------------------------
-- Single-column index
-- ------------------------------------------------------------

CREATE INDEX idx_customer_city
ON customers(city);


-- ------------------------------------------------------------
-- Multi-column index
-- ------------------------------------------------------------

CREATE INDEX idx_customer_country_city
ON customers(country, city);


-- ------------------------------------------------------------
-- Show indexes
-- ------------------------------------------------------------

SHOW INDEX FROM customers;


-- ------------------------------------------------------------
-- Drop index
-- ------------------------------------------------------------

DROP INDEX idx_customer_city
ON customers;


-- ============================================================
-- 24. STORED PROCEDURES
-- ============================================================

-- A stored procedure is a predefined set of SQL statements
-- saved in the database and executed whenever needed.

-- General CREATE syntax:
--
-- CREATE PROCEDURE procedure_name(parameters)
-- BEGIN
--     SQL statements
-- END;


-- ------------------------------------------------------------
-- Stored procedure example from the class
-- ------------------------------------------------------------

DELIMITER $$

CREATE PROCEDURE check_balance(
    IN acc_id INT,
    OUT bal DECIMAL(10, 2)
)
BEGIN
    SELECT balance
    INTO bal
    FROM accounts
    WHERE id = acc_id;
END $$

DELIMITER ;


-- ------------------------------------------------------------
-- CALL stored procedure
-- ------------------------------------------------------------

CALL check_balance(2, @balance);

SELECT @balance;


-- ------------------------------------------------------------
-- DROP stored procedure
-- ------------------------------------------------------------

DROP PROCEDURE IF EXISTS check_balance;


-- ============================================================
-- 25. STORED PROCEDURE WITH AN INPUT PARAMETER
-- ============================================================

DELIMITER $$

CREATE PROCEDURE get_customer_orders(
    IN cust_id INT
)
BEGIN
    SELECT
        o.order_id,
        o.product,
        o.amount,
        o.order_date
    FROM orders AS o
    WHERE o.customer_id = cust_id;
END $$

DELIMITER ;


CALL get_customer_orders(1);

DROP PROCEDURE IF EXISTS get_customer_orders;
