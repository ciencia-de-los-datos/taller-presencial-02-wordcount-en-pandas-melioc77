"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame. un solo dataframe
    #
    filenames = glob.glob(f"{input_directory}/*.txt")
    #y tomamos el primer elemento y lo tomamos como nombre, el header me habla de la cabecera, con names puedo asignar el nombre de la columna
    #dataframes=[]
    #for filename in filenames:
    #    dataframes.append(pd.read_csv(filenames[0], sep="\t", header=None, names=["text"]))
    
    
    dataframes=[
        pd.read_csv(filename, sep="\t", header=None, names=["text"])
        for filename in filenames
    ]
    
    #df =pd.read_csv(filenames[0], sep="\t", header=None, names=["text"])
    #print(dataframes)
    concateanted_df = pd.concat(dataframes, ignore_index=True)
    return concateanted_df
    



def clean_text(dataframe):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #
    dataframe =dataframe.copy() #para no modificar el original
    dataframe["text"] = dataframe["text"].str.lower()
    dataframe["text"] = dataframe["text"].str.replace(".", "").str.replace(",", "")
    #dataframe["text"] = dataframe["text"].str.replace(",", "")

    return dataframe


def count_words(dataframe):
    """Word count"""

    dataframe = dataframe.copy()  
    dataframe["text"]  = dataframe["text"].str.split()
    dataframe = dataframe.explode("text")
    dataframe["count"] =  1 #agrego una columna de puros 1, cuyo encabezado es count
    dataframe = dataframe.groupby("text").agg({"count": "sum"}) #va a generar la suma de todas las claves que tengan por valor el mismo texto en común
    #dataframe = dataframe["text"].value_counts()#.reset_index()
    return dataframe

def count_words_(dataframe):
    """Word count"""

    dataframe = dataframe.copy()  
    dataframe["text"]  = dataframe["text"].str.split()
    dataframe = dataframe.explode("text")
    #dataframe["count"] =  1 #agrego una columna de puros 1, cuyo encabezado es count
    #dataframe = dataframe.groupby("text").agg({"count": "sum"}) #va a generar la suma de todas las claves que tengan por valor el mismo texto en común
    dataframe = dataframe["text"].value_counts()#.reset_index()
    return dataframe




def save_output(dataframe, output_filename):
    """Save output to a file."""
    #
    # Guarde el DataFrame en un archivo de texto.
    #
    dataframe.to_csv(output_filename, sep="\t", index=True, header=False)

#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""
    df = load_input(input_directory)

    df= clean_text(df)
    df =count_words_(df)
    save_output(df, output_filename)
   

if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
