import pygame
import random
from pyvidplayer2 import Video

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

##########################################################################################################################
#ChatBot 

template = """
Answer the question below. 

Here is the conversation history : {context}

Question : {question}

"""

model = OllamaLLM(model = "gemma4")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model 

firstRun = True

def handle_conversation() :
    global firstRun
    context = "You are BMO from adventure time, a robot friend that has a very unique personality! Do not use any emojis or emoticons in your responses. Only written words!"
    
    if firstRun :
        print("Hello there! Press my red button to start speaking and then press my green button when you have finished talking. " \
        "If you wanna play a game you can press my triangle button!")
        firstRun = False
    while True : 
        screen.blit(faces[9], (0,0))
        pygame.display.flip()
        user_input = input("You : ")
        if user_input.lower() == "exit" : 
            break
        screen.blit(faces[14], (0,0))
        pygame.display.flip()
        result = chain.invoke({"context" : context, "question" : user_input})
        print(result)
        context += f"\nUser : {user_input}\nAI : {result}"

##########################################################################################################################

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("BMO")
logo = pygame.image.load('BMO png.png')
pygame.display.set_icon(logo)

#BMO vid
video = Video("A Normal Day at Work.mp4")
video.resize((800,480))
window = pygame.display.set_mode(video.current_size)

#BMO faces
faces = [pygame.image.load("bmo1.jpg"), pygame.image.load("bmo2.jpg"), pygame.image.load("bmo3.jpg"), pygame.image.load("bmo4.jpg"), 
         pygame.image.load("bmo6.jpg"), pygame.image.load("bmo7.jpg"), pygame.image.load("bmo9.jpg"), pygame.image.load("bmo15.jpg"), 
         pygame.image.load("bmo16.jpg"), pygame.image.load("bmo17.jpg"), pygame.image.load("bmo18.jpg"), pygame.image.load("bmo19.jpg"), 
         pygame.image.load("bmo20.jpg"), pygame.image.load("bmo21.jpg"), pygame.image.load("bmo22.jpg"), pygame.image.load("bmo23.jpg"), 
         pygame.image.load("bmo24.jpg")]
# screen.blit(random.choice(faces), (0,0))
# pygame.display.flip()

#timer event
# timer = pygame.time.Clock()
# ChangeFace = pygame.USEREVENT + 1
# pygame.time.set_timer(ChangeFace, 2000)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a :
                handle_conversation()
        # if event.type == ChangeFace:
        #     screen.blit(random.choice(faces), (0,0))
        #     pygame.display.flip()
    if video.draw(window, (0, 0)):    #these 2 lines are needed if video background
        pygame.display.update()

# Quit Pygame
pygame.quit()