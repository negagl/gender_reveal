import gender_guesser.detector as gender
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()

detector = gender.Detector()


@app.get("/", response_model=dict, status_code=200)
def home() -> dict:
    return JSONResponse(status_code=200, content={"Hello": "World"})


@app.get('/detect_gender/{name}', response_model=dict, status_code=200)
def detect_gender(name) -> dict:
    gender = detector.get_gender(name)
    resp = {"name": name, "gender": gender}
    return JSONResponse(status_code=200, content=resp)


@app.post('/detect_genders/', response_model=List[dict], status_code=200)
def detect_genders(names: list) -> List[dict]:
    print('Names =>', names)
    ret = [{}]
    for name in names:
        gender = detector.get_gender(name)
        resp = {"name": name, "gender": gender}
        ret.append(resp)
    return JSONResponse(status_code=200, content=ret)
