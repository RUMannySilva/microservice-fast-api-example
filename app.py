#!/usr/bin/env python3
"""
FastAPI Programming Joke Generator
A web API that serves clean, family-friendly programming jokes.
"""

from fastapi import FastAPI, Security, HTTPException, status
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
import random
import uvicorn
import os

# Initialize FastAPI app
app = FastAPI(
    title="Programming Joke Generator API",
    description="A simple API that serves random programming jokes",
    version="1.0.0"
)

# API Key Configuration
# You can set this via environment variable: export AUTH_KEY=your-secret-key
API_KEY = os.getenv("AUTH_KEY", "your-secret-api-key-12345")
API_KEY_NAME = "X-API-Key"

# Create API key header dependency
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def verify_api_key(api_key: str = Security(api_key_header)):
    """
    Verify the API key from the request header.
    
    Args:
        api_key: The API key from the X-API-Key header
        
    Returns:
        str: The API key if valid
        
    Raises:
        HTTPException: If API key is missing or invalid
    """
    if api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing API Key. Please provide X-API-Key header.",
        )
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key.",
        )
    return api_key


def get_jokes():
    """
    Returns a list of clean, family-friendly programming and nerd jokes.
    
    Returns:
        list: A list of joke strings
    """
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        
        "How do you comfort a JavaScript bug? You console it!",
        
        "Why did the programmer quit his job? He didn't get arrays!",
        
        "What's a programmer's favorite hangout place? Foo Bar!",
        
        "Why do Python programmers prefer snakes? Because they're great at wrapping things up!",
        
        "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
        
        "Why did the developer go broke? Because he used up all his cache!",
        
        "What do you call a programmer from Finland? Nerdic!",
        
        "Why don't programmers like nature? It has too many bugs!",
        
        "What's the object-oriented way to become wealthy? Inheritance!",
        
        "Why did the programmer get stuck in the shower? The instructions said: 'Lather, Rinse, Repeat.'",
        
        "How do you know if a programmer is an extrovert? They look at YOUR shoes when talking to you!",
        
        "Why do Java developers wear glasses? Because they can't C#!",
        
        "What's a programmer's favorite snack? Cookies! (The web kind)",
        
        "Why did the SQL query break up with the database? There was no connection!",
        
        "What do you call a programmer who doesn't comment code? A future job applicant!",
        
        "Why do programmers always mix up Halloween and Christmas? Because Oct 31 == Dec 25!",
        
        "What's a computer's favorite beat? An algo-rhythm!",
        
        "Why did the developer go to the doctor? Because he had a case of the runs (infinite loops)!",
        
        "What's a programmer's favorite type of music? Algo-rhythm and blues!",

        "Why do programmers prefer dark mode? Because light attracts bugs!",
        
        "How do you comfort a JavaScript bug? You console it!",
        
        "Why did the programmer quit his job? He didn't get arrays!",
        
        "What's a programmer's favorite hangout place? Foo Bar!",
        
    ]
    
    return jokes


@app.get("/")
async def root():
    """
    Root endpoint that provides API information.
    Note: This endpoint is public and does not require authentication.
    """
    return {
        "message": "Welcome to the Programming Joke Generator API!",
        "endpoints": {
            "/joke": "Get a random joke (requires API key)",
            "/jokes": "Get all jokes (requires API key)",
            "/health": "Health check (public)",
            "/docs": "Interactive API documentation"
        },
        "authentication": "Use X-API-Key header for protected endpoints"
    }


@app.get("/joke")
async def get_random_joke(api_key: str = Security(verify_api_key)):
    """
    Returns a randomly selected joke from the collection.
    Requires API key authentication via X-API-Key header.
    
    Returns:
        dict: A JSON object containing the joke
    """
    jokes = get_jokes()
    selected_joke = random.choice(jokes)
    
    return {
        "joke": selected_joke,
        "total_jokes": len(jokes)
    }


@app.get("/jokes")
async def get_all_jokes(api_key: str = Security(verify_api_key)):
    """
    Returns all jokes in the collection.
    Requires API key authentication via X-API-Key header.
    
    Returns:
        dict: A JSON object containing all jokes
    """
    jokes = get_jokes()
    
    return {
        "jokes": jokes,
        "total_jokes": len(jokes)
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the API is running.
    
    Returns:
        dict: Status information
    """
    return {
        "status": "healthy",
        "service": "Programming Joke Generator API"
    }


if __name__ == "__main__":
    # Run the application on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)

