

import socket



def port_svarar(vard, port): 
    try: 
        with socket.create_connection((vard, port), timeout=2): 
            return True 
    except OSError: 
        return False



def ServiceControl():
    servrar = ["127.0.0.1", "127.0.0.1"] 
    portar = [8000, 8001] 

    for i in range(len(servrar)): 
        if port_svarar(servrar[i], portar[i]): 
            print(servrar[i], "port", portar[i], "– svarar") 
        else: 
            print(servrar[i], "port", portar[i], "– SVARAR INTE")

