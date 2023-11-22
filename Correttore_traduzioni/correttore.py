import os
import docx2txt

def converti_docx_in_txt(cartella_input, cartella_output):
    # Verifica se la cartella di output esiste, altrimenti creala
    if not os.path.exists(cartella_output):
        os.makedirs(cartella_output)

    # Elabora ogni file .docx nella cartella di input
    for filename in os.listdir(cartella_input):
        if filename.endswith(".docx"):
            input_path = os.path.join(cartella_input, filename)
            output_filename = os.path.splitext(filename)[0] + ".txt"
            output_path = os.path.join(cartella_output, output_filename)

            # Converte il file .docx in .txt
            try:
                testo = docx2txt.process(input_path, output_path)
                print(f"File convertito: {output_filename}")
            except Exception as e:
                print(f"Errore durante la conversione di {filename}: {e}")

if __name__ == "__main__":
    cartella_input = "/percorso/della/cartella/input"
    cartella_output = "/percorso/della/cartella/output"

    converti_docx_in_txt(cartella_input, cartella_output)
