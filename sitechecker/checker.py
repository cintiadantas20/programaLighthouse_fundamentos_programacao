from http.client import HTTPConnection
from urllib.parse import urlparse

def site_is_online(url, timeout=2):
    """Retorna True se a URL está online e uma exceção, se não estiver"""
    # Define a exceção
    error = Exception("Ops, algo errado.")
    # Interpreta uma URL e retorna os seus componentes
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    # Cria um for loop para consultar as portas HTTP e HTTPs
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error