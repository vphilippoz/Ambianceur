import pygame
import time
import parameters as p

def initialize() -> None:
    """
    Initialize the music playback system.
    """
    pygame.mixer.init() # Initialize the pygame mixer

def finalize() -> None:
    """
    Finalize the music playback system.
    """
    pygame.mixer.quit() # Quit the pygame mixer

def load() -> str:
    """
    Load a random music file from the music folder

    Return: the path to the selected music file.
    """
    import os
    import random

    music_files = [f for f in os.listdir(p.MUSIC_FOLDER) if f.endswith(".mp3")] #Or other formats
    if not music_files:
        raise FileNotFoundError(f"No music files found in {p.MUSIC_FOLDER}")

    music_path = random.choice(music_files)
    return os.path.join(p.MUSIC_FOLDER, music_path)

def play(music_path: str) -> None:
    """
    Play the specified music file.
    
    Args:
        music_path: Path to the music file to play.
    """
    global music_playing, start_time

    try:
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play()
        music_playing = True
        start_time = time.time()
        if p.VERBOSE: print(f"Playing {music_path}")
    except Exception as e:
        if p.VERBOSE: print(f"Error playing music: {e}")

def stop() -> None:
    """
    Stop the music playback.
    """
    global music_playing
    pygame.mixer.music.stop()
    music_playing = False
    if p.VERBOSE: print("Stopping music")