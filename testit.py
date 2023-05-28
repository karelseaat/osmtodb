#!/usr/bin/env python

import osmium
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Location
from models import Base
import sys, getopt, os

#filename = "bicycleshops"
#selector = "shop.bicycle"

def arguments(argv):
   opts, args = getopt.getopt(argv,"h:i:t:",["ifile="])
   filename = ""
   selector = ""
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -t <selector>')
         sys.exit()
      if opt == "-t":
          selector = arg
      elif opt in ("-i", "--ifile"):
         filename = arg
    
   return selector, filename


def make_session(filename):
    if os.path.isfile(f"./{filename}.db"):
        os.remove(f"./{filename}.db")
    engine = create_engine(f"sqlite:///./{filename}.db", echo=False)
    dbsession = scoped_session(sessionmaker(bind=engine))
    Base.metadata.create_all(engine)
    return dbsession()

class HotelCounterHandler(osmium.SimpleHandler):
    def __init__(self, session, selector):
        super(HotelCounterHandler, self).__init__()
        self.num_nodes = 0
        self.session = session
        self.selector = selector

    def node(self, n):
        crude, detail = self.selector.split(".")
        
        if crude in n.tags and n.tags[crude] == detail:
            location = Location()
            location.lon = n.location.lon
            location.lat = n.location.lat
            self.session.add(location)


if __name__ == '__main__':
    selector, filename = arguments(sys.argv[1:])
    session = make_session(filename)
    h = HotelCounterHandler(session,  selector)
    h.apply_file(f"{filename}.osm")
    session.commit()

