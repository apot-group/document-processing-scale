from fastapi import FastAPI
import uvicorn
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


app = FastAPI(title="PROJECT_NAME", openapi_url="/api/openapi.json", docs_url="/api/docs")
sid = SentimentIntensityAnalyzer()

@app.post("/predict")    
def predict(data: str):
    data = str({"data": data})
    result = sid.polarity_scores(data)
    return result
 

if __name__ == "__main__":
    uvicorn.run("main:app",host='0.0.0.0', port=3030, reload=True, debug=True)