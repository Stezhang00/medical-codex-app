from fastapi import FastAPI

app = FastAPI()

@app.get("/icd")
def get_icd_codes():
    return {"icd_codes": ["A00.0", "A00.1", "A00.9"]}

@app.get("/cpt")
def get_cpt_codes():
    return {"cpt_codes": ["10030", "10035", "10040"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
