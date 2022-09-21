import time
import os
import webbrowser
os.system('cls' if os.name=='nt' else 'clear')
clases = ("\n-cat Catalá\n-cast Castellano\n-eng English\n-mat Mates\n-tic TIC\n-tec Tecnologia\n-eco IAEE\n-ef Educació Física\n-gh Geografía i Historia\n-tut Tutoria")
os.system('cls' if os.name=='nt' else 'clear')
while True:
    start = input("\n-x | -h | Open: ")
    if error == True:
        time.sleep(5)
        error = False


    if start == "h":
        os.system('cls' if os.name=='nt' else 'clear')
        print(clases)

    elif start == "x":
        break 

    elif start == "cat":
        webbrowser.open("https://classroom.google.com/u/1/c/NTQ2NzkyMzY3NDcy")
        os.system('cls' if os.name=='nt' else 'clear')
    
    elif start == "cast":
        webbrowser.open("https://classroom.google.com/u/1/c/NTQ2OTAwOTYzNDkx")
        os.system('cls' if os.name=='nt' else 'clear')

    elif start == "eng":
        webbrowser.open("https://classroom.google.com/u/1/c/NTI3MTU2NzY4Mjg4")
        os.system('cls' if os.name=='nt' else 'clear')

    elif start == "mat":
        webbrowser.open("https://classroom.google.com/u/1/c/NTQ1ODQ1NjA3MTA3")
        os.system('cls' if os.name=='nt' else 'clear')
    
    elif start == "tic":
        webbrowser.open("https://classroom.google.com/u/1/c/NTQ2MjkyMDE4MDI5")
        os.system('cls' if os.name=='nt' else 'clear')

    elif start == "tec":
        webbrowser.open("https://classroom.google.com/u/1/c/NTQ2OTY2NTc4OTAx")
        os.system('cls' if os.name=='nt' else 'clear')

    elif start == "eco":
        webbrowser.open("https://classroom.google.com/u/1/c/NTQ3MjUzNjgxNzIw")
        os.system('cls' if os.name=='nt' else 'clear')

    elif start == "ef":
        webbrowser.open("https://classroom.google.com/u/1/c/NTQ3MjE2MzkzOTA2")
        os.system('cls' if os.name=='nt' else 'clear')

    elif start == "gh":
        webbrowser.open("https://classroom.google.com/u/1/c/NTQ3MDA3OTU4OTkx")
        os.system('cls' if os.name=='nt' else 'clear')

    elif start == "tut":
        webbrowser.open("https://classroom.google.com/u/1/c/NTQ1NjczNjg1MDMz")
        os.system('cls' if os.name=='nt' else 'clear')
     
    else:
        error = True
        while error:
            time.sleep(1)
            os.system('cls' if os.name=='nt' else 'clear')
            print("No hay resultados para tu búsqueda. Pruébalo con el menú de -h for Help\n")
            
        
