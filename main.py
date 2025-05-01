from termcolor import cprint

def run():
    while True:
      cprint('1- Estado de sensores', 'black', 'on_yellow', attrs=['bold', 'underline'])
      cprint('2- Agregar sensor', 'black', 'on_yellow', attrs=['bold', 'underline'])
      cprint('3- Quitar sensor', 'black', 'on_yellow', attrs=['bold', 'underline'])
      cprint('4- Configurar adquisición de datos', 'black', 'on_yellow', attrs=['bold', 'underline'])
      cprint('0- SALIR', 'black', 'on_red', attrs=['bold', 'underline'])
      break

if __name__ == '__main__':
    cprint('BIENVENIDO AL ADMINISTRADOR DE SENSORES IOT \n Menu:', 'white', attrs=['bold', 'underline'])
    run()
 