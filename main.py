from fastapi import FastAPI

app = FastAPI()

@app.get("/medical-codex-1")
def get_medical_codex_1():
    return {"codex": "Medical Codex 1"}

@app.get("/medical-codex-2")
def get_medical_codex_2():
    return {"codex": "Medical Codex 2"}

