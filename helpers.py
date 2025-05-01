import os

from termcolor import cprint

def clear_console():
   if os.name =='nt':
      os.system('cls')
   else:
      os.system('clear')



def show_menu():
   cprint('Menu', 'white', attrs=['bold', 'underline'])
   cprint('1- Estado de sensores', 'black', 'on_yellow', attrs=['bold', 'underline'])
   cprint('2- Agregar sensor', 'black', 'on_yellow', attrs=['bold', 'underline'])
   cprint('3- Quitar sensor', 'black', 'on_yellow', attrs=['bold', 'underline'])
   cprint('4- Configurar adquisición de datos', 'black', 'on_yellow', attrs=['bold', 'underline'])
   cprint('5- Modificar un sensor', 'black', 'on_yellow', attrs=['bold', 'underline'])
   cprint('0- SALIR \n', 'black', 'on_red', attrs=['bold', 'underline'])
