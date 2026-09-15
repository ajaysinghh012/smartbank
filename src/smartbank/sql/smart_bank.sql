DROP TABLE IF EXISTS transaction;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS account;
DROP TABLE IF EXISTS Atm;
DROP TABLE IF EXISTS Branch;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS Bank;


CREATE TABLE Bank(
    code varchar(50) PRIMARY KEY,
    name TEXT NOT NULL,
    address VARCHAR(50) NOT NULL
);

INSERT INTO Bank VALUES ('ICICI1', 'ICICI', 'Sonha,Gurugram');
INSERT INTO Bank VALUES ('HDFC2', 'HDFC', 'Greater Noida');
INSERT INTO Bank VALUES ('PNB3', 'PUNJAB NATIONAL BANK', 'MATHURA');

SELECT * FROM Bank;


CREATE TABLE department(
    id int PRIMARY KEY,
    code varchar(10) NOT NULL,
    name TEXT NOT NULL,
    bank_code varchar(50) NOT NULL,
    CONSTRAINT fk_department_bank
        FOREIGN KEY (bank_code)
        REFERENCES Bank(code)
);


INSERT INTO department (id, code, name, bank_code) VALUES (1, 'LN', 'Loan', 'ICICI1');
INSERT INTO department (id, code, name, bank_code) VALUES (2, 'CS', 'Corporate Services', 'ICICI1');
INSERT INTO department (id, code, name, bank_code) VALUES (3, 'LN', 'Loan', 'HDFC2');
INSERT INTO department (id, code, name, bank_code) VALUES (4, 'CP', 'Corporate Services', 'HDFC2');
INSERT INTO department (id, code, name, bank_code) VALUES (5, 'LN', 'Loan', 'PNB3');
INSERT INTO department (id, code, name, bank_code) VALUES (6, 'CP', 'Corporate Services', 'PNB3');

SELECT * FROM department;


CREATE TABLE Branch(
    code varchar(10) PRIMARY KEY,
    address varchar(50) NOT NULL,
    bank_code varchar(50) NOT NULL,
    CONSTRAINT fk_branch_bank
        FOREIGN KEY (bank_code)
        REFERENCES Bank(code)
);


INSERT INTO Branch VALUES ('ICICI001', 'BLOCK C, ALPHA - 1, GREATER NOIDA', 'ICICI1');
INSERT INTO Branch VALUES ('ICICI002', 'BLOCK D, ALPHA - 2, GREATER NOIDA', 'ICICI1');
INSERT INTO Branch VALUES ('HDFC001', 'BLOCK C, ALPHA - 1, GREATER NOIDA', 'HDFC2');
INSERT INTO Branch VALUES ('HDFC002', 'BLOCK D, ALPHA - 2, GREATER NOIDA', 'HDFC2');
INSERT INTO Branch VALUES ('PNB001', 'BLOCK C, ALPHA - 1, GREATER NOIDA', 'PNB3');
INSERT INTO Branch VALUES ('PNB002', 'BLOCK D, ALPHA - 2, GREATER NOIDA', 'PNB3');


CREATE TABLE Atm (
    code varchar(50) PRIMARY KEY,
    location VARCHAR(100) NOT NULL,
    balance INT NOT NULL,
    bank_code varchar(50) NOT NULL,
    CONSTRAINT fk_atm_bank
        FOREIGN KEY (bank_code)
        REFERENCES Bank(code)
);


INSERT INTO Atm VALUES ('1', 'ALPHA - 1', 10000000, 'ICICI1');
INSERT INTO Atm VALUES ('2', 'SURAJPUR', 500000, 'ICICI1');
INSERT INTO Atm VALUES ('3', 'ALPHA - 1', 10000000, 'HDFC2');
INSERT INTO Atm VALUES ('4', 'SURAJPUR', 500000, 'HDFC2');
INSERT INTO Atm VALUES ('5', 'ALPHA - 1', 10000000, 'PNB3');
INSERT INTO Atm VALUES ('6', 'SURAJPUR', 500000, 'PNB3');

SELECT * FROM Atm;


CREATE TABLE account(
    account_no int PRIMARY KEY,
    owner text NOT NULL,
    email varchar(50) NOT NULL,
    phone_no BIGINT NOT NULL,
    aadhaar_no BIGINT NOT NULL,
    branch_code varchar(10) NOT NULL,
    bank_code VARCHAR(50) NOT NULL,
    CONSTRAINT fk_account_branch
        FOREIGN KEY (branch_code)
        REFERENCES Branch(code),
    CONSTRAINT fk_account_bank
        FOREIGN KEY (bank_code)
        REFERENCES Bank(code)
);


