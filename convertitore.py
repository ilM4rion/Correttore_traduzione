import os
import docx2txt
from docx import Document 

def convert_docx_in_txt(docx_path, txt_path):
    try:
        # Legge il file .docx
        doc = Document(docx_path)
        
        # Estrae il testo dal documento
        testo = ""
        for riga in doc.paragraphs:
            testo += riga.text + '\n'
        
        # Scrive il testo estratto in un file .txt
        with open(txt_path, 'w', encoding='utf-8') as file_txt:
            file_txt.write(testo)
    except Exception as e:
        print(f"Errore nella conversione di {docx_path}: {e}")

def converti_tutti_docx_in_txt(cartella_input, cartella_output):

    if not os.path.exists(cartella_output):
        os.makedirs(cartella_output)

    # Scorre tutti i file nella cartella
    for file_name in os.listdir(cartella_input):
        if file_name.endswith(".docx"):

            #os.path.join crea il path del singolo file nella directory
            docx_path = os.path.join(cartella_input, file_name)
            txt_name = file_name.replace(".docx", ".txt")
            txt_path = os.path.join(cartella_output, txt_name)

            # Converte il file .docx in .txt
            convert_docx_in_txt(docx_path, txt_path)

if __name__ == "__main__":
    
    cartella_input = "Inserire percorso directory input"
    cartella_output = "Inserire percorso directory output"
    converti_tutti_docx_in_txt(cartella_input, cartella_output)
