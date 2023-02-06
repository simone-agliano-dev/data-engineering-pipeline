import datetime
from src.app.logging import Logs
from src.app.database.db_connector import Database
from src.constants import DB, USER, PASSWORD, HOST, EVENT, VEHICLES, OPERATING, VEHICLES_DEREGISTER
from src.app.utilities.utils import generate_id, validate_fields
from src.app.database.query_options import insert_events, insert_vehicles, insert_operating_period, insert_vehicle_event


def transform_date(date: str) -> str:
    date_object = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date_object.strftime("%Y-%m-%d %H:%M:%S")


def event_data(data: dict) -> list:
    validate_fields(data, EVENT)
    event_type = data['event']
    on = data['on']
    at = transform_date(data['at'])
    organization_id = data['organization_id']
    return [event_type, on, at, organization_id]


def vehicle_event(data: dict) -> list:
    validate_fields(data, VEHICLES_DEREGISTER)
    id_vehicle = data['id']
    lat = 'NULL'
    lng = 'NULL'
    at_vehicle = 'NULL'
    return [id_vehicle, lat, lng, at_vehicle]


def vehicle_update(data: dict) -> list:
    validate_fields(data, VEHICLES)
    id_vehicle = data['id']
    lat = data['location']['lat']
    lng = data['location']['lng']
    at_vehicle = transform_date(data['location']['at'])
    return [id_vehicle, lat, lng, at_vehicle]


def operation_period_data(data: dict) -> list:
    validate_fields(data, OPERATING)
    id_operating = data['id']
    start = transform_date(data['start'])
    finish = transform_date(data['finish'])
    return [id_operating, start, finish]


def transform_and_load(data: list):
    """
    Takes a list of data and perform the Transformation and Load part of the pipeline, in this case the destination is a Database
    :param data: list
    :return:None
    """
    logs = Logs()
    my_db = Database(host=HOST, user=USER, password=PASSWORD)

    for inner_list in data:
        file = inner_list[0]
        for inner_dict in inner_list[1:]:
            id_event = generate_id()
            event = event_data(inner_dict)
            insert_event_query = insert_events(id_event, file, event[0], event[1], event[2], event[3])
            my_db.query(insert_event_query)
            if inner_dict['event'] in 'update':
                vehicle = vehicle_update(inner_dict['data'])
                insert_vehicle_query = insert_vehicles(id_event, vehicle[0], vehicle[1], vehicle[2], vehicle[3])
                my_db.query(insert_vehicle_query)
            elif inner_dict['event'] in ('deregister', 'register'):
                vehicle = vehicle_event(inner_dict['data'])
                insert_vehicle_query = insert_vehicle_event(id_event, vehicle[0], vehicle[1], vehicle[2], vehicle[3])
                my_db.query(insert_vehicle_query)
            elif inner_dict['event'] in ('create', 'delete'):
                operating = operation_period_data(inner_dict['data'])
                operation_period_query = insert_operating_period(id_event, operating[0], operating[1], operating[2])
                my_db.query(operation_period_query)
            else:
                logs.error(inner_dict)
                print(f"Error data: {inner_dict}")
