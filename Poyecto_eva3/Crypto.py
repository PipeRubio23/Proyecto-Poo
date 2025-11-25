from cryptography.fernet import Fernet
from os import system

system("cls")

clave_fernet = "3yDYUan7tufWfCBwR96QSYXkisCW-YehF6lqPZUkoQQ="
#print(f"clave de acceso: {clave_fernet.decode()}")
#print(f"longitud clave acceso: {len(clave_fernet)}")

clave = input("digite clave: ")
f= Fernet(clave_fernet)
clave_encriptada= f.encrypt(clave.encode())
print(f"clave codificada: {clave_encriptada.decode()}")