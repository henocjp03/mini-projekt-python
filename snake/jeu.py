import turtle
import time
import random

# Configuration de l'écran
WIDTH = 600
HEIGHT = 600
DELAY = 0.07

class SnakeGame:
    def __init__(self):
        # Initialisation de l'écran
        self.screen = turtle.Screen()
        self.screen.title("Jeu du Serpent")
        self.screen.bgcolor("black")
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.tracer(0)  # Désactive l'animation automatique
        
        # Création de la tête du serpent
        self.head = turtle.Turtle()
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "stop"
        self.head.speed = 20  # Vitesse de déplacement
        
        # Liste pour stocker les segments du corps
        self.segments = []
        
        # Création de la nourriture
        self.food = turtle.Turtle()
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.food.goto(0, 100)
        
        # Score
        self.score = 0
        self.high_score = 0
        
        # Affichage du score
        self.score_display = turtle.Turtle()
        self.score_display.speed(0)
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, HEIGHT/2 - 40)
        self.update_score_display()
        
        # Instructions
        self.instructions = turtle.Turtle()
        self.instructions.speed(0)
        self.instructions.color("gray")
        self.instructions.penup()
        self.instructions.hideturtle()
        self.instructions.goto(0, HEIGHT/2 - 70)
        self.instructions.write("Utilisez les flèches pour déplacer le serpent", 
                               align="center", font=("Arial", 12, "normal"))
        
        # Contrôles clavier
        self.screen.listen()
        self.screen.onkey(self.go_up, "Up")
        self.screen.onkey(self.go_down, "Down")
        self.screen.onkey(self.go_left, "Left")
        self.screen.onkey(self.go_right, "Right")
        self.screen.onkey(self.reset_game, "space")  # Touche espace pour redémarrer
        
        # Variables de jeu
        self.game_over_flag = False
        self.last_update_time = time.time()
        
        # Objets pour les messages (pré-créés pour éviter la latence)
        self.game_over_display = None
        self.restart_display = None
        
    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"
    
    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"
    
    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"
    
    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"
    
    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + self.head.speed)
        
        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - self.head.speed)
        
        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - self.head.speed)
        
        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + self.head.speed)
    
    def update_score_display(self):
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score}  Meilleur score: {self.high_score}", 
                                align="center", font=("Arial", 20, "normal"))
    
    def spawn_food(self):
        # Position aléatoire pour la nourriture - version optimisée sans récursion
        max_attempts = 50
        for _ in range(max_attempts):
            x = random.randint(-WIDTH//2 + 40, WIDTH//2 - 40)
            y = random.randint(-HEIGHT//2 + 40, HEIGHT//2 - 40)
            x = round(x / 20) * 20  # Aligner sur la grille
            y = round(y / 20) * 20
            
            # Vérifier que la nourriture n'apparaît pas sur la tête
            if (x, y) == (self.head.xcor(), self.head.ycor()):
                continue
                
            # Vérifier que la nourriture n'apparaît pas sur un segment
            collision = False
            for segment in self.segments:
                if segment.distance(x, y) < 20:
                    collision = True
                    break
            
            if not collision:
                self.food.goto(x, y)
                return
        
        # Si aucune position valide n'est trouvée, placer la nourriture dans un coin
        self.food.goto(WIDTH//2 - 60, HEIGHT//2 - 60)
    
    def check_collision_with_food(self):
        if self.head.distance(self.food) < 20:
            self.spawn_food()
            
            # Ajouter un nouveau segment
            new_segment = turtle.Turtle()
            new_segment.shape("square")
            new_segment.color("gray")
            new_segment.penup()
            self.segments.append(new_segment)
            
            # Augmenter le score
            self.score += 10
            if self.score > self.high_score:
                self.high_score = self.score
            
            self.update_score_display()
    
    def check_collision_with_walls(self):
        if (self.head.xcor() > WIDTH//2 - 20 or self.head.xcor() < -WIDTH//2 + 20 or
            self.head.ycor() > HEIGHT//2 - 20 or self.head.ycor() < -HEIGHT//2 + 20):
            return True
        return False
    
    def check_collision_with_body(self):
        for segment in self.segments:
            if segment.distance(self.head) < 10:
                return True
        return False
    
    def reset_game(self):
        # Nettoyer les messages précédents
        if self.game_over_display:
            self.game_over_display.clear()
            self.game_over_display.hideturtle()
        if self.restart_display:
            self.restart_display.clear()
            self.restart_display.hideturtle()
            
        self.head.goto(0, 0)
        self.head.direction = "stop"
        
        # Cacher les segments
        for segment in self.segments:
            segment.hideturtle()
        
        # Vider la liste des segments
        self.segments.clear()
        
        # Réinitialiser le score
        self.score = 0
        self.update_score_display()
        
        self.game_over_flag = False
        self.spawn_food()
    
    def game_over(self):
        self.game_over_flag = True
        
        # Créer ou réutiliser l'affichage Game Over
        if not self.game_over_display:
            self.game_over_display = turtle.Turtle()
            self.game_over_display.speed(0)
            self.game_over_display.color("red")
            self.game_over_display.penup()
            self.game_over_display.hideturtle()
        
        self.game_over_display.clear()
        self.game_over_display.goto(0, 0)
        self.game_over_display.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
        self.game_over_display.showturtle()
        
        # Créer ou réutiliser l'affichage de redémarrage
        if not self.restart_display:
            self.restart_display = turtle.Turtle()
            self.restart_display.speed(0)
            self.restart_display.color("yellow")
            self.restart_display.penup()
            self.restart_display.hideturtle()
        
        self.restart_display.clear()
        self.restart_display.goto(0, -40)
        self.restart_display.write("Appuyez sur ESPACE pour rejouer", 
                               align="center", font=("Arial", 15, "normal"))
        self.restart_display.showturtle()
    
    def run(self):
        # Boucle principale du jeu optimisée
        while True:
            current_time = time.time()
            
            # Mise à jour à intervalle régulier (basé sur DELAY)
            if current_time - self.last_update_time >= DELAY:
                self.screen.update()
                
                if not self.game_over_flag:
                    # Vérifier les collisions avec les murs
                    if self.check_collision_with_walls():
                        self.game_over()
                        self.last_update_time = current_time
                        continue
                    
                    # Vérifier les collisions avec le corps
                    if self.check_collision_with_body():
                        self.game_over()
                        self.last_update_time = current_time
                        continue
                    
                    # Déplacer les segments dans l'ordre inverse
                    for index in range(len(self.segments)-1, 0, -1):
                        x = self.segments[index-1].xcor()
                        y = self.segments[index-1].ycor()
                        self.segments[index].goto(x, y)
                    
                    # Déplacer le premier segment vers la tête
                    if len(self.segments) > 0:
                        x = self.head.xcor()
                        y = self.head.ycor()
                        self.segments[0].goto(x, y)
                    
                    self.move()
                    self.check_collision_with_food()
                
                self.last_update_time = current_time

# Lancement du jeu
if __name__ == "__main__":
    game = SnakeGame()
    game.run()