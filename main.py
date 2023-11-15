import uvicorn
from config import get_settings
from fastapi import FastAPI, HTTPException
from reader import read_csv
from statistics import calculate_average_statistic, calculate_statistics

app = FastAPI()
settings = get_settings()
data = read_csv(settings.csv_file, encoding=settings.csv_encoding)
average_stats = calculate_average_statistic(data)
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=settings.port, reload=False)


@app.get("/")
async def root():
    return {"message": "☁☁卌☁☁"}


@app.get("/stats/player/{name}")
async def stats(name: str):
    stats = calculate_statistics(average_stats.get(name, None), name)
    if stats is not None:
        return stats
    raise HTTPException(status_code=404, detail="Player not found")
