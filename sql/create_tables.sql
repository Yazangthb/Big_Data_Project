-- Optional
-- but it is useful if you want to not commit the change when some errors happened before the commit statement
START TRANSACTION;

DROP TABLE IF EXISTS emps CASCADE;
DROP TABLE IF EXISTS depts CASCADE;

-- Add tables
-- emps table
CREATE TABLE IF NOT EXISTS emps (
    empno integer NOT NULL PRIMARY KEY,
    ename VARCHAR(50) NOT NULL,
    job VARCHAR(50) NOT NULL,
    mgr integer,
    hiredate date,
    sal decimal(10, 2),
    comm decimal(10, 2),
    deptno integer NOT NULL
);

-- dept table
CREATE TABLE IF NOT EXISTS depts(
    deptno integer NOT NULL PRIMARY KEY,
    dname varchar(50) NOT NULL,
    location varchar(50) NOT NULL
);

-- Add constraints
-- FKs
ALTER TABLE emps DROP CONSTRAINT IF EXISTS fk_emps_mgr_empno;

ALTER TABLE emps ADD CONSTRAINT fk_emps_mgr_empno FOREIGN KEY(mgr) REFERENCES emps (empno);

ALTER TABLE emps DROP CONSTRAINT IF EXISTS fk_emps_deptno_deptno;

ALTER TABLE emps ADD CONSTRAINT fk_emps_deptno_deptno FOREIGN KEY(deptno) REFERENCES depts (deptno);

-- This is related to how the date types are stored in my dataset
ALTER DATABASE team17_projectdb SET datestyle TO iso, ymd;

COMMIT;