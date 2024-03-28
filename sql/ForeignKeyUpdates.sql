-- Primary Key Table: Age Categories
-- Existing Table: Positive
-- Connecting Keys AgeCategoryID in AgeCategories to Positive in AgeCategories
-- Based on Existing Data in the Positive Table
ALTER TABLE Positive
ADD AgeCategoryID int;

ALTER TABLE Positive
ADD CONSTRAINT FK_Positive_AgeCategories
FOREIGN KEY (AgeCategoryID) REFERENCES AgeCategories(AgeCategoryID);

UPDATE Positive
SET Positive.AgeCategoryID = AgeCategories.AgeCategoryID
FROM Positive, AgeCategories
WHERE Positive.AgeCategory = AgeCategories.AgeCategory;

-- After the AgeCategoryID has been matched inside Positive, safe to drop the column
ALTER TABLE Positive
DROP COLUMN AgeCategory;

-- Primary Key Table: AgeCategories
-- Existing Table: Vaccine
-- Connecting Keys AgeCategoryID in AgeCategories to Vaccine in AgeCategories
-- Based on Existing Data in the Vaccine Table
ALTER TABLE Vaccine
ADD AgeCategoryID int;

ALTER TABLE Vaccine
ADD CONSTRAINT FK_Vaccine_AgeCategories
FOREIGN KEY (AgeCategoryID) REFERENCES AgeCategories(AgeCategoryID);

UPDATE Vaccine
SET Vaccine.AgeCategoryID = AgeCategories.AgeCategoryID
FROM Vaccine, AgeCategories
WHERE Vaccine.AgeCategory = AgeCategories.AgeCategory;

-- After the AgeCategoryID has been matched inside Vaccine, safe to drop the column
ALTER TABLE Vaccine
DROP COLUMN AgeCategory;

-- Drop any row that is not an adult in the Vaccine list
-- Referring to "COVID-19 vaccine data (ONLY adults but age-wise)" in the Specification
DELETE FROM Vaccine
WHERE AgeCategoryID IN (SELECT AgeCategoryID FROM AgeCategories WHERE Adult = 0);

-- Primary Key Table: AgeCategories
-- Existing Table: Patient
-- Connecting Keys AgeCategoryID in AgeCategories to Patient in AgeCategories
ALTER TABLE Patient
ADD AgeCategoryID int;

ALTER TABLE Patient
ADD CONSTRAINT FK_Patient_AgeCategories
FOREIGN KEY (AgeCategoryID) REFERENCES AgeCategories(AgeCategoryID);

-- Primary Key Table: Vaccine
-- Existing Table: Patient
-- Connecting Keys VaccineID in Vaccine to Patient in Vaccine
ALTER TABLE Patient
ADD VaccineID int;

ALTER TABLE Patient
ADD CONSTRAINT FK_Patient_Vaccine
FOREIGN KEY (VaccineID) REFERENCES Vaccine(VaccineID);

-- Primary Key Table: Testing
-- Existing Table: Patient
-- Connecting Keys TestID in Testing to Patient
ALTER TABLE Patient
ADD TestID int;

ALTER TABLE Patient
ADD CONSTRAINT FK_Patient_Testing
FOREIGN KEY (TestID) REFERENCES Testing(TestID);

-- Primary Key Table: Hospitalization
-- Existing Table: Patient
-- Connecting Keys HospitalizationID in Hospitalization to Patient
ALTER TABLE Patient
ADD HospitalizationID int;

ALTER TABLE Patient
ADD CONSTRAINT FK_Patient_Hospitalization
FOREIGN KEY (HospitalizationID) REFERENCES Hospitalization(HospitalizationID);

-- Primary Key Table: Hospital
-- Existing Table: Hospitalization
-- Connecting Keys HospitalID in Hospital to Hospitalization
ALTER TABLE Hospitalization
ADD CONSTRAINT FK_Patient_Hospital
FOREIGN KEY (HospitalID) REFERENCES Hospital(HospitalID);