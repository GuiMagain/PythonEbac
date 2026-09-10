from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional



app = FastAPI()

tarefas = []

def encontra_tarefa(id_tarefa: int):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            return tarefa
    return None

@app.post("/adiciona")
def post_tarefas(id_tarefa: int, nome_tarefa: str, descricao_tarefa: str, concluida: bool = False):
    if encontra_tarefa(id_tarefa) is not None:
        raise HTTPException(status_code=400, detail="Tarefa já existe!")
    tarefas.append({
        "id": id_tarefa,
        "nome": nome_tarefa,
        "descricao": descricao_tarefa,
        "concluida": concluida
    })
    return {"message": "Tarefa adicionada com sucesso!"}

@app.get("/tarefas")
def get_tarefas():
    if not tarefas:
        return {"message": "Não existe nenhuma tarefa criada!"}
    else:
        return {"tarefas": tarefas}

@app.put("/atualiza/{id_tarefa}")
def put_tarefas(id_tarefa: int, concluida: bool = None):
    tarefa = encontra_tarefa(id_tarefa)
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada!")
    if concluida is not None:
        tarefa["concluida"] = concluida
        return {
            "message": "Status da tarefa atualizado com sucesso!",
            "tarefa_atualizada": tarefa
        }

@app.delete("/deletar/{id_tarefa}")
def delete_tarefa(id_tarefa: int):
    tarefa = encontra_tarefa(id_tarefa)
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada!")
    else:
        tarefas.remove(tarefa)
        return {"message": "tarefa deletada com sucesso!"}
