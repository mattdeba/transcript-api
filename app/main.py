from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI(
    title="YouTube Transcript API",
    description="Une API simple pour récupérer la transcription d'une vidéo YouTube",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API de transcription YouTube !"}

@app.get("/transcript/{video_id}/{lang}")
def get_transcript(video_id: str, lang: str):
    """
    Récupère la transcription d'une vidéo YouTube via son ID
    """
    try:
        ytt_api = YouTubeTranscriptApi()
        res = ytt_api.fetch(video_id, languages=[lang])
        final_text = []
        for snippet in res:
            final_text.append(snippet.text)
        return {"video_id": video_id, "transcript": final_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur : {str(e)}")
