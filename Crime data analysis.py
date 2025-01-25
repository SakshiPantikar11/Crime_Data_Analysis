import pymysql

# Connect to the database
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='pass1234',
    database='crime_data_analysis'
)

print("\nConnected to database successfully!")


import pymysql

try:
    # Establish a connection to the MySQL database
    conn = pymysql.connect(host='127.0.0.1',
    user='root',
    password='pass1234',
    database='crime_data_analysis')
    # Execute SQL queries to retrieve basic statistics
    cursor = conn.cursor()

    # Total number of records in the dataset
    query_total_records = "SELECT COUNT(*) FROM crime_data;"
    cursor.execute(query_total_records)
    total_records = cursor.fetchone()[0]
    print("\nTotal number of records:", total_records)
    print()
    # Unique values in specific columns
    columns_to_analyze = ['AREA_NAME', 'Crm_Cd_Desc', 'Vict_Sex', 'Status']  # Add more columns as needed
    for column in columns_to_analyze:
        query_unique_values = f"SELECT COUNT(DISTINCT {column}) FROM crime_data;"
        cursor.execute(query_unique_values)
        unique_values_count = cursor.fetchone()[0]
        print(f"Number of unique values in {column}: {unique_values_count}")

    # Close cursor and connection
    cursor.close()
    conn.close()

except pymysql.Error as e:
    print("Error:", e)


import pymysql
import matplotlib.pyplot as plt
try:
            # Establish a connection to the MySQL database
            conn = pymysql.connect(host='127.0.0.1',
    user='root',
    password='pass1234',
    database='crime_data_analysis')

            # Execute SQL query to retrieve latitude and longitude information
            cursor = conn.cursor()
            query = """
            SELECT LAT, LON FROM crime_data;
            """
            cursor.execute(query)
            results = cursor.fetchall()

            # Extract latitude and longitude data from results
            latitudes = [result[0] for result in results if result[0] is not None]
            longitudes = [result[1] for result in results if result[1] is not None]

            # Close cursor and connection
            cursor.close()
            conn.close()

            # Plotting crime hotspots on a map
            plt.figure(figsize=(10, 8))
            plt.scatter(longitudes, latitudes, s=10, alpha=0.5)
            plt.title('Crime Hotspots')
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            plt.grid(True)
            plt.tight_layout()
            plt.show()

except pymysql.Error as e:
            print("Error:", e)


import pymysql
import matplotlib.pyplot as plt

try:
    # Establish a connection to the MySQL database
    conn = pymysql.connect(host='127.0.0.1',
                                       user='root',
                                       password='pass1234',
                                       database='crime_data_analysis')

    # Execute SQL query to investigate the distribution of victim ages
    cursor = conn.cursor()
    age_query = """
                            SELECT Vict_Age, COUNT(*) AS Age_Count
                            FROM crime_data
                            WHERE Vict_Age IS NOT NULL
                            GROUP BY Vict_Age
                            ORDER BY Vict_Age;
                            """
    cursor.execute(age_query)
    age_results = cursor.fetchall()

    # Extract age data from results
    ages = [result[0] for result in age_results]
    age_counts = [result[1] for result in age_results]

    # Plotting victim age distribution
    plt.figure(figsize=(10, 6))
    plt.bar(ages, age_counts, color='skyblue')
    plt.title('Victim Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Execute SQL query to investigate the distribution of victim genders
    gender_query = """
                                SELECT Vict_Sex, COUNT(*) AS Gender_Count
                                FROM crime_data
                                WHERE Vict_Sex IS NOT NULL
                                GROUP BY Vict_Sex;
                            """
    cursor.execute(gender_query)
    gender_results = cursor.fetchall()

    # Extract gender data from results
    genders = [result[0] for result in gender_results]
    gender_counts = [result[1] for result in gender_results]

    # Plotting victim gender distribution
    plt.figure(figsize=(6, 6))
    plt.pie(gender_counts, labels=genders, autopct='%1.1f%%', startangle=140,
            colors=['lightcoral', 'lightskyblue'])
    plt.title('Victim Gender Distribution')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

    # Close cursor and connection
    cursor.close()
    conn.close()

except pymysql.Error as e:
    print("Error:", e)


import pymysql

try:
                # Establish a connection to the MySQL database
                conn = pymysql.connect(host='127.0.0.1',
                                       user='root',
                                       password='pass1234',
                                       database='crime_data_analysis')

                # Execute SQL query to examine the status of reported crimes
                cursor = conn.cursor()
                status_query = """
                SELECT Status, COUNT(*) AS Crime_Count
                FROM crime_data
                GROUP BY Status;
                """
                cursor.execute(status_query)
                status_results = cursor.fetchall()

                # Print out the status of reported crimes and their counts
                print("\nStatus of Reported Crimes:")
                for status, count in status_results:
                    print(f"{status}: {count}")

                # Close cursor and connection
                cursor.close()
                conn.close()

except pymysql.Error as e:
                print("Error:", e)
