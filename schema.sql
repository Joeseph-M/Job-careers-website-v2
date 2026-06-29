CREATE DATABASE if NOT EXISTS careers_db;
USE careers_db;

DROP TABLE IF EXISTS jobs;

CREATE TABLE jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(60) NOT NULL,
    location VARCHAR(100) NOT NULL,
    salary INT,
    currency VARCHAR(10),
    responsibilities VARCHAR(4000),
    requirements VARCHAR(2000)
);

INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements) 
VALUES
('Data Analyst','Singapore', 3500, 'SGD', 'Analyse business data', 'SQL, Python, Excel'),
('Data Scientist','Singapore',7500, 'SGD', 'Build pipelines and train staff', 'SQL, Python, Excel'),
('Backend Engineer','USA',6500, 'SGD', 'Review backend setup', 'SQL, Python,'),
('Data Engineer','Remote',5500, 'SGD', 'Migrate database to AWS', 'SQL, Python, Excel');

