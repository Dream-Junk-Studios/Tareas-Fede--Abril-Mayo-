
from pdf_reader import extract_pdf_text
import re




def segmenter(texto):


    # Separa el texto en párrafos
    parrafos = texto.split('\n\n')

    # Define cuántos párrafos deseas en cada lista
    num_parrafos_por_lista = 1

    # Separa los párrafos en sublistas según la cantidad especificada
    listas_de_parrafos = [parrafos[i:i+num_parrafos_por_lista] for i in range(0, len(parrafos), num_parrafos_por_lista)]

    # Imprime las sublistas
    parrafos = []
    for lista in listas_de_parrafos:
        txt = re.sub(r'x0c' ,"" ,str(lista))
        txt = re.sub(r'\n' ,"" ,str(txt))
        parrafos.append(txt)
    return parrafos






def main():
    texto = extract_pdf_text('Tareas_Desarollo.pdf')
    segmenter(texto)

if __name__ == '__main__':
    main()