from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Succesfully deployed simple app on AKS Cluster"}
