import webbrowser
import json
import os
import sys
import urllib.parse

#Script to open the browser and automatically search for the site using the terminal
if __name__ == '__main__':

    #Ensure the command has the minimum required arguments
    if (len(sys.argv) < 2):
        print ("Uso incorreto! Digite: web <nome_do_site>")
        sys.exit(1)

    #Get the second argument of the command
    alvo = sys.argv[1].lower()

    try:
        #Get the current directory path
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        #Use the obtained path and append the sites.json file
        caminho_json = os.path.join(diretorio_script, "sites.json")

        #Open sites.json and save it to a variable
        with open(caminho_json, "r", encoding="utf-8") as arquivo:
            sites = json.load(arquivo)

        #Check if the alvo exists in sites
        if alvo in sites:
            #Get the website URL from the sites variable
            url = sites[alvo]
            #Open a connection with the browser and open the site via the URL
            browser_connection = webbrowser.open(url, 2, True)

            if not browser_connection:
                print("Erro de conexão com o navegador.")
            else:
                print(f"Abridor web: '{alvo}' aberto com sucesso!")
        else:
            print(f"O site '{alvo}' não está cadastrado no sites.json.")
            print(f"Deseja procurar o site diretamente no google?S/n")
            resposta = input()
            if resposta.lower() != 'n':
                termo = urllib.parse.quote_plus(alvo)
                url = f"https://www.google.com/search?q={termo}"
                webbrowser.open(url, 2 , True)

    except FileNotFoundError:
        print("Erro: Arquivo 'sites.json' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")