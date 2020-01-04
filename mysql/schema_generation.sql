drop table if exists CRIME;
drop table if exists INCARCERATION;
drop table if exists WEAPON;
drop table if exists VICTIM_OFFENDER;
drop table if exists PERSON;
drop table if exists LOCATION;


CREATE TABLE LOCATION(
State			VARCHAR(20),
City			VARCHAR(20),
PRIMARY KEY(State, City) );


-- creating relation for the PERSON entity as shown in EER diagram
CREATE TABLE PERSON(
Ssn VARCHAR(9),
Sex CHAR,
Race VARCHAR(15),
Firstname VARCHAR(15),
Lastname VARCHAR(15),
OffenderFlag Boolean,
VictimFlag Boolean,
PRIMARY KEY(Ssn));

-- creating relation for the VICTIM_OFFENDER entity as shown in EER diagram
CREATE TABLE VICTIM_OFFENDER(
SsnVictim VARCHAR(9),
SsnOffender	VARCHAR(9),
PRIMARY KEY(SsnVictim),
FOREIGN KEY(SsnVictim) REFERENCES PERSON(Ssn),
FOREIGN KEY(SsnOffender) REFERENCES PERSON(Ssn) );


-- creating relation for the WEAPON entity as shown in EER diagram
CREATE TABLE WEAPON(
Id INT,
Type VARCHAR(20),
PRIMARY KEY(Id) );


-- creating relation for the INCARCERATION entity as shown in EER diagram
CREATE TABLE INCARCERATION (
Id INT,
Jail_sentence	VARCHAR(20),
Jail_name VARCHAR(35),
PRIMARY KEY(Id) );

CREATE TABLE CRIME
(Id INT,
Year YEAR,
State VARCHAR(20),
City VARCHAR(20),
weapon_id INT,
incarceration_id INT,
committed_by VARCHAR(9),
committed_on VARCHAR(9),
PRIMARY KEY(Id),
FOREIGN KEY(State, City) REFERENCES LOCATION(State, City),
FOREIGN KEY(weapon_id) REFERENCES WEAPON(Id),
FOREIGN KEY(incarceration_id) REFERENCES INCARCERATION(Id),
FOREIGN KEY(committed_by) REFERENCES PERSON(Ssn),
FOREIGN KEY(committed_on) REFERENCES PERSON(Ssn));
