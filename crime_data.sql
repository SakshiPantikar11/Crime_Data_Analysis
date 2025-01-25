
SELECT COUNT(*) FROM crime_data_analysis.crime_data;

SELECT COUNT(DISTINCT 'AREA_NAME', 'Crm_Cd_Desc', 'Vict_Sex', 'Status') FROM crime_data_analysis.crime_data;

SELECT Vict_Sex, COUNT(*) 
FROM crime_data_analysis.crime_data
WHERE Vict_Sex IS NOT NULL
GROUP BY Vict_Sex

#Crime Hotspots
SELECT LAT, LON FROM crime_data_analysis.crime_data;

#Victim Age Distribution
SELECT Vict_Age, COUNT(*) AS Age_Count
                            FROM crime_data_analysis.crime_data
                            WHERE Vict_Age IS NOT NULL
                            GROUP BY Vict_Age
                            ORDER BY Vict_Age;
                            
#Victim Gender Distribution
SELECT Vict_Sex, COUNT(*) AS Gender_Count
                            FROM crime_data_analysis.crime_data
                            WHERE Vict_Sex IS NOT NULL
                            GROUP BY Vict_Sex;

#Status of Reported Crimes:
SELECT Status, COUNT(*) AS Crime_Count
                FROM crime_data_analysis.crime_data
                GROUP BY Status;