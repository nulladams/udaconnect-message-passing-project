import json
import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc


def sendmsg(person_id, lat, lon):
    """Create and send location message using gRPC protocol
    
        Params:
        person_id: id of person
        lat: person's latitude
        lon: person's longitude
    """
    location = location_pb2.LocationMessage(
        person_id=person_id,
        latitude=lat,
        longitude=lon
    )

    response = stub.Create(location)



channel = grpc.insecure_channel("localhost:30022")
stub = location_pb2_grpc.TestServiceStub(channel)

stub = location_pb2_grpc.LocationServiceStub(channel)

sendmsg(6, "42.9435345", "-12.4234234")