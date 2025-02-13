## Create Caso válido
def test_create_task(client):
    # Cria tarefas 
    task_data = {"task": "Test Task", "status": False}
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 201

    response_data = response.json()
    assert "id" in response_data
    assert response_data["task"] == "Test Task"
    assert response_data["status"] is False

## Get Caso válido
def test_get_tasks(client):
    # Cria tarefas 
    task_data = {"task": "Test Task", "status": False}
    client.post("/tasks/", json=task_data)
    task_data = {"task": "new", "status": True}
    client.post("/tasks/", json=task_data)

    response = client.get("/tasks/")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 2
    assert tasks[0]["task"] == "Test Task"
    assert tasks[0]["status"] is False
    assert tasks[1]["task"] == "new"
    assert tasks[1]["status"] is True

## Delete Caso válido
def test_delete_task(client):
    # Cria tarefas 
    task_data = {"task": "Test Task", "status": False}
    response = client.post("/tasks/", json=task_data)
    task_id = response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204

    # Verifica se a tarefa foi removida
    response = client.get("/tasks/")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 0

    # Caso inválido Tarefa nao encontrada
    response = client.delete("/tasks/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}

## Put Caso Valido
def test_update_task(client):
    # Cria uma tarefa para testar
    task_data = {"task": "Test Task", "status": False}
    response = client.post("/tasks/", json=task_data)
    task_id = response.json()["id"]

    updated_data = {"task": "Updated Task", "status": True}
    response = client.put(f"/tasks/{task_id}", json=updated_data)
    assert response.status_code == 200

    # Verifica se a tarefa foi atualizada
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    task = response.json()
    assert task["task"] == "Updated Task"
    assert task["status"] is True

    # Caso inválido Tarefa nao encontrada
    response = client.put("/tasks/999", json=updated_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}

## Patch Caso válido
def test_complete_task(client):
    # Cria uma tarefa para testar
    task_data = {"task": "Test Task", "status": False}
    response = client.post("/tasks/", json=task_data)
    task_id = response.json()["id"]

    response = client.patch(f"/tasks/{task_id}/complete")
    assert response.status_code == 200

    # Verifica se a tarefa foi marcada como concluída
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    task = response.json()
    assert task["status"] is True

    # Caso inválido Tarefa nao encontrada
    response = client.patch("/tasks/999/complete")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}