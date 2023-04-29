from fastapi import FastAPI

app = FastAPI()

icd10am = {
    "A00": "Cholera",
    "A01": "Typhoid fever",
    "A02": "Salmonella infections",
    "B00": "Herpesviral [herpes simplex] infections",
    # more codes and descriptions here...
}

snomedct = {
    "105590001": "Malignant neoplasm of lung",
    "105596006": "Malignant neoplasm of colon",
    "105602007": "Malignant neoplasm of breast",
    # more codes and descriptions here...
}

@app.get("/icd10am/{code}")
def get_icd10am(code: str):
    return {"code": code, "description": icd10am.get(code, "Code not found")}

@app.get("/snomedct/{code}")
def get_snomedct(code: str):
    return {"code": code, "description": snomedct.get(code, "Code not found")}
