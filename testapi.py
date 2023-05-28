#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Location
from models import Base
from sqlalchemy import func, text

def make_session():
    engine = create_engine(f"sqlite:///./bicycleshops.db", echo=False)
    dbsession = scoped_session(sessionmaker(bind=engine))
    Base.metadata.create_all(engine)
    return dbsession()

#from geoalchemy2.comparator import Comparator
session = make_session()
lat=52.21395053208327
lon=6.89347062803371 
q = session.execute(text(f"SELECT *, SQRT(POW((69.1 * (lat - {lat})) , 2 ) + POW((53 * (lon - {lon})), 2)) AS distance FROM locations ORDER BY distance ASC LIMIT 1;"))

print(q.fetchone())
#print(q.lat, q.lon)
