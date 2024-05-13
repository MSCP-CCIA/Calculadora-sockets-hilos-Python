import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
cod=""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
    print ("Operaciones:")
    print ("1.Suma | 2.Resta | 3.Multiplicacion | 4.Division | 5.Potenciacion | 6.Logaritmacion ")
    print ("Digite la operación sin puntos: ")
    operacion=input()  
    s.send(operacion.encode("UTF-8"))
    recibido =s.recv(BUFFER_SIZE).decode("UTF-8")
    ls=recibido
    if len(ls) > 1:
        ls=[]
        lisnum=[]
        lis=[]
        ls=recibido
        for i in ls:
            if i == "@":
                lis.append(lisnum)
                lisnum=[]
            if i != "@":
                lisnum.append(i)
        #print (lis)
        cod="".join(lis[0])
        IP="".join(lis[1])
        PORT="".join(lis[2])
        OPERAC="".join(lis[3])
    if cod == 'si':
        print ("Digite dos numeros para realizar "+OPERAC+": ")
        print("Numero 1:")
        numero1=input()
        print ("Numero 2:")
        numero2=input()
        num=numero1+'@'+numero2
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(IP), int(PORT)))
        s.send(num.encode("UTF-8"))
        resultado = s.recv(BUFFER_SIZE).decode("UTF-8")
        print ("El resultado de la operacion "+OPERAC+" es: "+resultado+"")
    if recibido == 'o':
        print ("El servidor al que intenta acceder se encuentra Apagado(OFF)")
        print ("Intente más tarde por favor...")
     
    break  
s.close()
