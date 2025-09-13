CREATE TABLE employees (
  id INT PRIMARY KEY,
  employee_name varchar(15),
  department varchar(10),
  salary INT
);

CREATE TABLE asset_type_master(
  id SERIAL PRIMARY KEY,
  asset_name VARCHAR(30) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE employee_assets_mapping(
  id SERIAL PRIMARY KEY,
  employees INT NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
  asset_type_master INT NOT NULL REFERENCES asset_type_master(id) ON DELETE CASCADE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO employees (id, employee_name, department, salary) 
VALUES 
(1, 'Clark', 'Sales', 34000), 
(2, 'Dave', 'Accounting', 41000), 
(3, 'Ava', 'Sales', 36000); 

SELECT * FROM employees;

INSERT INTO asset_type_master (id, asset_name, created_at, updated_at) 
VALUES 
(1, 'Laptop', NOW(), NOW()),
(2, 'Mobile Charger', NOW(), NOW()),
(3, 'Printer', NOW(), NOW());

INSERT into employee_assets_mapping (id, employees, asset_type_master, created_at, updated_at)
VALUES
(1, 1, 1, NOW(), NOW()),
(2, 1, 2, NOW(), NOW()),
(3, 1, 3, NOW(), NOW()),
(4, 2, 1, NOW(), NOW()),
(5, 2, 3, NOW(), NOW()),
(6, 3, 1, NOW(), NOW()),
(7, 3, 2, NOW(), NOW()),
(8, 3, 3, NOW(), NOW());

SELECT employee_name, department
FROM employees
JOIN employee_assets_mapping ON employees.id = employee_assets_mapping.employees
JOIN asset_type_master ON employee_assets_mapping.asset_type_master = asset_type_master.id 
WHERE asset_type_master.asset_name = 'Mobile Charger';
