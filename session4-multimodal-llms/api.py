
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer
import io

app = FastAPI()

# Load the pre-trained model and tokenizer
model = AutoModel.from_pretrained('openbmb/MiniCPM-V-2_6-int4', trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-V-2_6-int4', trust_remote_code=True)
model.eval()

class TextInput(BaseModel):
    inputs: str

@app.post("/generate_text")
async def generate_text(data: TextInput):
    try:
        msgs = [{'role': 'user', 'content': [data.inputs]}]
        response = model.chat(image=None, msgs=msgs, tokenizer=tokenizer)
        return JSONResponse(content={"generated_text": response})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate_text_image")
async def generate_text_image(file: UploadFile = File(...), prompt: str = None):
    try:
        image_content = await file.read()
        image = Image.open(io.BytesIO(image_content)).convert('RGB')

        msgs = [{'role': 'user', 'content': [image, prompt]}]
        response = model.chat(image=None, msgs=msgs, tokenizer=tokenizer)
        return JSONResponse(content={"generated_text": response})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "MiniCPM-V-2_6-int4 API is running"}