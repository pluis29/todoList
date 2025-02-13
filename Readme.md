# ToDo List API
API simples para gerenciamento de tarefas, desenvolvida como parte de um teste de conhecimento. A aplicação permite criar, listar, atualizar, marcar como concluída e deletar tarefas. Além disso, possui um sistema básico de monitoramento com Prometheus para coleta de métricas.

#
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Endpoints da API](#endpoints-da-api)
- [Monitoramento](#monitoramento)
- [Sugestões de Consultas Úteis no Prometheus](#sugestões-de-consultas-úteis-no-prometheus)
    - [Exemplos de Consultas no Prometheus](#exemplos-de-consultas-no-prometheus)
- [Testes](#testes)
    - [Executando os Testes](#executando-os-testes)
## Tecnologias Utilizadas
- **Python**: Linguagem principal.
- **FastAPI**: Framework para construção da API.
- **SQLite**: Banco de dados para armazenamento local.
- **Prometheus**: Coleta de métricas da aplicação.
- **Docker**: Containerização da aplicação.
- **Pytest**: Framework para testes unitários e de integração.





## Como Executar o Projeto
- Clone o repositório:
    ```bash
    git clone https://github.com/pluis29/todoList.git todoList
    ```
- Dentro do diretório, crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

- Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
- Inicialize os containers:
    ```bash
    docker compose up --build
    ```
- Após isso, você poderá acessar a API pelo endereço *`http://localhost:8000/`*.
- A documentação interativa da API (Swagger UI) estará em *`http://localhost:8000/docs`*.
- Acesse o Prometheus em *`http://localhost:9090`*.
  


## Endpoints da API
Abaixo estão os endpoints disponíveis na API, com exemplos de requisições e respostas.


| Método   | Endpoint               | Descrição                      |
|----------|------------------------|--------------------------------|
| `GET`    | `/tasks/`              | Lista todas as tarefas.        |
| `GET`    | `/tasks/{id}`          | Obtém os detalhes de uma tarefa específica. |
| `POST`   | `/tasks/`              | Cria uma nova tarefa.          |
| `PUT`    | `/tasks/{id}`          | Atualiza os dados de uma tarefa existente. |
| `DELETE` | `/tasks/{id}`          | Remove uma tarefa do banco de dados. |
| `PATCH`  | `/tasks/{id}/complete` | Marca uma tarefa como concluída. |
| `GET`    | `/metrics`             | Retorna métricas da aplicação para monitoramento com Prometheus. |

Para exemplos completos de requests e responses, acesse a documentação interativa da API em ***Swagger UI*** *`http://localhost:8000/docs`*.
 
## Monitoramento

A aplicação expõe métricas no endpoint ***/metrics***, que são coletadas pelo Prometheus.
- Para visualizar as métricas, acesse o Prometheus em *`http://localhost:9090`*.

### Sugestões de Consultas Úteis no Prometheus

A seguir estão algumas consultas úteis para monitorar o desempenho e o comportamento:

- **`http_requests_total`**: Total de requisições HTTP, categorizadas por método, endpoint e código de status.
- **`http_request_duration_seconds`**: Duração das requisições em segundos.
- **`http_response_size_bytes`**: Tamanho das respostas em bytes.

#### Exemplos de Consultas no Prometheus

1. **Número total de requisições**:
   ```promql
   http_requests_total
   ```
2. **Tempo médio de resposta**:
   ```promql
   rate(http_request_duration_seconds_sum[1m]) / rate(http_request_duration_seconds_count[1m])
   ```
3. **Tamanho médio das respostas**:
   ```promql
   rate(http_response_size_bytes_sum[1m]) / rate(http_response_size_bytes_count[1m])
   ```


## Testes
O projeto inclui testes unitários e de integração.
- **Testes unitários**: Verificam a lógica das funções do CRUD e Schema.
- **Testes de integração**: Verificam os endpoints da API e a interação com o banco de dados.

#### Executando os Testes
Para executar todos os testes, use o seguinte comando:
```bash
chmod +x run_tests.sh
./run_tests.sh
``` 
