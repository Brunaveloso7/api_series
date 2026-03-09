from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Olá, mundo"}

@app.get("/itens/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/soma/{num1}/{num2}")
def soma(num1: int, num2: int):
    return {"resultado": num1 + num2}



#Crie uma rota que retorne a soma de dois números passados por caminho (path de url)

#Extra: melhore a tipagem do código usando tipos do módulo typing onde for necessário

