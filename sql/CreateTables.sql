CREATE TABLE Hospital(
	HospitalID int NOT NULL IDENTITY(1, 1),
	Date date NOT NULL,
	Region nvarchar(50) NOT NULL,
	ICUCurrent int NOT NULL,
	ICUCurrentVented int NOT NULL,
	Hospitalizations int NOT NULL,
	PRIMARY KEY(HospitalID)
);

CREATE TABLE Positive(
	PositiveID int NOT NULL IDENTITY(1, 1),
	Date date NOT NULL,
	AgeCategory nchar(50) NOT NULL,
	PercentPositive7d float NOT NULL,
	PRIMARY KEY(PositiveID)
);

CREATE TABLE Testing(
	TestID int NOT NULL IDENTITY(1, 1),
	Date date NOT NULL,
	PHUNum int NOT NULL,
	PHUName nvarchar(100) NOT NULL,
	PercentPositive7d float NOT NULL,
	PercentTest7d float NOT NULL,
	PRIMARY KEY(TestID)
);

CREATE TABLE Vaccine(
	VaccineID int NOT NULL IDENTITY(1, 1),
	Date date NOT NULL,
	AgeCategory nvarchar(50) NOT NULL,
	UnVaxRate100k float,
	PartialVaxRate100k float,
	NotFullVaxRate100k float,
	FullVaxRate100k float,
	BoostVaxRate100k float,
	UnVaxRate7ma float,
	PartialVaxRate7ma float,
	NotFullVaxRate7ma float,
	FullVaxRate7ma float,
	BoostVaxRate7ma float,
	PRIMARY KEY(VaccineID)
);

CREATE TABLE AgeCategories(
	AgeCategoryID int NOT NULL IDENTITY(1, 1),
	AgeCategory nvarchar(50) NOT NULL,
	Adult bit NOT NULL,
	PRIMARY KEY(AgeCategoryID)
);

CREATE TABLE Patient(
	PatientID int NOT NULL IDENTITY(1, 1),
	FName nvarchar(50) NOT NULL,
	LName nvarchar(50) NOT NULL,
	Gender char(2), -- Including M/F/NB/NULL
	PRIMARY KEY(PatientID)
);

CREATE TABLE Hospitalization(
    HospitalizationID int NOT NULL IDENTITY(1, 1),
    StartDate date NOT NULL,
    EndDate date,
    HospitalID int NOT NULL,
    PRIMARY KEY(HospitalizationID)
);

-- The Patient table will have Identification numbers based on the four other tables
-- These foreign keys will reference when a Patient got a vaccine/positive/hospitalized
-- None will be mandatory, but will make it easy to get data from the day they had certain events happen (if they have)
-- These are added with a Foreign Key Constraint within the other SQL file.
