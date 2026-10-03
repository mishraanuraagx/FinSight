from fastapi import FastAPI
from app.routes import data, models, predict

app = FastAPI(
    title="FinSight API",
    description="Financial Insights and Prediction APIs",
    version="0.1",
)

# Routers
app.include_router(data.router, prefix="/data")
app.include_router(models.router, prefix="/models")
app.include_router(predict.router, prefix="/predict")
