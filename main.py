import os
import pygame as pg


symbole_j_1 = 1
symbole_j_2 = 2

score_j_1 = 0
score_j_2 = 0

pg.init() #initialisation du module pygame
noir=(0,0,0)
blanc=(255,255,255)
fond_game=(20, 189, 172)
cross_color= (84, 84, 84)
circle_color = (242, 235, 211)
logo = pg.image.load(r"data\OIP32x29.jpg")
pg.display.set_icon(logo)
pg.display.set_caption("Tic Tac Toe")
fonte = pg.font.Font("freesansbold.ttf", 12)
fonte_score = pg.font.Font("freesansbold.ttf", 16)
fonte_victory_screen = pg.font.Font("freesansbold.ttf", 32)

screen = pg.display.set_mode((400,400)) #création de la fenêtre d'affichage en 400 * 400
clock = pg.time.Clock()

#définition des dimensions des sections
header_height = 50
footer_height = 50
main_height = 400 - header_height - footer_height
rejouer_button_rect = pg.Rect(0, 0, 100, footer_height-5)
# surface object
header_surface = pg.Surface((400, header_height))
header_left_surface = header_surface.subsurface((0, 0, header_surface.get_width() // 2, header_surface.get_height()))
header_right_surface = header_surface.subsurface((header_surface.get_width() // 2, 0, header_surface.get_width() // 2, header_surface.get_height()))

main_surface = pg.Surface((400, main_height))
footer_surface = pg.Surface((400, footer_height))
texte = fonte.render("texte", True, noir)

def button_replay():
    rejouer_button_rect = pg.Rect(200 - (100 //2), 350, 100, 70)
    pg.draw.rect(screen, (255, 255, 255), (rejouer_button_rect))
    text = fonte.render("Rejouer", True, fond_game)
    text_rect_button = text.get_rect(center=rejouer_button_rect.center)
    screen.blit(text, text_rect_button)
    return rejouer_button_rect

def draw_header_footer():
    header_surface.fill(blanc)  # Fond blanc pour le header
    footer_surface.fill(blanc)  # Fond blanc pour le footer

def draw_grille():
    
    pg.draw.line(main_surface, noir, (150, 0), (150, 300), 5)
    pg.draw.line(main_surface, noir, (250, 0), (250, 300), 5)
    pg.draw.line(main_surface, noir, (50, 100), (350, 100), 5)
    pg.draw.line(main_surface, noir, (50, 200), (350, 200), 5)



joueur_actuel = 1
grille =   [[0, 0, 0], 
            [0, 0, 0], 
            [0, 0, 0]]
victoire = False
match_nul = False

def game_rules():
        global victoire, match_nul, score_j_1, score_j_2, winner_is
        for ligne in range (3):
            if grille[ligne][0] == grille[ligne][1] == grille[ligne][2] != 0:
                print (f"victoire en ligne du joueur {joueur_actuel}")
                victoire = True
                if joueur_actuel == 1:
                    score_j_1 += 1
                    winner_is = 1
                else:
                    score_j_2 += 1
                    winner_is = 2

        for colonne in range (3):
            if grille[0][colonne] == grille[1][colonne] == grille[2][colonne] != 0:
                print (f"victoire en colonne du joueur {joueur_actuel}")
                victoire = True
                if joueur_actuel == 1:
                    score_j_1 += 1
                    winner_is = 1
                else:
                    score_j_2 += 1
                    winner_is = 2
        
        
        if grille [0][0] == grille [1][1] == grille [2][2] !=  0:
            print (f"victoire en diagonnale du joueur {joueur_actuel}")
            victoire = True
            if joueur_actuel == 1:
                score_j_1 += 1
                winner_is = 1
            else:
                score_j_2 += 1
                winner_is = 2
    
        if grille [0][2] == grille [1][1] == grille [2][0] != 0:
            print (f"victoire en diagonnale du joueur {joueur_actuel}")
            victoire = True
            if joueur_actuel == 1:
                score_j_1 += 1
                winner_is = 1
            else:
                score_j_2 += 1
                winner_is = 2
        
        if victoire is not True:
            match_nul = True
            for ligne in grille:
                if 0 in ligne:
                    match_nul = False
                

        if match_nul:
            print("Match nul")
            winner_is = 0
            
running = True
while running:

    #chargement et affichage de l'écran d'acceuil
    running_victoire = True
    running_game = True
    while running_game:
        if victoire or match_nul:
            running_game = False
            running_victoire = True
        
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                running_game = False
                running_victoire = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                print(f"position x:{x} y:{y}")
                colonne = (x - 50) // 100
                ligne = (y - 50) // 100
                print (f"colonne {colonne} ligne {ligne}")

                if button_replay().collidepoint(x, y):
                    print("button")
                    grille = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                    joueur_actuel = 1
                    victoire = False
                    match_nul = False
                    running_victoire = False
                    running_game = False
                    break

                if grille[ligne][colonne] == 0:
                    if joueur_actuel == 1:
                        grille[ligne][colonne] = symbole_j_1
                    else:
                        grille[ligne][colonne] = symbole_j_2
                    game_rules()
                    if victoire == False:

                        joueur_actuel = 3 - joueur_actuel

        screen.fill(blanc)

        screen.blit(header_surface, (0, 0))
        screen.blit(main_surface, (0, header_height))
        screen.blit(footer_surface, (0, 400 - footer_height))

        main_surface.fill(fond_game)
        button_replay()

        for colonne in range(3):
            for ligne in range(3):
                if grille[ligne][colonne] == symbole_j_1:
                    pg.draw.line(main_surface, cross_color, ((colonne * 100) + 50, (ligne * 100)), (((colonne + 1) * 100) + 50, ((ligne + 1) * 100)), 10)
                    pg.draw.line(main_surface, cross_color, (((colonne + 1) * 100) + 50, (ligne * 100)), ((colonne * 100) + 50, ((ligne + 1) * 100)), 10)
                elif grille[ligne][colonne] == symbole_j_2:
                    pg.draw.circle(main_surface, circle_color, (colonne * 100 + 100, ligne * 100 + 50), 40, 10)
        
        

        # Dessine la grille
        draw_grille()

        draw_header_footer()
        """pg.draw.rect(footer_surface, noir, (50, 50 , 100, 70),5)"""

        #affiche le tour du joueur en cours dans le header
        texte = fonte.render("Tour du joueur {}".format(joueur_actuel), True, noir)
        texte_rect = texte.get_rect(center=(header_surface.get_width() // 2, header_surface.get_height() // 2))
        header_surface.blit(texte, texte_rect.topleft)

        #affiche le score des joueurs  dans le header
        texte = fonte_score.render("X         {}".format(score_j_1), True, noir)
        texte_rect = texte.get_rect(center=(header_left_surface.get_width() // 2, header_left_surface.get_height() // 3))
        header_left_surface.blit(texte, texte_rect.topleft)

        texte = fonte_score.render("O         {}".format(score_j_2), True, noir)
        texte_rect = texte.get_rect(center=(header_right_surface.get_width() // 2, header_right_surface.get_height() // 3))
        header_right_surface.blit(texte, texte_rect.topleft)


        # Met à jour l'affichage
        pg.display.flip()

        clock.tick(60)
        #print(running_victoire)
        #print(running_game)
        
  
    while running_victoire: 
        #print(score_j_1)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                running_victoire = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if button_replay().collidepoint(x, y):
                    print("button")
                    grille = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                    joueur_actuel = 1
                    victoire = False
                    match_nul = False
                    running_victoire = False
                    break
                
        
        screen.fill(blanc)

        screen.blit(header_surface, (0, 0))
        screen.blit(main_surface, (0, header_height))
        screen.blit(footer_surface, (0, 400 - footer_height))
        
        main_surface.fill(fond_game)

        draw_header_footer()

        
        #affiche rejouer dans le footer
        button_replay()

        #affiche le score des joueurs  dans le header
        texte = fonte_score.render("X         {}".format(score_j_1), True, noir)
        texte_rect = texte.get_rect(center=(header_left_surface.get_width() // 2, header_left_surface.get_height() // 2))
        header_left_surface.blit(texte, texte_rect.topleft)

        texte = fonte_score.render("O         {}".format(score_j_2), True, noir)
        texte_rect = texte.get_rect(center=(header_right_surface.get_width() // 2, header_right_surface.get_height() // 2))
        header_right_surface.blit(texte, texte_rect.topleft)

        if winner_is == 1 :

            texte = fonte_victory_screen.render("X", True, cross_color)
            texte_rect = texte.get_rect(center=(main_surface.get_width() // 2, main_surface.get_height() // 2))
            main_surface.blit(texte, texte_rect.topleft)

            texte = fonte_victory_screen.render("Victoire", True, cross_color)
            texte_rect = texte.get_rect(center=(main_surface.get_width() // 2, main_surface.get_height() // 1.5))
            main_surface.blit(texte, texte_rect.topleft)
        
        elif winner_is == 2 :

            texte = fonte_victory_screen.render("O", True, circle_color)
            texte_rect = texte.get_rect(center=(main_surface.get_width() // 2, main_surface.get_height() // 2))
            main_surface.blit(texte, texte_rect.topleft)

            texte = fonte_victory_screen.render("Victoire", True, circle_color)
            texte_rect = texte.get_rect(center=(main_surface.get_width() // 2, main_surface.get_height() // 1.5))
            main_surface.blit(texte, texte_rect.topleft)

        else:

            texte = fonte_victory_screen.render("X      O", True, cross_color)
            texte_rect = texte.get_rect(center=(main_surface.get_width() // 2, main_surface.get_height() // 2))
            main_surface.blit(texte, texte_rect.topleft)

            texte = fonte_victory_screen.render("match nul", True, circle_color)
            texte_rect = texte.get_rect(center=(main_surface.get_width() // 2, main_surface.get_height() // 1.5))
            main_surface.blit(texte, texte_rect.topleft)

            
        pg.display.flip()
        clock.tick(60)