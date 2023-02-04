def insert_events(id_event, file, event, on_event, at_event, organization_id):
    return f"""INSERT INTO events (id, file, event, on_event , at_event, organization_id) VALUES ({id_event}, '{file}',
            '{event}', '{on_event}', STR_TO_DATE('{at_event}', '%Y-%m-%d %H:%i:%s'), '{organization_id}');"""


def insert_vehicles(id_event, id_vehicle, lat, lng, at_vehicle):
    return f"""INSERT INTO vehicles (id_event, id_vehicle, lat , lng, at_vehicle) VALUES ({id_event}, '{id_vehicle}', 
                {lat}, {lng}, STR_TO_DATE('{at_vehicle}', '%Y-%m-%d %H:%i:%s'));"""


def insert_vehicle_event(id_event, id_vehicle, lat, lng, at_vehicle):
    return f"""INSERT INTO vehicles (id_event, id_vehicle, lat , lng, at_vehicle) VALUES ({id_event}, '{id_vehicle}', 
                {lat}, {lng}, {at_vehicle});"""


def insert_operating_period(id_event, id_operating, start, finish):
    return f"""INSERT INTO operating_period (id_event, id_operating, start , finish) VALUES ({id_event}, 
                '{id_operating}', STR_TO_DATE('{start}', '%Y-%m-%d %H:%i:%s'), STR_TO_DATE('{finish}', '%Y-%m-%d %H:%i:%s'));"""