INSERT INTO account VALUES (100001, 'Rahul Sharma', 'rahul.sharma@gmail.com', 9876543210, 234567890123, 'ICICI001', 'ICICI1');
INSERT INTO account VALUES (100002, 'Priya Verma', 'priya.verma@gmail.com', 9123456780, 345678901234, 'HDFC001', 'HDFC2');
INSERT INTO account VALUES (100003, 'Amit Kumar', 'amit.kumar@gmail.com', 9988776655, 456789012345, 'PNB001', 'PNB3');
INSERT INTO account VALUES (100004, 'Sneha Reddy', 'sneha.reddy@gmail.com', 9001234567, 567890123456, 'ICICI002', 'ICICI1');
INSERT INTO account VALUES (100005, 'Vikram Singh', 'vikram.singh@gmail.com', 9812345670, 678901234567, 'HDFC001', 'HDFC2');
INSERT INTO account VALUES (100006, 'Anjali Mehta', 'anjali.mehta@gmail.com', 9765432108, 789012345678, 'PNB001', 'PNB3');
INSERT INTO account VALUES (100007, 'Rohit Yadav', 'rohit.yadav@gmail.com', 9654321087, 890123456789, 'ICICI001', 'ICICI1');
INSERT INTO account VALUES (100008, 'Kavita Joshi', 'kavita.joshi@gmail.com', 9543210876, 901234567890, 'HDFC002', 'HDFC2');
INSERT INTO account VALUES (100009, 'Manoj Tiwari', 'manoj.tiwari@gmail.com', 9432108765, 112233445566, 'PNB002', 'PNB3');
INSERT INTO account VALUES (100010, 'Neha Kapoor', 'neha.kapoor@gmail.com', 9321087654, 223344556677, 'ICICI001', 'ICICI1');

SELECT * FROM account;


CREATE TABLE customer(
    id text PRIMARY KEY,
    name text NOT NULL,
    phone_no BIGINT NOT NULL,
    mail varchar(50),
    account_no bigint NOT NULL UNIQUE,
    bank_code varchar(50) NOT NULL,   -- fixed: was int, now matches Bank.code type
    CONSTRAINT fk_customer_account
        FOREIGN KEY (account_no)
        REFERENCES account(account_no),
    CONSTRAINT fk_customer_bank
        FOREIGN KEY (bank_code)
        REFERENCES Bank(code)
);


INSERT INTO customer VALUES ('CUST001', 'Rahul Sharma', 9876543210, 'rahul.sharma@gmail.com', 100001, 'ICICI1');
INSERT INTO customer VALUES ('CUST002', 'Priya Verma', 9123456780, 'priya.verma@gmail.com', 100002, 'HDFC2');
INSERT INTO customer VALUES ('CUST003', 'Amit Kumar', 9988776655, 'amit.kumar@gmail.com', 100003, 'PNB3');
INSERT INTO customer VALUES ('CUST004', 'Sneha Reddy', 9001234567, 'sneha.reddy@gmail.com', 100004, 'ICICI1');
INSERT INTO customer VALUES ('CUST005', 'Vikram Singh', 9812345670, 'vikram.singh@gmail.com', 100005, 'HDFC2');
INSERT INTO customer VALUES ('CUST006', 'Anjali Mehta', 9765432108, 'anjali.mehta@gmail.com', 100006, 'PNB3');
INSERT INTO customer VALUES ('CUST007', 'Rohit Yadav', 9654321087, 'rohit.yadav@gmail.com', 100007, 'ICICI1');
INSERT INTO customer VALUES ('CUST008', 'Kavita Joshi', 9543210876, 'kavita.joshi@gmail.com', 100008, 'HDFC2');
INSERT INTO customer VALUES ('CUST009', 'Manoj Tiwari', 9432108765, 'manoj.tiwari@gmail.com', 100009, 'PNB3');
INSERT INTO customer VALUES ('CUST010', 'Neha Kapoor', 9321087654, 'neha.kapoor@gmail.com', 100010, 'ICICI1');

SELECT * FROM customer;


CREATE TABLE transaction (
    transaction_id INT PRIMARY KEY,
    money INT NOT NULL,
    account_no INT NOT NULL,
    txn_type VARCHAR(20) NOT NULL CHECK (txn_type IN ('sent', 'received')),
    counterparty_account INT NOT NULL,
    CONSTRAINT fk_txn_account
        FOREIGN KEY (account_no) 
		REFERENCES account(account_no),
    CONSTRAINT fk_txn_counterparty
        FOREIGN KEY (counterparty_account) 
		REFERENCES account(account_no)
);

INSERT INTO transaction (transaction_id, money, account_no, txn_type, counterparty_account) VALUES
(1, 5000, 100001, 'sent', 100002),
(2, 5000, 100002, 'received', 100001),

(3, 2000, 100003, 'sent', 100001),
(4, 2000, 100001, 'received', 100003),

(5, 15000, 100002, 'sent', 100005),
(6, 15000, 100005, 'received', 100002),

(7, 750, 100004, 'sent', 100003),
(8, 750, 100003, 'received', 100004),

(9, 30000, 100005, 'sent', 100006),
(10, 30000, 100006, 'received', 100005);


select * from transaction where txn_type = 'sent';
select * from transaction where txn_type = 'received';