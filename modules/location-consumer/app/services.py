import logging
from datetime import datetime, timedelta
from typing import Dict, List

from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy import select

from geoalchemy2.functions import ST_AsText, ST_Point

from models import Location
from schemas import LocationSchema

from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

logging.basicConfig(level=logging.WARNING)
# logger = logging.getLogger("udaconnect-api")

engine = create_engine(
            f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
session = Session(engine)


class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        location, coord_text = (
            session.query(Location, Location.coordinate.ST_AsText())
            .filter(Location.id == location_id)
            .one()
        )

        # Rely on database to return text form of point to reduce overhead of conversion in app code
        location.wkt_shape = coord_text
        return location

    @staticmethod
    def create(location: Dict) -> Location:
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            #logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")

        new_location = Location()
        new_location.person_id = location["person_id"]
        #new_location.creation_time = location["creation_time"]
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        session.add(new_location)
        session.commit()

        return new_location


