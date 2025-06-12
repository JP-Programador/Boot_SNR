from base_clientes import clientes
from planos import planos, nomes_amigaveis
from classificador import classificar_descricao
import uuid

def gerar_protocolo():
    return str(uuid.uuid4())[:8].upper()  
protocolo = gerar_protocolo()

def mostrar_coberturas(plano):
    print("\nCoberturas do seu plano:")
    for chave in planos[plano]:
        print(f" - {nomes_amigaveis[chave]}")
    print("")

def triagem():
    while True:
        print("\nOpa, Sou a juli, que irá te ajudar a acionar o seguro imediatamente. Vamos começar! \n")
        cpf = input("Me diga seu CPF: ").strip()

        if cpf not in clientes:
            print("❌ Ops, que pena não encontrei seu CPF em nosa base. Verifica os digitos, caso seja cliente novo entra em cotato com o numero 0800 9380 13452.")
            continue

        cliente = clientes[cpf]
        print(f"\n✅ Encontamos seu cadastro, Seja bem vindo ao chat {cliente['nome']}!")
        print(f"Endereço encontrado em nosso sitema: {cliente['endereco']}")

        confirma = input("Verifica se o endereço está correto, para darmos continuidade. (s para sim / n para não): ").lower()

        if confirma != 's':
            print(f"Ops que pena, deve ter dado algum problem em seu cadastro, entre em contato com o numero 0800 9380 13452, que iremos resolver o seu problema. \n Obrigado pela atenção, {cliente['nome']}")
            continue

        plano = cliente['plano']
        print(f"\n {cliente['nome']}, Segue seu plano e a cobertura do mesmo, sendo ele:{plano.upper()}")
        mostrar_coberturas(plano)

        relato = input("Descreva para mim o que está ocorendo: ")
        categoria = classificar_descricao(relato)

        if categoria in planos[plano]:
            print(f"\n🧠 Pelas suas infomações passadas, iremos acionar o seguro baseado nessa categoria: {nomes_amigaveis.get(categoria, categoria)}")
            print(f"\n Segue seu código de protocolo: {protocolo}.")
            print("\n✅ Seguro acionado, equipe notificada e a caminho! Entraremos em contato para mais informações.")
        else:
            print("\n❌ Ops! Essa situação não está coberto em seu plano, mas entre agora em contato com o numero 0800 9380 13452. para que possamos resolver o mais rápido possivel")

        opcao = input("\nDeseja realizar uma nova triagem? (s para sim / n para parar): ").lower()
        if opcao != 's':
            print("Obrigado pelo atendimento. Até logo!")
            break

if __name__ == "__main__":
    triagem()
