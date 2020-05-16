CREATE DATABASE speedData;
use speedData;

CREATE TABLE IF NOT EXISTS tblSpeedData (
    `id` INT AUTO_INCREMENT,
    `fldTheft_year` INT,
    `fldVeh_model` VARCHAR(50),
    `fldVehicle_number_of_thefts` float
    PRIMARY KEY

);
INSERT INTO tblSpeedData VALUES

    (1,2015,'Nissan Altima',1.104),
    (2,2015,'Chrysler',1.069),
    (3,2015,'Toyota Camry',923),
    (4,2015,'Toyota Corolla',776),
    (5,2015,'GMC Sierra',670),
    (6,2015,'Dodge Charger',666),
    (7,2015,'Hyundai Sonata',632),
    (8,2015,'Chevrolet Malibu',629),
    (9,2015,'Chevrolet Impala',594),
    (10,2015,'Chevrolet Cruze',586),
    (11,2015,'Nissan Versa',549),
    (12,2015,'Ford Fusion',488),
    (13,2015,'Hyundai Elantra',475),
    (14,2015,'Chevrolet Camaro',461),
    (15,2015,'Kia Motors Corporation Optima',461),
    (16,2015,'Jeep Cherokee/Grand Cherokee',450),
    (17,2015,'Honda Civic',388),
    (18,2015,'Ford Transit',385),
    (19,2015,'Nissan Sentra',383),
    (20,2015,'Chevrolet Silverado',381),
    (21,2015,'Dodge Dart',358),
    (22,2015,'Honda Accord',350),
    (23,2015,'Ford Focus',345),
    (24,2015,'Ford Mustang',329),
    (25,2015,'Chevrolet Tahoe',319);
