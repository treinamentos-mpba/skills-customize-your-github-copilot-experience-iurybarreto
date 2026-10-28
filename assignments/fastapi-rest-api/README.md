# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma API REST com FastAPI, definindo rotas HTTP, validando dados com modelos e implementando operações CRUD para gerenciar tarefas.

## 📝 Tasks

### 🛠️ Criar e executar a aplicação

#### Descrição
Complete o endpoint de verificação de saúde no código inicial e execute a aplicação FastAPI localmente para explorar a documentação interativa. Instale as dependências com `pip install fastapi uvicorn` e inicie o servidor com `uvicorn starter-code:app --reload`.

#### Requisitos
O programa concluído deve:

- Criar um endpoint `GET /health` que retorne um JSON indicando que a API está funcionando.
- Iniciar a aplicação com Uvicorn e permitir acesso à documentação em `/docs`.
- Retornar uma resposta JSON válida ao acessar `GET /health`.

### 🛠️ Criar e listar tarefas

#### Descrição
Implemente as rotas para cadastrar tarefas e listar as tarefas armazenadas durante a execução da aplicação. Use o modelo Pydantic fornecido para validar os dados de entrada.

#### Requisitos
O programa concluído deve:

- Criar uma rota `POST /tasks` que receba um título e uma descrição e retorne a tarefa criada com um identificador.
- Retornar o status HTTP `201 Created` ao cadastrar uma tarefa.
- Criar uma rota `GET /tasks` que retorne todas as tarefas cadastradas.
- Manter as tarefas em memória enquanto a aplicação estiver em execução.

### 🛠️ Consultar, atualizar e remover tarefas

#### Descrição
Complete as operações de gerenciamento de uma tarefa específica usando seu identificador e trate os casos em que ela não existir.

#### Requisitos
O programa concluído deve:

- Criar uma rota `GET /tasks/{task_id}` que retorne a tarefa correspondente.
- Criar uma rota `PUT /tasks/{task_id}` que atualize o título e a descrição da tarefa.
- Criar uma rota `DELETE /tasks/{task_id}` que remova a tarefa.
- Retornar o status HTTP `404 Not Found` quando o identificador não corresponder a uma tarefa cadastrada.
