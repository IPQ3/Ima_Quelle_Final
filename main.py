import js as p5

from Characterselect import *
from Battle1 import *
from BattleStats import *
from Ending_1 import *
from Ending_2 import *

battlestats = BattleStats()
character = 0
griffith = 1
ulya = 2
otto = 3
character_select = Character_Select()
battle1 = Battle1()
ending_1 = Ending_1()
ending_2 = Ending_2()
ending_1 = Ending_1()

CharacterSelect = p5.loadImage('Character Select.png')
BattleBackground = p5.loadImage('Battle Background.png')

program_state = 'START'
print('program_state =', program_state)

def title():
  p5.background(0)
  p5.fill(0,0,180)
  p5.stroke(180,0,0)
  p5.textSize(17)
  p5.text('Press e to play',96,150)

    
chHP = 1
chDMG = 1
chSPD = 1

def setup():
  p5.createCanvas(300, 300)
  p5.background(0)
  p5.rectMode(p5.CENTER)


def draw():
  global character_select,program_state
  p5.background(0)
  cursor_xy = (int(p5.mouseX), int(p5.mouseY))
  #p5.text(cursor_xy, 10, 20)  # cursor (x, y) 
  #print(p5.mouseX, p5.mouseY)
  if(program_state == 'START'):
    title()
  else:
    pass

  if(program_state == 'START'):
    if(p5.keyIsPressed == True):
      if(p5.key == 'e'):
        program_state = 'CHARACTERSELECT'
        if(program_state == 'CHARACTERSELECT'):
          print('program_state =', program_state)
          character_select.draw()
    else:
      pass
  elif(program_state == 'CHARACTERSELECT'):
    character_select.draw()
    #battlestats.draw()
    if(p5.mouseIsPressed == True):
      battle1.draw()
      #battlestats.draw()
    else:
      pass

  elif(program_state == 'BATTLE1'):
    battle1.draw()
    battle1.update()
    #battlestats.draw()
    
  elif(program_state == 'ENDING_1'):
    ending_1.draw()
  elif(program_state == 'ENDING_2'):
    ending_2.draw()

def keyPressed(event):
  #print('keyPressed.. ' + str(p5.key))
  pass

def keyReleased(event):
  #print('keyReleased.. ' + str(p5.key))
  pass

def mousePressed(event):
  #print('mousePressed..')
  pass

def mouseReleased(event):
  #print('mouseReleased..')
  pass


  
