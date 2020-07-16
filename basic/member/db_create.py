import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='qwer1234',
    db='test',
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
    )

try:
    # with connection.cursor() as cursor:
    #     sql='''
    #         create table if not exists users(
    #             userid varchar(20) PRIMARY KEY,
    #             userpw varchar(20) not null,
    #             username varchar(20) not null,
    #             userage int,
    #             usermail varchar(20),
    #             useradd varchar(50),
    #             usergender varchar(20),
    #             usertel varchar(20)
    #         )DEFAULT CHARSET=utf8
    #     '''
    #     cursor.execute(sql)
    #     connection.commit()

    with connection.cursor() as cursor:
        sql='''
            insert into users values(
                'gildong4','qwer1234','길동',
                '33','asdf1234@naver.com',
                '부산시 남구','male',
                '010-1234-5678')
        '''
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        sql='''
            select * from users;
        '''
        cursor.execute(sql)
        a = cursor.fetchall()
        print(a)

finally:
    connection.close()