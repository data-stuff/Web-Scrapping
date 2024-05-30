--- view my data
SELECT TOP 10 *
FROM GoogleCentro;

SELECT TOP 10 *
FROM GoogleSansa;

SELECT TOP 10 *
FROM TripAdvisor;

SELECT TOP 10 *
FROM ItaliaRicensioni;

--- Create a new table to combineall
CREATE TABLE RBReviews (
	Topics VARCHAR (250),
	Reviews Varchar (MAX)
);

--- Combining rows from all tables with explicit VARCHAR casting
--- And Inserting results into the new table
INSERT INTO RBReviews (Topics, Reviews)

SELECT CAST(Topic AS VARCHAR(250)) AS Topics, CAST(Review AS VARCHAR(MAX)) AS Reviews
FROM GoogleCentro

UNION ALL

SELECT CAST(Topic AS VARCHAR(250)) AS Topics, CAST(Review AS VARCHAR(MAX)) AS Reviews
FROM GoogleSansa

UNION ALL

SELECT CAST(Topic AS VARCHAR(250)) AS Topics, CAST(Review AS VARCHAR(MAX)) AS Reviews
FROM ItaliaRicensioni

UNION ALL

SELECT CAST(Topic AS VARCHAR(255)) AS Topics, CAST(Review AS VARCHAR(MAX)) AS Reviews
FROM TripAdvisor;

---Giving the new table a primary key
ALTER TABLE RBReviews
ADD RB_id INT IDENTITY (1,1) PRIMARY KEY;

--- see reviews of the new tabl 
SELECT 
    Reviews, 
    COUNT(*) AS ReviewCount
FROM 
    RBReviews
GROUP BY 
    Reviews;

-- View if duplicates in the RBReviews table
SELECT 
    Reviews, 
    COUNT(*) AS DuplicateCount
FROM 
    RBReviews
GROUP BY 
    Reviews;

--- check for empty reviews 
SELECT *
FROM RBReviews
WHERE TRIM(Reviews) = ''; --497 empty rows detected

--- delete the empty rows
DELETE FROM RBReviews
WHERE TRIM(Reviews) = '';

select RB_id, Topics, Reviews 
from RBReviews; 