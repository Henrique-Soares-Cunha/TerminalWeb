import webbrowser
import json
import os
import sys
import urllib.parse

def serchManager( alvo , is_site_listed : bool):
    if (is_site_listed == True):
        # Get the website URL from the sites variable
        url = sites[alvo]
    else:
        termo = urllib.parse.quote_plus(alvo)
        url = f"https://www.google.com/search?q={termo}"

    # Open a connection with the browser and open the site via the URL
    browser_connection = webbrowser.open(url, 2, True)

    # Check browser connection status
    if not browser_connection:
        print("Erro de conexão com o navegador.")
        sys.exit(1)
    else:
        print(f"Abridor web: '{alvo}' aberto com sucesso!")

def geminiQuestion( question ):
    print("função em desencolvimento")
    print(sys.argv[2].lower())
    #vai conectar com o gemini, fazer uma pergunta, printar a resposta parar de executar
    # a fazer
    sys.exit(1)

#Script to open the browser and automatically search for the site using the terminal
if __name__ == '__main__':

    #Ensure the command has the minimum required arguments
    tamanho = len(sys.argv)
    if (tamanho < 2 or tamanho > 3):
        print ("Uso incorreto! Digite: web <nome_do_site>")
        sys.exit(1)

    if (tamanho == 3):
        try:
            comando = sys.argv[1].lower()
            match comando:
                case "gemini":
                    geminiQuestion( sys.argv[2].lower())
                case _:
                    print(f"comando ${comando} invalido")
                    sys.exit(1)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            sys.exit(1)

    else:
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
            is_site_listed = alvo in sites
            serchManager(alvo, is_site_listed)

        except FileNotFoundError:
            print("Erro: Arquivo 'sites.json' não encontrado.")
            sys.exit(1)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            sys.exit(1)