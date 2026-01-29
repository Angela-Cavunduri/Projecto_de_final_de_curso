from fastapi import FastAPI

app = FastAPI(
    title="Troca Fácil API",
    description="Backend do sistema Troca Fácil",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Backend do Troca Fácil está a funcionar"}
