from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root@localhost:3306/python_ludycom")

meta = MetaData()

conn = engine.connect()