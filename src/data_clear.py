import pandas as pd
from statistics import mean, median, mode 

def converter_type(data: str, atr: str, type: str)-> None:
    """
    Realiza a conversão do tipo de dado no atributo.
    
    Args:
        data: dataset a set selecionado.
        Atr: atributo que deseja converter tipo.
        type: o tipo de dados que deseja para ser convertido "string, int, float, etc".
    """
    
    data = data
    atr = atr
    tipo = type
    data[atr] = data[atr].astype(tipo)
    
    try:
        print(f"o atributo {atr} foi convertido para {tipo}")
            
    except Exception as e:
        print(f'Ocorreu erro {e}')
        




def valores_faltantes(data: pd.DataFrame, atr: str, metodo: str)-> None:
    """
    Realiza o input nos valores faltantes conforme 'mean', 'median' ou 'mode'.
    
    Args:
        data: Dataframe selecionado.
        Atr: atributo para preencher.
        metodo: string com o método ('mean', 'median', 'mode').
    """
    try:
        if metodo == 'mean':
            valor = data[atr].mean()     
        elif metodo == 'median':
            valor = data[atr].median()     
        elif metodo == 'mode':
            valor = data[atr].mode()
        else:
            print("Método inválido. Metodos aceitos são ('mean', 'median' ou 'mode').")
            return     
        
        data[atr] = data[atr].fillna(valor)
        
        print(f"O atributo {atr} teve nulos ou faltantes substituidos por {metodo}: {valor}")
    
    except Exception as e:
        print(f'Ocorreu erro {atr} {e}')
        
    
