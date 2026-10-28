# 📘 Atividade: Jogo da Forca em Python

## 🎯 Objetivo

Pratique manipulação de strings, listas, seleção aleatória, laços de repetição e condicionais ao criar um jogo da Forca. O jogador deverá descobrir uma palavra secreta antes de esgotar as tentativas.

## 📝 Tarefas

### 🛠️ Preparar a Palavra Secreta e os Palpites

#### Descrição
Use a lista de palavras fornecida no código inicial para escolher uma palavra secreta aleatoriamente e preparar as variáveis que acompanharão o progresso do jogo.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra da lista usando o módulo `random`.
- Manter o registro das letras já descobertas pelo jogador.
- Definir o limite de palpites incorretos e iniciar o contador de erros.
- Exibir as letras descobertas e ocultar as demais usando `_` (por exemplo, `_ _ _ _`).

### 🛠️ Implementar o Jogo da Forca

#### Descrição
Crie o loop principal do jogo para receber palpites, atualizar o progresso e encerrar a partida quando o jogador vencer ou esgotar as tentativas.

#### Requisitos
O programa concluído deve:

- Solicitar um palpite de letra ao jogador a cada rodada.
- Revelar as posições correspondentes quando a letra estiver na palavra secreta.
- Contabilizar palpites incorretos e informar quantas tentativas restam.
- Encerrar o jogo quando todas as letras forem descobertas ou o limite de erros for atingido.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra secreta.
