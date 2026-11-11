def responder(mensagem):
    mensagem = mensagem.lower()

    if "pedido" in mensagem:
        return "Para consultar seu pedido, informe o número."

    elif "produto" in mensagem:
        return "Qual produto você está procurando?"

    return "Olá! Sou o SmartSupport AI. Como posso ajudar?"


print("=== SmartSupport AI ===")

while True:
    mensagem = input("Você: ")

    if mensagem.lower() == "sair":
        break

    print("Bot:", responder(mensagem))