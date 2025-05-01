from termcolor import cprint

from helpers import show_menu, clear_console
from sensors import add_sensor, delete_sensor, update_sensor, list_sensors, acquisition_config 
 

def run():
    while True:
      show_menu()

      seleccion = input('Elija una opción [0-5]: ')
      print(f'Opción seleccionada: {seleccion}')
      match seleccion:
         case '1':
            list_sensors()
         case '2':
            add_sensor()
         case '3':
            delete_sensor()
         case '4':
            acquisition_config()
         case '5':
            update_sensor()
         case '0':
            break 
         case _:
            print('Opción NO válida')
            
 

if __name__ == '__main__':
    cprint('BIENVENIDO AL ADMINISTRADOR DE SENSORES IOT \n', 'white', attrs=['bold', 'underline'])
    run()
 