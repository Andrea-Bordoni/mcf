def somma_n(n):
    """Questa funzione restituisce la somma dei primi n numeri naturali."""
    somma=0
    for i in range(1,n+1):
        somma=somma+i
    return somma

def somma_sqrt(n):
    """Questa funzione restituisce la somma delle radici dei primi n numeri naturali."""
    somma=0
    for i in range(1,n+1):
        somma=somma+i**0.5
    return somma

def sumprod(n):
    """Questa funzione restituisce la somma e il prodotto dei primi n numeri naturali."""
    somma=0
    p=1
    for i in range(1,n+1):
        somma=somma+1
        p=p*i
    return somma,p

def sum_alfa(n,alfa=1):
    """Questa funzione restituisce la somma delle potenze alfa-esime dei primi n numeri naturali."""
    somma=0
    for i in range(1,n+1):
        somma=somma+i**alfa
    return somma


if __name__=="__main__":
    n=int(input('Inserisci n: '))

    #somma dei primi n numeri naturali
    print(somma_n.__doc__)
    print(somma_n(n))

    #somma delle radici dei primi n numeri naturali
    print(somma_sqrt.__doc__)
    print(somma_sqrt(n))

    #somma e prodotto dei primi n numeri naturali
    print(sumprod.__doc__)
    print(sumprod(n))

    #somma delle radici alfa-esime dei primi n numeri narturali, con alfa da passare come parametro
    print(sum_alfa.__doc__)
    print(sum_alfa(n))
    print(sum_alfa(n,3))
