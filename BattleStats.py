from main import *
from Ending_1 import *
from Battle1 import *
from Characterselect import *

#character_select = Character_Select()

class BattleStats():
  #print('BattleStats') < This is to make sure its on
  def __init__(self):
    chHP = 1
    chDMG = 1
    chSPD = 1
    ATKR = 0
    ATK = 0
    griffith = 1
    ulya = 2
    otto = 3
    #character = 0
    
  def draw(self, griffith = 1, ulya = 2, otto = 3, character = 0, chHP = 1,chDMG = 1, chSPD = 1, ATKR = 0, ATK = 0):
    #global character
    p5.background(0)
    if(character == griffith):
      chHP = 200
      chDMG = 50
      chSPD = 10

    elif(character == ulya):
      chHP = 150
      chDMG = 30
      chSPD = 50

    elif(character == otto):
      chHP = 150
      chDMG = 30
      chSPD = 30
      
  def update(self):
    if(chHP<0):
      program_state = 'LOSE'
      if(program_state == 'LOSE'):
        Ending_1.draw()
    else:
      pass
