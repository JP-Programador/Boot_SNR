from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns

exemplos = [
    ("Caiu um raio e queimou todos os aparelhos eletrônicos.", "incendio"),
    ("Entraram na minha casa.", "roubo"),
    ("A parede da sala está cheia de rachaduras após o terremoto.", "desastre_natural"),
    ("Minha televisão queimou depois de uma tempestade.", "incendio"),
    ("O telhado voou com o vento forte de ontem.", "desastre_natural"),
    ("Minha janela foi quebrada durante uma briga na rua.", "vidro"),
    ("Preciso de ajuda para consertar o encanamento da cozinha.", "reparo_domestico"),
    ("O notebook parou de funcionar depois do apagão.", "computador"),
    ("Fizeram uma manifestação e quebraram o portão.", "tumulto"),
    ("A rua ficou alagada e entrou água pela garagem.", "desastre_natural"),
    ("A geladeira queimou por causa de uma descarga elétrica.", "incendio"),
    ("Levaram minha bicicleta da garagem.", "roubo"),
    ("Houve uma explosão no aquecedor e causou fogo.", "incendio"),
    ("O temporal derrubou a árvore em cima do muro.", "desastre_natural"),
    ("Quebraram o espelho do banheiro sem querer.", "vidro"),
    ("Preciso arrumar a descarga do banheiro.", "reparo_domestico"),
    ("Meu computador está travando após queda de energia.", "computador"),
    ("Durante o protesto jogaram pedras na minha casa.", "tumulto"),
    ("O granizo perfurou a cobertura da área externa.", "desastre_natural"),
    ("Explodiu um transformador e queimou meu som.", "incendio"),
    ("Meu portão foi amassado por um caminhão.", "impacto_veiculo"),
    ("Alguém tentou me chantagear exigindo dinheiro.", "roubo"),
    ("Minha casa foi arrombada à noite.", "roubo"),
    ("O fogão explodiu quando fui acender.", "incendio"),
    ("O furacão arrancou a porta da garagem.", "desastre_natural"),
    ("Furto de objetos durante a madrugada.", "roubo"),
    ("A ventania arrancou a telha e molhou tudo.", "desastre_natural"),
    ("O espelho da sala caiu e quebrou.", "vidro"),
    ("O encanamento estourou e alagou a cozinha.", "reparo_domestico"),
    ("O roteador queimou depois da chuva.", "computador"),
    ("A manifestação invadiu o bairro e depredaram casas.", "tumulto"),
    ("A enxurrada levou móveis do quintal.", "desastre_natural"),
    ("Meu notebook não liga mais após o raio.", "computador"),
    ("Roubaram meu celular pela janela.", "roubo"),
    ("Uma explosão de gás assustou a vizinhança.", "incendio"),
    ("Os ventos arrancaram o portão da frente.", "desastre_natural"),
    ("Minha janela trincou sozinha com o frio.", "vidro"),
    ("Preciso de ajuda com a torneira que está vazando.", "reparo_domestico"),
    ("O PC não liga após o pico de energia.", "computador"),
    ("Jogaram pedras e quebraram o vidro do carro na garagem.", "vidro"),
    ("Arrombaram o portão e invadiram meu quintal.", "roubo"),
    ("Cortaram os fios para roubar meu ar-condicionado.", "roubo"),
    ("O temporal destruiu meu jardim inteiro.", "desastre_natural"),
    ("Preciso de encanador urgente para o banheiro.", "reparo_domestico"),
    ("Depredaram minha fachada durante o protesto.", "tumulto"),
    ("O transformador explodiu e queimou vários eletros.", "incendio"),
    ("Derrubaram a cerca durante o tumulto.", "tumulto"),
    ("Explosão do botijão provocou incêndio.", "incendio"),
    ("Computador parou após falta de luz.", "computador"),
    ("alagou.", "desastre_natural"),
    ("Furto de eletrônicos.", "roubo"),
    ("Meu computador queimou.", "computador"),
    ("Meu notebook queimou.", "computador"),
    ("Meu pc queimou.", "computador"),
]

frases, categorias = zip(*exemplos)

X_train, X_test, y_train, y_test = train_test_split(frases, categorias, test_size=0.2, random_state=42)

modelo = make_pipeline(TfidfVectorizer(), MultinomialNB())

modelo.fit(X_train, y_train)

joblib.dump(modelo, "modelo_classificador.pkl")
print("✅ Modelo treinado e salvo.")


y_pred = modelo.predict(X_test)
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

acuracia = accuracy_score(y_test, y_pred)
relatorio = classification_report(y_test, y_pred)
matriz = confusion_matrix(y_test, y_pred)
labels = sorted(set(categorias))


print("🔎 Acurácia:", round(acuracia * 100, 2), "%\n")
print("📋 Relatório de Classificação:")
print(relatorio)
print("📊 Matriz de Confusão:")
print(matriz)

plt.figure(figsize=(10, 7))
sns.heatmap(matriz, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.title("Matriz de Confusão")
plt.tight_layout()
plt.show()
