# 📘 Assignment: Testes de APIs com FastAPI

## 🎯 Objective

Aprenda a testar endpoints de uma API FastAPI com `pytest` e `TestClient`, verificando respostas, códigos HTTP e tratamento de erros sem depender de um banco de dados ou ORM.

## 📝 Tasks

### 🛠️ Preparar o cliente de testes

#### Descrição
Configure o ambiente de testes e use o cliente de testes do FastAPI para verificar o endpoint de saúde fornecido na aplicação.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `pip install fastapi uvicorn pytest httpx`.
- Criar uma fixture que disponibilize `TestClient` para os testes.
- Testar `GET /health` e verificar o status HTTP `200` e o conteúdo JSON esperado.
- Executar os testes com `pytest -q`.

### 🛠️ Testar operações de tarefas

#### Descrição
Escreva testes automatizados para os endpoints CRUD da API de tarefas, verificando o fluxo de criação, consulta, atualização e remoção.

#### Requisitos
O programa concluído deve:

- Testar `POST /tasks` e verificar o status `201`, o título, a descrição e o identificador da tarefa criada.
- Testar `GET /tasks` e `GET /tasks/{task_id}` para verificar a listagem e a consulta de tarefas.
- Testar `PUT /tasks/{task_id}` e confirmar que os dados da tarefa foram atualizados.
- Testar `DELETE /tasks/{task_id}` e confirmar que a tarefa foi removida.
- Isolar os testes para que dados criados em um teste não afetem os demais.

### 🛠️ Verificar erros e validação

#### Descrição
Complete a suíte testando requisições inválidas e identificadores inexistentes para garantir respostas previsíveis da API.

#### Requisitos
O programa concluído deve:

- Verificar que consultar, atualizar ou remover uma tarefa inexistente retorna `404 Not Found`.
- Verificar que uma requisição sem o título obrigatório retorna `422 Unprocessable Entity`.
- Confirmar que os testes de erro verificam tanto o status HTTP quanto a resposta recebida.
