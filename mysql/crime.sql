drop table if exists CRIME;
drop table if exists INCARCERATION;
drop table if exists WEAPON;
drop table if exists OFFENDER;
drop table if exists VICTIM;
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

-- creating relation for the VICTIM entity as shown in EER diagram
CREATE TABLE VICTIM(
SsnVictim VARCHAR(9),
SsnOffender	VARCHAR(9),
PRIMARY KEY(SsnVictim),
FOREIGN KEY(SsnVictim) REFERENCES PERSON(Ssn),
FOREIGN KEY(SsnOffender) REFERENCES PERSON(Ssn) );


-- creating relation for the OFFENDER entity as shown in EER diagram.

CREATE TABLE OFFENDER(
SsnOffender VARCHAR(9),
SsnVictim	VARCHAR(9),
PRIMARY KEY(SsnOffender),
FOREIGN KEY(SsnOffender) REFERENCES PERSON(Ssn),
FOREIGN KEY(SsnVictim) REFERENCES PERSON(Ssn) );


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

insert into LOCATION values ('Montana', 'Bozeman');
insert into LOCATION values ('Montana', 'Missoula');
insert into LOCATION values ('Montana', 'Billings');
insert into LOCATION values ('Montana', 'Kallispel');
insert into LOCATION values ('Montana', 'Great Falls');
insert into LOCATION values ('Montana', 'Laurel');
insert into LOCATION values ('Montana', 'Whitefish');
insert into LOCATION values ('Montana', 'Miles City');


insert into PERSON values (000000001, 'M', 'Asian', 'Jack', 'Wong', FALSE, TRUE);
insert into PERSON values (000000002, 'M', 'Caucasian', 'Joe', 'Bennit', TRUE, FALSE);
insert into PERSON values (000000003, 'M', 'African', 'Andrew', 'Jackson', FALSE, TRUE);
insert into PERSON values (000000004, 'F', 'Native', 'Ashley', 'DeHart', TRUE, FALSE);
insert into PERSON values (000000005, 'F', 'Asian', 'Charlie', 'Mason', FALSE, TRUE);
insert into PERSON values (000000006, 'M', 'Caucasian', 'Frank', 'Larson', TRUE, FALSE);
insert into PERSON values (000000007, 'M', 'Asian', 'Charlie', 'Mason', FALSE, TRUE);
insert into PERSON values (000000008, 'M', 'African', 'Eli', 'Humphrey', TRUE, FALSE);
insert into PERSON values (000000009, 'M', 'Native', 'Matt', 'Fowler', FALSE, TRUE);
insert into PERSON values (000000010, 'F', 'Caucasian', 'Jessie', 'Day', TRUE, FALSE);
insert into PERSON values (000000011, 'M', 'Asian', 'Joe', 'Chan', FALSE, TRUE);
insert into PERSON values (000000012, 'M', 'Caucasian', 'Drew', 'Phillips', TRUE, FALSE);
insert into PERSON values (000000013, 'M', 'Unknown', 'Michael', 'Mitchell', FALSE, TRUE);
insert into PERSON values (000000014, 'M', 'African', 'Kai', 'Gunn', TRUE, FALSE);
insert into PERSON values (000000015, 'M', 'Caucasian', 'Tim', 'Donald', FALSE, TRUE);
insert into PERSON values (000000016, 'F', 'Unknown', 'Miranda', 'DeCrea', TRUE, FALSE);
insert into PERSON values (000000017, 'M', 'Asian', 'Blake', 'Franco', FALSE, TRUE);
insert into PERSON values (000000018, 'M', 'African', 'DeAndre', 'Tomlinson', TRUE, FALSE);
insert into PERSON values (000000019, 'F', 'Caucasian', 'Riley', 'DeCrea', FALSE, TRUE);
insert into PERSON values (000000020, 'M', 'Native', 'Carver', 'Sun', TRUE, FALSE);


insert into VICTIM values(000000001,000000002);
insert into VICTIM values(000000003,000000004);
insert into VICTIM values(000000005,000000006);
insert into VICTIM values(000000007,000000008);
insert into VICTIM values(000000009,000000010);
insert into VICTIM values(000000011,000000012);
insert into VICTIM values(000000013,000000014);
insert into VICTIM values(000000015,000000016);
insert into VICTIM values(000000017,000000018);
insert into VICTIM values(000000019,000000020);


insert into OFFENDER values(000000020,000000019);
insert into OFFENDER values(000000018,000000017);
insert into OFFENDER values(000000016,000000015);
insert into OFFENDER values(000000014,000000013);
insert into OFFENDER values(000000012,000000011);
insert into OFFENDER values(000000010,000000009);
insert into OFFENDER values(000000008,000000007);
insert into OFFENDER values(000000006,000000005);
insert into OFFENDER values(000000004,000000003);
insert into OFFENDER values(000000002,000000001);

insert into WEAPON values(1, "Handgun");
insert into WEAPON values(2, "Rifle");
insert into WEAPON values(3, "Knife");
insert into WEAPON values(4, "Explosives");
insert into WEAPON values(5, "Vehicle");
insert into WEAPON values(6, "Gasoline");
insert into WEAPON values(7, "Blunt_object");
insert into WEAPON values(8, "Tazer");
insert into WEAPON values(9, "Poison");
insert into WEAPON values(10, "Whip");

insert into INCARCERATION values(1, '6 Months', 'Fox River');
insert into INCARCERATION values(2, '2 Years', 'Salt Lake');
insert into INCARCERATION values(3, '2 Months', 'Chicago Pen.');
insert into INCARCERATION values(4, '5 Years', 'Texas State');
insert into INCARCERATION values(5, 'Life', 'New York State');
insert into INCARCERATION values(6, 'Life', 'Overlook Penitentiary');
insert into INCARCERATION values(7, '1 Year', 'Azkaban');
insert into INCARCERATION values(8, '15 Years', 'Boomsby');
insert into INCARCERATION values(9, 'Life', 'Erewhon');
insert into INCARCERATION values(10, '55 Years', 'Chicago Pen');

insert into CRIME values(1, 2016, 'Montana', 'Bozeman', 1, 1, 000000002, 000000001);
insert into CRIME values(2, 2018, 'Montana', 'Billings', 2, 2, 000000004, 000000003);
insert into CRIME values(3, 2019, 'Montana', 'Missoula', 3, 3, 000000006, 000000005);
insert into CRIME values(4, 2014, 'Montana', 'Kallispel', 4, 4, 000000008, 000000007);
insert into CRIME values(5, 2012, 'Montana', 'Great Falls', 5, 5, 000000010, 000000009);
insert into CRIME values(6, 2017, 'Montana', 'Billings', 6, 6, 000000012, 000000011);
insert into CRIME values(7, 2009, 'Montana', 'Whitefish', 7, 7, 000000014, 000000013);
insert into CRIME values(8, 2012, 'Montana', 'Billings', 8, 8, 000000016, 000000015);
insert into CRIME values(9, 2018, 'Montana', 'Billings', 9, 9, 000000018, 000000017);
insert into CRIME values(10, 2019, 'Montana', 'Laurel', 10, 9, 000000020, 000000019);
insert into CRIME values(11, 2016, 'Montana', 'Bozeman', 3, 10, 000000006, 000000003);
insert into CRIME values(12, 2019, 'Montana', 'Miles City', 10, 9, 000000020, 000000019);
