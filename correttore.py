import os

def leggi_correzioni(file_correzioni):
    correzioni = {}
    with open(file_correzioni, 'r') as file:
        for linea in file:
            # Split della linea in due parti usando ':' come separatore
            parte_sbagliata, parte_corretta = linea.strip().split(':')

            # Rimozione delle "" in caso di stringhe
            parte_sbagliata.replace('"', '')
            parte_corretta.replace('"', '')
            
            # Aggiunta della correzione al dizionario
            correzioni[parte_sbagliata] = parte_corretta
    return correzioni

def sostituisci_correzioni(testo, correzioni):
    for sbagliato, corretto in correzioni.items():
        testo = testo.replace(sbagliato, corretto)
    return testo

def elabora_file(file_input, file_correzioni, cartella_output):
    # Leggi le correzioni dal file
    correzioni = leggi_correzioni(file_correzioni)

    # Assicurati che la cartella di output esista
    if not os.path.exists(cartella_output):
        os.makedirs(cartella_output)

    # Elabora ciascun file nella cartella di input
    for nome_file in os.listdir(file_input):
        percorso_file_input = os.path.join(file_input, nome_file)
        percorso_file_output = os.path.join(cartella_output, nome_file)

        with open(percorso_file_input, 'r') as file_in, open(percorso_file_output, 'w') as file_out:
            testo = file_in.read()
            testo_corretto = sostituisci_correzioni(testo, correzioni)
            file_out.write(testo_corretto)

if __name__ == "__main__":
    cartella_input = "percorso_cartella_input"  # Sostituisci con il percorso della tua cartella di input
    file_correzioni = "percorso_file_correzioni.txt"  # Sostituisci con il percorso del tuo file di correzioni
    cartella_output = "percorso_cartella_output"  # Sostituisci con il percorso della tua cartella di output

    elabora_file(cartella_input, file_correzioni, cartella_output)
