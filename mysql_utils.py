import pymysql
from pymysql import cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Drones4dayz',
                             database='academicworld',
                             cursorclass=cursors.DictCursor)

with connection:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT COUNT(*) FROM faculty"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)