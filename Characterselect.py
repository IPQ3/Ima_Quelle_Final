import js as p5
from main import *
from Battle1 import *
from BattleStats import *

battlestats = BattleStats()
battle1 = Battle1()
#character_select = Character_Select()

CharacterSelect = p5.loadImage('Character Select.png')

class Character_Select:
  #print('select character') < This is to make sure its on
  
  def __init__(self):
    character = 0
    griffith = 1
    ulya = 2
    otto = 3
    program_state = 'CHARACTERSELECT'

    
  def draw(self, griffith = 1, ulya = 2, otto = 3):
    global character
    program_state = 'CHARACTERSELECT'
    p5.background(40)
    p5.image(CharacterSelect,0,0)
    p5.stroke(0,0,135)
    p5.fill(0)
    p5.rect(150,265,380,60)
    p5.stroke(0,255,0)
    p5.fill(0,135,0)
    p5.text('Griffith',25,270)
    p5.stroke(255,0,0)
    p5.fill(135,0,0)
    p5.text('Ulya',135,270)
    p5.stroke(0,0,255)
    p5.fill(0,0,135)
    p5.text('Otto',235,270)
    
    if(program_state == 'CHARACTERSELECT'):
      if(p5.mouseIsPressed == True):
        if(p5.mouseX > 0 and p5.mouseX < 100):
          character = griffith
          program_state = 'BATTLE1'
          battle1.draw()
          print('Character = Griffith')
          chHP = 200
          chDMG = 50
          chSPD = 10
          print('Character HP =', chHP)
          print('Character DMG =', chDMG)
          print('Character HP =', chSPD)
      
        elif(p5.mouseX > 100 and p5.mouseX < 200):
          character = ulya
          program_state = 'BATTLE1'
          battle1.draw()
          print('Character = Ulya')
          chHP = 150
          chDMG = 30
          chSPD = 50
          print('Character HP =', chHP)
          print('Character DMG =', chDMG)
          print('Character SPD =', chSPD)
      
        elif(p5.mouseX > 200 and p5.mouseX < 300):
          character = otto
          program_state = 'BATTLE1'
          battle1.draw()
          print('Character = Otto')
          chHP = 150
          chDMG = 30
          chSPD = 30
          print('Character HP =', chHP)
          print('Character DMG =', chDMG)
          print('Character HP =', chSPD)
      else:
        pass
    else:
      pass
      
