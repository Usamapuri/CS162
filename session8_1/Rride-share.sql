  
.mode column
PRAGMA foreign_keys = ON; -- activates foreign key features in sqlite. It is disabled by default

CREATE TABLE Drivers (
    DRIVER_ID INTEGER PRIMARY KEY,
    NAME VARCHAR(20),
    PHONE VARCHAR(20),
    EMAIL VARCHAR(20)
);



CREATE TABLE Riders ( -- Info on the one riders
    RIDER_ID INTEGER PRIMARY KEY,
    NAME VARCHAR(20),
    PHONE VARCHAR(20),
    EMAIL VARCHAR(20)
);

CREATE TABLE Rides (
    RIDENUMBER INTEGER, -- A unique integer to identify this ride
    DRIVER_ID INTEGER,
    RIDER_ID INTEGER,
    BILL NUMERIC(11, 2), -- Bill for RIDERS for this ride
    FOREIGN KEY (DRIVER_ID) REFERENCES Drivers(DRIVER_ID),
    FOREIGN KEY (RIDER_ID) REFERENCES Lifters(RIDER_ID)
);

INSERT INTO Drivers VALUES (1, 'Robert', '123');
INSERT INTO Drivers VALUES (2, 'Mary', '12');
INSERT INTO Drivers VALUES (3, 'John', '23');


INSERT INTO Riders VALUES (1, 'A', '123');
INSERT INTO Riders VALUES (2, 'B', '123');
INSERT INTO Riders VALUES (3, 'C', '123');
INSERT INTO Riders VALUES (4, 'D', '132');

INSERT INTO Rides VALUES (1, 1, 2, 20);
INSERT INTO Rides VALUES (2, 1, 3, 10);
INSERT INTO Rides VALUES (3, 1, 3, 25);
INSERT INTO Rides VALUES (4, 2, 4, 13);
INSERT INTO Rides VALUES (5, 2, 3, 24);
INSERT INTO Rides VALUES (6, 2, 2, 7);
INSERT INTO Rides VALUES (7, 3, 2, 18);
INSERT INTO Rides VALUES (8, 3, 2, 32);
INSERT INTO Rides VALUES (9, 3, 2, 15);
INSERT INTO Rides VALUES (10, 3, 3, 2.5);

SELECT '1. how many trips have been made by each driver this month, and how much they will be paid.:';
SELECT '----------------------------------------------------';
/* They will be paid by 0.9 of the rides' worth*/
SELECT Drivers.NAME, COUNT(*) AS NUMBER_RIDES, 0.9*SUM(Rides.BILL) AS PAYMENT 
    FROM Rides
    JOIN Drivers ON Drivers.DRIVER_ID = Rides.DRIVER_ID
    GROUP BY Drivers.DRIVER_ID;

SELECT '';
SELECT '2. find all the riders who havmt taken any trips this month and their phone number';
SELECT '----------------------------------------------------';

SELECT * FROM Riders 
    LEFT OUTER JOIN Rides
    ON Riders.RIDER_ID = Rides.RIDER_ID
    GROUP BY Rides.RIDER_ID HAVING SUM(Rides.RIDER_ID) IS NULL;
