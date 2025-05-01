from sensors_data import sensors_db
from constants import ON_LINE, OFF_LINE

# SENSOR
# - id: int
# - name: str
# - description: str
# - status: str
# - value: float
# - alarm_high: float
# - alarm_low: float

def list_sensors():
    if not __check_if_sensors():
        return

    for index, sensor in enumerate(sensors_db, start=1):
        line_status = ON_LINE if sensor['status'] else OFF_LINE
        print(f'{index}.{sensor['name']} - {line_status}')

def add_sensor():
    #id_assign llamar a funcion que asigan id
    name = input('Nombre del sensor: ')
    description = input('Descripción del sensor: ')
    alarm_high = input('Alarma nivel alto: ')
    alarm_low = input('Alarma nivel bajo: ')
    sensor = {
        'name': name,
        'description': description,
        'alarm_high': alarm_high,
        'alarm_low': alarm_low,
    }
    sensors_db.append(sensor)
 

def delete_sensor():
    pass

def update_sensor():
    pass

def acquisition_config():
    pass

def __check_if_sensors():
    if not sensors_db:
        print('No existen sensores cargados aun')
        return False
    return True
