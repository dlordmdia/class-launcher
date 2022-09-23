import time
import os
import webbrowser
import urllib.parse
os.system('cls' if os.name=='nt' else 'clear')
clases = ("\nSi estás en Un Online Compiler (Terminal de Python en una WEB) utiliza mejor el script class-launcher.online.py de mi GitHub \n\n-cat Catalá\n-cast Castellano\n-eng English\n-mat Mates\n-tic TIC\n-tec Tecnologia\n-eco IAEE\n-ef Educació Física\n-gh Geografía i Historia\n-tut Tutoria\n-val Valors\n\n-cal Horario de Clases\n")
os.system('cls' if os.name=='nt' else 'clear')

art = input("Estás en un online Terminal(WEB)? (y/n): ")

if art == "y":

    while True:
        start = input("\n-x | -h | Abrir: ")

        if start == "h":
            print(clases)

        elif start == "x":
            break 

        elif start == "cat":
            s = urllib.parse.quote('https://classroom.google.com/u/1/c/NTQ2NzkyMzY3NDcy')
            print('https://'+s)

        
        elif start == "cast":
            s = urllib.parse.quote('https://classroom.google.com/u/1/c/NTQ2OTAwOTYzNDkx')
            print('https://'+s)

        elif start == "eng":
            s = urllib.parse.quote('somesite/foo/bar/foo bar/foo-bar foo/bar')
            print('https://'+s)

        elif start == "mat":
            s = urllib.parse.quote('https://classroom.google.com/u/1/c/NTQ1ODQ1NjA3MTA3')
            print('https://'+s)
        
        elif start == "tic":
            s = urllib.parse.quote('https://classroom.google.com/u/1/c/NTQ2MjkyMDE4MDI5')
            print('https://'+s)

        elif start == "tec":
            s = urllib.parse.quote('https://classroom.google.com/u/1/c/NTQ2OTY2NTc4OTAx')
            print('https://'+s)

        elif start == "eco":
            s = urllib.parse.quote('https://classroom.google.com/u/1/c/NTQ3MjUzNjgxNzIw')
            print('https://'+s)

        elif start == "ef":
            s = urllib.parse.quote('https://classroom.google.com/u/1/c/NTQ3MjE2MzkzOTA2')
            print('https://'+s)

        elif start == "gh":
            s = urllib.parse.quote('https://classroom.google.com/u/1/c/NTQ3MDA3OTU4OTkx')
            print('https://'+s)

        elif start == "tut":
            s = urllib.parse.quote('https://classroom.google.com/u/1/c/NTQ1NjczNjg1MDMz')
            print('https://'+s)
        
        elif start == "val":
            s = urllib.parse.quote('https://classroom.google.com/u/1/c/NTQ1ODM0Njg1NzE0')
            print('https://'+s)
        
        elif start == "cal":
            print('''
                    ________________________________
                    /                                \.
                    |eco  |tec  |cast/cat |eco  |eng |
                    |-----|-----|---------|-----|----|
                    |tic  |eco  |eng      |tec  |val |
                    |-----|-----|---------|-----|----|
                    |cast |ef   |gh       |ef   |cast|
                    |/////|/////|/////////|/////|////|
                    |cat  |eng  |tec      |cat  |mat |
                    |-----|-----|---------|-----|----|
                    |mat  |tic  |mat      |tic  |cat |
                    |-----|-----|---------|-----|----|
                    |gh   |cast |tut      |mat  |gh  |
                    \________________________________/
                    ''')
        
        else:
            print("No hay resultados para tu búsqueda. Pruébalo con el menú de -h for Help\n")

else:
    while True:
        start = input("\n-x | -h | Abrir: ")

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
        
        elif start == "val":
            webbrowser.open("https://classroom.google.com/u/1/c/NTQ1ODM0Njg1NzE0")
            os.system('cls' if os.name=='nt' else 'clear')
        
        elif start == "cal":
            os.system('cls' if os.name=='nt' else 'clear')
            print('''
                    ________________________________
                    /                                \.
                    |eco  |tec  |cast/cat |eco  |eng |
                    |-----|-----|---------|-----|----|
                    |tic  |eco  |eng      |tec  |val |
                    |-----|-----|---------|-----|----|
                    |cast |ef   |gh       |ef   |cast|
                    |/////|/////|/////////|/////|////|
                    |cat  |eng  |tec      |cat  |mat |
                    |-----|-----|---------|-----|----|
                    |mat  |tic  |mat      |tic  |cat |
                    |-----|-----|---------|-----|----|
                    |gh   |cast |tut      |mat  |gh  |
                    \________________________________/
                    ''')
        
        else:
            os.system('cls' if os.name=='nt' else 'clear')
            time.sleep(0.5)
            print("No hay resultados para tu búsqueda. Pruébalo con el menú de -h for Help\n")