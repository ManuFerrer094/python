import time
import datetime

print("Los segundos son:",time.time())

print("El dia de hoy es: "+datetime.date.today().strftime("%Y-%m"))
print("El mes actual tiene"+datetime.date.today().strftime("%t"))


