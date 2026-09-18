from fastapi import FastAPI

app = FastAPI(
    title="SkillSwap API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "SkillSwap está funcionando corretamente."}