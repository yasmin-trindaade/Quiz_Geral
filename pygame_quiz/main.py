import pygame
import requests

pygame.init()

# Configurações da tela
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Educacional")

# Fonte
font = pygame.font.Font(None, 36)

# Função para exibir o texto
def exibir_texto(texto, x, y):
    render = font.render(texto, True, (255, 255, 255))
    tela.blit(render, (x, y))

# Função para salvar o ranking no Django via API
def salvar_ranking(nome, pontos):
    url = 'http://127.0.0.1:8000/salvar_ranking/'
    dados = {'nome': nome, 'pontos': pontos}
    resposta = requests.post(url, data=dados)
    if resposta.status_code == 200:
        print('Ranking salvo com sucesso!')
    else:
        print('Erro ao salvar ranking.')

# Função para exibir as perguntas
def jogar():
    perguntas = [
        {"pergunta": "Qual é a capital do Brasil?", "opcoes": ["Brasília", "Rio", "São Paulo", "BH"], "correta": "Brasília"},
        {"pergunta": "2 + 2 é igual a?", "opcoes": ["4", "22", "5", "3"], "correta": "4"},
        {"pergunta": "Quem descobriu o Brasil?", "opcoes": ["Cabral", "Colombo", "Napoleão", "Nero"], "correta": "Cabral"},
    ]
    pontos = 0

    for pergunta in perguntas:
        tela.fill((0, 0, 0))  # Limpar a tela
        exibir_texto(pergunta["pergunta"], 100, 100)

        botoes = []
        for i, opcao in enumerate(pergunta["opcoes"]):
            botao = pygame.Rect(100, 200 + i * 60, 600, 40)
            botoes.append(botao)
            pygame.draw.rect(tela, (100, 100, 255), botao)
            exibir_texto(opcao, 120, 210 + i * 60)

        pygame.display.flip()

        resposta = None
        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    for i, botao in enumerate(botoes):
                        if botao.collidepoint(pygame.mouse.get_pos()):
                            resposta = pergunta["opcoes"][i]
                            rodando = False

        if resposta.lower() == pergunta["correta"].lower():
            pontos += 1

    salvar_ranking("Jogador", pontos)
    print(f"Você fez {pontos} pontos!")

# Iniciar o jogo
if __name__ == "__main__":
    jogar()
    pygame.quit()
