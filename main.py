# importar modulos
import wikipedia
import random

# cambiar el lenguaje. Español
wikipedia.set_lang('es')

# selector de opciones de artículos
def searchselector():
    global searchselect
    searchselect=int(input('Selecciona una opción de la lista (0 a '+ str(len(resultlist)-1)+'): '))

# buscador random
def randomsearchselector():
    global searchselect
    searchselect=random.randrange(len(resultlist))

# obtener pagina especifica
def getpage(searchselect):
    global page
    page=wikipedia.page(resultlist[searchselect], auto_suggest=False)


# obtener pagina random
def getrandompage(topic):
    global page
    page=wikipedia.page(topic)

# obtener resumen de la página
def getsummary(page):
    str="_"
    print(str*64)
    print(page.title)
    print(str*64)
    print(page.summary)
    print(str*64)


# obtener contenido completo
def getcontent(page):
    str="_"
    print(str*64)
    print(page.content)
    print(str*64)


# salir del programa
def exitfunc():
    n=input('¿Quieres salir? s/n: ')
    if (n=="s"):
        exit()
    else:
        searchfunc()

# nueva busqueda
def newsearchfunc():
    secondchoice=input("¿Quieres hacer una nueva búsqueda? s/n: ")
    if (secondchoice=="s"):
        searchfunc()
    else:
        linkaskfunc()

# random link de la página
def linkaskfunc():
    secondchoice=input("¿Quieres saltar a un enlace aleatorio dentro de la página actual? s/n: ")
    if (secondchoice=="s"):
        linkfunc()
    else:
        exitfunc()

# random link
def linkfunc():
    global searchselect
    global page
    global resultlist
    resultlist=page.links
    searchselect=random.randrange(len(resultlist))
    getpage(searchselect)
    decidedisplaytype=input("¿Quieres ver un resumen de la página? En caso de No, se obtendrá la página completa s/n: ")
    if (decidedisplaytype=="s"):
        getsummary(page)
    else:
        getcontent(page)
    linkaskfunc()

# programa
def searchfunc():
    global inputsearch
    global resultlist
    askrandom=input("¿Generar artículo aleatorio? s/n: ")
    if (askrandom=="s"):
        topic=wikipedia.random(1)
        getrandompage(topic)
    else:
        inputsearch=input('Ingrese un término de búsqueda para buscar en Wikipedia: ')
        resultlist=list(wikipedia.search(inputsearch))
        for i in range(len(resultlist)):
                print(i,"- ",resultlist[i], end='\n')
        decideselecttype=input("¿Quieres seleccionar un artículo de la lista al azar? s/n: ")
        if (decideselecttype=="s"):
            randomsearchselector()
        else:
            searchselector()
        getpage(searchselect)
    decidedisplaytype=input("¿Quieres ver un resumen de la página? En caso de No, se obtendrá la página completa s/n: ")
    if (decidedisplaytype=="s"):
        getsummary(page)
    else:
        getcontent(page)
    newsearchfunc()

searchfunc()