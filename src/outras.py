import requests
from pathlib import Path

def baixar_arquivo(url: str, pasta_destino: str, nome_arquivo: str) -> None:
    """
    Realiza o download de um arquivo e o salva em uma pasta específica.
    
    Args:
        url: Link direto para o arquivo bruto (raw).
        pasta_destino: Nome ou caminho da pasta onde o arquivo será salvo.
        nome_arquivo: Nome que o arquivo terá localmente.
    """
    # 1. Usando Pathlib para caminhos mais limpos
    pasta = Path(pasta_destino)
    caminho_completo = pasta / nome_arquivo

    # 2. Criar pasta 
    pasta.mkdir(parents=True, exist_ok=True)

    try:
        print(f"Iniciando download de: {nome_arquivo}...")
        
        # 3. Timeout evita que o código fique "travado" se o site cair
        resposta = requests.get(url, timeout=10)
        
        # 4. Verifica se o download deu certo (Ex: erro 404 ou 500)
        resposta.raise_for_status()

        # 5. Salva o arquivo
        with open(caminho_completo, 'wb') as f:
            f.write(resposta.content)
            
        print(f"✅ Sucesso! Arquivo salvo em: {caminho_completo}")

    except requests.exceptions.HTTPError as err:
        print(f"❌ Erro HTTP: {err}")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")