import joblib

modelo = joblib.load("modelo_classificador.pkl")

palavras_chave = {
    "computador": ["computador", "notebook", "pc", "roteador", "travando", "não liga", "virus"],
    "incendio": ["fogo", "incêndio", "queimou", "chama", "explosão", "pegou fogo"],
    "roubo": ["roubo", "roubaram", "furtaram", "arrombamento", "invadiram"],
    "desastre_natural": ["enchente", "alagamento", "tempestade", "granizo", "furacão", "vendaval", "alagou", "alagada", "Choveu", "Chuva"],
    "vidro": ["vidro", "espelho", "quebrou", "trincou"],
    "reparo_domestico": ["encanamento", "vazando", "torneira", "descarga", "cano", "reparo"],
    "tumulto": ["tumulto", "manifestação", "protesto", "depredaram", "quebraram", "baile", "social", "invasão"],
    "impacto_veiculo": ["amassado", "bateu", "colidiu", "caminhão", "impacto", "portao", "batida"],
}

def verificar_palavras_chave(texto):
    texto = texto.lower()
    for categoria, palavras in palavras_chave.items():
        for palavra in palavras:
            if palavra in texto:
                return categoria
    return None

def classificar_descricao(texto):
    categoria_modelo = modelo.predict([texto])[0]
    categoria_palavra = verificar_palavras_chave(texto)

    # Preferência por palavras-chave se elas forem diferentes do modelo
    if categoria_palavra is None or categoria_palavra == categoria_modelo:
        return categoria_modelo
    else:
        return categoria_palavra
