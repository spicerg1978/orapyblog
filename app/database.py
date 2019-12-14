from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('mysql://microblog/microbl0g@localhost:3306/microblog', convert_unicode=True)
metadata = MetaData(bind=engine)

#users = Table('user', metadata, autoload=True)
#con = engine.connect()
#con.execute(users.select(user.c.id == 1).execute().first())
engine.execute('select * from user').first()


