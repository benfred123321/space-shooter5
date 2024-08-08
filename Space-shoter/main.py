import pgzrun
import random

HEIGHT = 800
WIDTH = 1200
white = (255,255,255)
blue =  (10,10,255)

ship = Actor("galaga")
ship.pos = (WIDTH//2,HEIGHT-60)
 
 
speed=5
bullets = []
enemies = []
score = 0
direction = 1
ship.dead = False
ship.countdown = 90

for x in range(8):
    for y in range(4):
        enemies.append(Actor("bug"))
        enemies[-1].x = 100 + 50 * x
        enemies[-1].y = 80 + 50 * y 
  
def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullet = Actor("bullet")
            bullets.append(bullet)
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y - 50 
  
def update():
    global score,direction
    move_down = False
    #move the ship left or right with arrow keys
    if ship.dead == False:
        if keyboard.left:
            ship.x = ship.x - speed
            if ship.x < 0:
                ship.x = 0
        elif keyboard.right:
            ship.x = ship.x + speed
            if ship.x > WIDTH:
                ship.x = WIDTH
        

    
    for bullet in bullets:
        if bullet.y < 0:
            bullets.remove(bullet)
        else:
            bullet.y = bullet.y - 10 
    if len(enemies) == 0:
        game_over()
    if len(enemies) > 0 and (enemies[-1].x > WIDTH - 80 or enemies[0].x < 80):
        move_down = True
        direction = direction *- 1
    for enemy in enemies:
        enemy.x += 5 * direction
        if  move_down == True:
            enemy.y += 100
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score += 1     
                bullets.remove(bullet)
                enemies.remove(enemy)
                if len(enemies) == 0:
                    game_over()
        if enemy.colliderect(ship):
            ship.dead = True
    if ship.dead:
        game_over()


def game_over():
    screen.draw.text("Game Over!!!",(400,600))



def display_score():
    screen.draw.text(str(score),(50,25))


def draw():
    screen.clear()
    screen.fill(blue)
    if ship.dead == False:
        ship.draw()
    for alien in enemies:
        alien.draw()
    for bullet in bullets:
        bullet.draw()
    if len(enemies) == 0:
        game_over()
    display_score()




pgzrun.go()