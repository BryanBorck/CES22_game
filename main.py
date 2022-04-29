from turtle import bgpic
import pygame, sys
from button import Button
import our_game

pygame.init()

SCREEN = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0])
pygame.display.set_caption("Menu")
WIDTH = pygame.display.get_desktop_sizes()[0][0]
HEIGHT = pygame.display.get_desktop_sizes()[0][1]
scaler = HEIGHT/720

BG = pygame.image.load("assets/menu/backformation_2.png")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/OCRAEXT.TTF", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")

        BG = pygame.image.load("assets/menu/backoptions.jpg")
        BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

        SCREEN.blit(BG, (0,0))

        PLAY_TEXT1 = get_font(45).render("- Aperte SPACE para pular.", True, "Black")
        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(WIDTH/2, 100*scaler))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)

        PLAY_TEXT2 = get_font(45).render("- Aperte <- para esquerda e -> para direita.", True, "Black")
        PLAY_RECT2 = PLAY_TEXT2.get_rect(center=(WIDTH/2, 200*scaler))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)

        PLAY_TEXT3 = get_font(45).render("- Aperte ESC para pausar.", True, "Black")
        PLAY_RECT3 = PLAY_TEXT3.get_rect(center=(WIDTH/2, 300*scaler))
        SCREEN.blit(PLAY_TEXT3, PLAY_RECT3)

        PLAY_TEXT4 = get_font(45).render("- Elimine o inimigo pulando em cima dele!", True, "White")
        PLAY_RECT4 = PLAY_TEXT4.get_rect(center=(WIDTH/2, 400*scaler))
        SCREEN.blit(PLAY_TEXT4, PLAY_RECT4)

        PLAY_TEXT5 = get_font(45).render("- Colete todas as 5 estrelas para passar de fase!", True, "White")
        PLAY_RECT5 = PLAY_TEXT5.get_rect(center=(WIDTH/2, 500*scaler))
        SCREEN.blit(PLAY_TEXT5, PLAY_RECT5)


        PLAY_BACK = Button(image=None, pos=(WIDTH/2, 650*scaler), 
                             text_input="Entendi!", font=get_font(75), base_color="White", hovering_color="Black")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    game = our_game.Game()
                    game.start()
                    game.loop()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("White")

        BG = pygame.image.load("assets/menu/backoptions.jpg")
        BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

        SCREEN.blit(BG, (0,0))

        OPTIONS_SOUND = Button(image=None, pos=(pygame.display.get_desktop_sizes()[0][0]/2, 100), 
                            text_input="Ativar/Desativar som", font=get_font(45), base_color= "White", hovering_color="Black")

        OPTIONS_CHARACTER = Button(image=None, pos=(WIDTH/2, 300*scaler), 
                            text_input="Mudar Personagem", font=get_font(45), base_color= "White", hovering_color="Black")
        
        OPTIONS_BACK = Button(image=None, pos=(WIDTH/2, 520*scaler), 
                            text_input="VOLTAR", font=get_font(75), base_color= "White", hovering_color="Black")

        OPTIONS_SOUND.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_CHARACTER.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_SOUND.update(SCREEN)
        OPTIONS_CHARACTER.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("NICK'S HARDEST ADVENTURE", True, our_game.GOIABA)
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH/2, 100*scaler))

        PLAY_BUTTON = Button(image=None, pos=(WIDTH/2, 250*scaler), 
                            text_input="JOGAR", font=get_font(80), base_color="White", hovering_color= our_game.DARK_BLUE)
        OPTIONS_BUTTON = Button(image=None, pos=(WIDTH/2, 400*scaler), 
                            text_input="OPÇÕES", font=get_font(80), base_color="White", hovering_color= our_game.DARK_BLUE)
        QUIT_BUTTON = Button(image=None, pos=(WIDTH/2, 550*scaler), 
                            text_input="SAIR", font=get_font(80), base_color="White", hovering_color= our_game.DARK_BLUE)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()