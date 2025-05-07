# EXC 21 - Faça um programa em Python que abra e reproduza o áudio de um arquivo .mp3

import time
import pygame

# Inicializa o Mixer do Pygame
pygame.mixer.init()

# Caminho do arquivo
meu_audio = "assets/low-taper-fade.mp3"

# Carregando e tocando a música
pygame.mixer.music.load(meu_audio)
pygame.mixer.music.play()

print('Tocando audio...')

# Mantém o programa em funcionamento
while pygame.mixer.music.get_busy():
    time.sleep(1)

print('Audio finalizado')
