
import telebot

bot = telebot.TeleBot('6699313892:AAEKeme8ciec__LZ2m-mRAk7-bfRWZ9RHY0')

@bot.message_handler(commands=["start"])
def start(mensagem):
    texto = "Olá! Bem-vindo ao bot do Cauan. Escolha uma opção:\n" \
            "/pizza - Pizza\n" \
            "/hamburguer - Hambúrguer\n" \
            "/salada - Salada"
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza para sua casa. Tempo de espera: 20 minutos.")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o Brabo! Em 10 minutos chega aí.")

@bot.message_handler(commands=["salada"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Não tem salada não. Clique aqui para iniciar: /start")

@bot.message_handler(func=lambda message: True)
def opcao1(mensagem):
    texto = "O que você quer? (Clique em uma opção)\n" \
            "/pizza - Pizza\n" \
            "/hamburguer - Hambúrguer\n" \
            "/salada - Salada"
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para reclamacao@example.com")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu! Cauan mandou um abraço de volta")

bot.polling()
