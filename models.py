from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, ForeignKey, String, Integer, Boolean, Date, DateTime, BigInteger, Double

Base = declarative_base(name="Base")
metadata = Base.metadata

class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    lat = Column(Double(), nullable=False )
    lon = Column(Double(), nullable=False)
