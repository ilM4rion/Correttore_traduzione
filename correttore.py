import os

def crea_dizionario(file_correzioni):
    correzioni = {}
    with open(file_correzioni, 'r', encoding='utf-8') as file:
        for linea in file:
            
            # Split della linea in due parti usando ':' come separatore
            parte_sbagliata, parte_corretta = linea.strip().split(':')

            # Rimozione delle "" in caso di stringhe
            parte_sbagliata = parte_sbagliata.replace('"', '')
            parte_corretta = parte_corretta.replace('"', '')

            # Aggiunta della correzione al dizionario
            correzioni[parte_sbagliata] = parte_corretta

    return correzioni

def sostituisci_correzioni(testo, correzioni):
    for sbagliato, corretto in correzioni.items():
        testo = testo.replace(sbagliato, corretto)
    return testo

def elabora_file(file_input, file_correzioni, cartella_output):
    
    # Crea il dizionario
    correzioni = crea_dizionario(file_correzioni)

    # Controllo esistenza cartella
    if not os.path.exists(cartella_output):
        os.makedirs(cartella_output)

    # Elabora ciascun file nella cartella di input
    for nome_file in os.listdir(cartella_input):
        percorso_file_input = os.path.join(cartella_input, nome_file)
        percorso_file_output = os.path.join(cartella_output, nome_file)

        with open(percorso_file_input, 'r', encoding='utf-8') as file_in, open(percorso_file_output, 'w', encoding='utf-8') as file_out:
            testo = file_in.read()
            testo_corretto = sostituisci_correzioni(testo, correzioni)
            file_out.write(testo_corretto)

if __name__ == "__main__":
    cartella_input = "Sostituisci con il percorso della tua cartella di input"  # Sostituisci con il percorso della tua cartella di input
    file_correzioni = "Sostituisci con il percorso del tuo file di correzioni"  # Sostituisci con il percorso del tuo file di correzioni
    cartella_output = "Sostituisci con il percorso della tua cartella di output"  # Sostituisci con il percorso della tua cartella di output

    elabora_file(cartella_input, file_correzioni, cartella_output)
