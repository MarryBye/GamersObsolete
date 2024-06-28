import psycopg2 as psql

conn = psql.connect(
    database="gmrs_site",
    user="postgres",
    password="58231",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

cursor.execute(
    ''' 
    INSERT INTO users(user_login, user_password, user_email) 
    VALUES (%s, %s, %s) 
    ''', ("Aboba_1488", "773hH98h*837h", "aboba@gmail.com")
)

cursor.execute(
    '''
    SELECT * FROM users
    '''
)

data = cursor.fetchall()
print(data)
iddd = data[0]

cursor.execute(
    '''
    SELECT add_admin(22)
    ''', (iddd)
)

cursor.execute(
    '''
        SELECT check_is_admin(22)               
    ''', (iddd)
)
print(cursor.fetchall())

conn.commit()
