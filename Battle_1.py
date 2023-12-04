import js as p5
from main import *
from Ending_1 import *
from Ending_2 import *
from Characterselect import *
from BattleStats import *

battlestats = BattleStats()
#character_select = Character_Select()
ending_1 = Ending_1()
BattleBackground = p5.loadImage('Battle Background.png')

class Battle1(BattleStats):
  
  def __init__(self):
    Turns1 = 1
    ATKR = p5.random(1,3)
    ATK = 0
    bmHP = 300
    bmDMG = 50
    bmSPD = 50
    bmDodge = 40
    Hands = 2
    CallOfTheWild = 3

    chHP = 1
    chDMG = 1
    chSPD = 1
    BATKR = p5.random(1,5) #For random Numbers
    BATK = 0  #To assign attack
    ATKR = 0
    ATK = 0
    griffith = 1
    ulya = 2
    otto = 3
    program_state = 'BATTLE1'
    character = ulya
    
  def draw(self,Turns1 = 1, griffith = 1, ulya = 2, otto = 3, chHP = 1, chDMG = 1, chSPD = 1, ATK = 1, ATKR = 0, BMATK = 1, BMATKR = p5.random(1,3), bite = 20, tackle = 10, dodge = 20, bmHP = 100, bmDMG = 10, bmSPD = 30, bmDodge = 30):
    
    global program_state
    character = ulya
    program_state = 'BATTLE1'
    p5.image(BattleBackground,0,0)
    p5.background(0)
    p5.stroke(0,0,135)
    p5.fill(0)
    p5.rect(100,265,380,60)
    p5.fill(0,0,180)
    p5.stroke(180,0,0)
    p5.textSize(15)
    p5.text('The Beast Mother stands before you.',15,270)
    print('program_state =',program_state)
    print('character =', character)
    if(p5.keyIsPressed == True):
      print('key is pressed')
    battlestats.draw()
    p5.noLoop()
    if(p5.mouseIsPressed == True):
      Battle1.update(self)
    else:
      pass
    if(bmHP == 0):
      program_state = 'WIN'
      ending_2.draw()
    else:
      pass
      
  def update(self,Turns1 = 1, character = 2, griffith = 1, ulya = 2, otto = 3, chHP = 1, chDMG = 1, chSPD = 1, ATK = 1, ATKR = 0, BMATK = 1, BMATKR = p5.random(1,3), bite = 20, tackle = 10, dodge = 20, bmHP = 100, bmDMG = 10, bmSPD = 30, bmDodge = 30):
    global program_state
    #battlestats.draw()
    p5.image(BattleBackground,0,0)
    p5.stroke(0,0,135)
    p5.fill(0)
    p5.rect(100,265,380,60)
    p5.fill(0,0,180)
    p5.stroke(180,0,0)
    p5.textSize(15)
    p5.text('The Beast Mother stands before you.',15,250)
    p5.text('What do you do.',15,270)
    p5.text('l = low attack',189,20)
    p5.text('h = high attack', 189,40)
    p5.text('d = dodge', 189,60)
    if(program_state == 'BATTLE1'):
      if(Turns1 == 1):
        print('turn 1')
        if(character == 2):
          #print('Character HP =', chHP)
          #print('Character DMG =', chDMG)
          #print('Character SPD =', chSPD)
          if(p5.keyIsPressed == True):
            print('key is pressed')
            if(p5.key == 'l'):
              print('low attack')
              bmHP -= 30
              if(p5.mouseIsPressed == True):
                Turns1 = 2
              
            elif(p5.key == 'h'):
              print('high attack')
              ATKR = p5.random(1,2)
              if(ATKR >1.5):
                print('high roll')
                ATK = 30
                if(ATK == 30):
                  bmHP -= 30
                  if(p5.mouseIsPressed == True):
                    Turns1 = 2
              elif(ATKR < 1.6):
                print('low roll')
                ATK = 20
                if(ATK == 20):
                  bmHP -= 20
                  if(p5.mouseIsPressed == True):
                    Turns1 = 2
                    
            elif(p5.key == 'd'):
              print('dodge')
              bmHP = bmHP
              if(p5.mouseIsPressed == True):
                Turns1 = 2
              
          #else:
            #pass
            
        elif(character == griffith):
          BMATKR = p5.random(1,4)
          if(BMATKR == 1):
            BMATK = bite
            if(BMATK == bite):
              chHP -= 30
              p5.fill(0,0,180)
              p5.stroke(180,0,0)
              p5.textSize(17)
              p5.text('The Beast Mother bites you.',15,260)
              p5.text('you lose 20 HP.',15,280)
              print('Character HP =', chHP)
              print('Character DMG =', chDMG)
              print('Character SPD =', chSPD)
              if(p5.mouseIsPressed == True):
                Turns1 = 2
              else:
                pass
            #else:
                #pass


          elif(BMATKR == 2):
            BMATK = Hands
            if(BMATK == Hands):
              chHP -=25
              p5.fill(0,0,180)
              p5.stroke(180,0,0)
              p5.textSize(15)
              p5.text('The Beast Mothers hands squeeze your body',15,260)
              p5.text('you lose 20 HP',15,280)
              print('Character HP =', chHP)
              print('Character DMG =', chDMG)
              print('Character SPD =', chSPD)
              if(p5.mouseIsPressed == True):
                Turns1 = 2
              else:
                pass
            #else:
              #pass

          elif(BMATKR == 3):
            BMATK = CallOfTheWild
            if(BMATK == CallofTheWild):
              chDMG -= 10
              p5.fill(0,0,180)
              p5.stroke(180,0,0)
              p5.textSize(15)
              p5.text('The Beast Mother Howls.',10,170)
              p5.text('your damage decreases by 10.',10,190)
              print('Character HP =', chHP)
              print('Character DMG =', chDMG)
              print('Character SPD =', chSPD)
              if(p5.mouseIsPressed == True):
                Turns1 = 2
              else:
                pass
            #else:
              #pass

          elif(BMATKR == 4):
            BMATK = dodge
            if(BMATK == dodge):
              p5.fill(0,0,180)
              p5.stroke(180,0,0)
              p5.textSize(17)
              p5.text('The Beast Mother dodges your attack',15,260)
              print('Character HP =', chHP)
              print('Character DMG =', chDMG)
              print('Character SPD =', chSPD)
              if(p5.mouseIsPressed == True):
                Turns1 = 2
              else:
                pass
            #else:
              #pass

        
        elif(character == otto):
          BMATKR = p5.random(1,5)
          if(BMATKR == 1):
            BMATK = bite
            if(BMATK == bite):
              chHP -= 30
              p5.fill(0,0,180)
              p5.stroke(180,0,0)
              p5.textSize(17)
              p5.text('The Beast Mother bites you.',15,260)
              p5.text('you lose 20 HP.',15,280)
              print('Character HP =', chHP)
              print('Character DMG =', chDMG)
              print('Character SPD =', chSPD)
              if(p5.mouseIsPressed == True):
                Turns1 = 2
              else:
                pass
            #else:
              #pass


          elif(BMATKR > 2):
            if(BMATKR < 3):
              BMATK = Hands
              if(BMATK == Hands):
                chHP -=25
                p5.fill(0,0,180)
                p5.stroke(180,0,0)
                p5.textSize(15)
                p5.text('The Beast Mothers hands squeeze your body',15,260)
                p5.text('you lose 20 HP',15,280)
                print('Character HP =', chHP)
                print('Character DMG =', chDMG)
                print('Character SPD =', chSPD)
                if(p5.mouseIsPressed == True):
                  Turns1 = 2
                else:
                  pass
              #else:
                #pass

          elif(BMATKR > 3):
            if(BMATKR < 4):
              BMATK = CallOfTheWild
              if(BMATK == CallofTheWild):
                chDMG -= 10
                p5.fill(0,0,180)
                p5.stroke(180,0,0)
                p5.textSize(15)
                p5.text('The Beast Mother Howls.',10,170)
                p5.text('your damage decreases by 10.',10,190)
                print('Character HP =', chHP)
                print('Character DMG =', chDMG)
                print('Character SPD =', chSPD)
                if(p5.mouseIsPressed == True):
                  Turns1 = 2
                else:
                  pass
              #else:
                #pass

          elif(BMATKR > 4):
            BMATK = dodge
            if(BMATK == dodge):
              p5.fill(0,0,180)
              p5.stroke(180,0,0)
              p5.textSize(17)
              p5.text('The Beast Mother dodges your attack',15,260)
              print('Character HP =', chHP)
              print('Character DMG =', chDMG)
              print('Character SPD =', chSPD)
              if(p5.mouseIsPressed == True):
                Turns1 = 2
              else:
                pass
            #else:
              #pass
        

      elif(Turns1 == 2):
        print('Turn 2')
        print('Character HP =', chHP)
        #print('Character DMG =', chDMG)
        #print('Character SPD =', chSPD)
        print('Beast Mothers HP =', bmHP)
        if(character == ulya):
          BMATKR = p5.random(1,5)
          if(BMATKR == 1):
            BMATK = bite
            if(BMATK == bite):
              chHP -= 30
              p5.fill(0,0,180)
              p5.stroke(180,0,0)
              p5.textSize(17)
              p5.text('The Beast Mother bites you.',15,260)
              p5.text('you lose 20 HP.',15,280)
              print('Character HP =', chHP)
              print('Character DMG =', chDMG)
              print('Character SPD =', chSPD)
              if(p5.mouseIsPressed == True):
                Turns1 = 2
              else:
                pass
            #else:
              #pass


          elif(BMATKR > 2):
            if(BMATKR < 3):
              BMATK = Hands
              if(BMATK == Hands):
                chHP -=25
                p5.fill(0,0,180)
                p5.stroke(180,0,0)
                p5.textSize(15)
                p5.text('The Beast Mothers hands squeeze your body',15,260)
                p5.text('you lose 20 HP',15,280)
                print('Character HP =', chHP)
                print('Character DMG =', chDMG)
                print('Character SPD =', chSPD)
                if(p5.mouseIsPressed == True):
                  Turns1 = 2
                else:
                  pass
              #else:
                #pass

          elif(BMATKR > 3):
            if(BMATKR < 4):
              BMATK = CallOfTheWild
              if(BMATK == CallofTheWild):
                chDMG -= 10
                p5.fill(0,0,180)
                p5.stroke(180,0,0)
                p5.textSize(15)
                p5.text('The Beast Mother Howls.',10,170)
                p5.text('your damage decreases by 10.',10,190)
                print('Character HP =', chHP)
                print('Character DMG =', chDMG)
                print('Character SPD =', chSPD)
                if(p5.mouseIsPressed == True):
                  Turns1 = 2
                else:
                  pass
              #else:
                #pass

          elif(BMATKR > 4):
            BMATK = dodge
            if(BMATK == dodge):
              p5.fill(0,0,180)
              p5.stroke(180,0,0)
              p5.textSize(17)
              p5.text('The Beast Mother dodges your attack',15,260)
              print('Character HP =', chHP)
              print('Character DMG =', chDMG)
              print('Character SPD =', chSPD)
              if(p5.mouseIsPressed == True):
                Turns1 = 2
              else:
                pass
            #else:
              #pass
        elif(character == otto):
          print('Character HP =', chHP)
          print('Character DMG =', chDMG)
          print('Character SPD =', chSPD)
          if(p5.keyIsPressed == True):
            print('key is pressed')
            if(p5.key == 'l'):
              print('low attack')
              bmHP -= 30
              if(p5.mouseIsPressed == True):
                Turns1 = 2

            elif(p5.key == 'h'):
              print('high attack')
              ATKR = p5.random(1,2)
              if(ATKR >1.5):
                print('high roll')
                ATK = 30
                if(ATK == 30):
                  bmHP -= 30
                  if(p5.mouseIsPressed == True):
                    Turns1 = 2
              elif(ATKR < 1.6):
                print('low roll')
                ATK = 20
                if(ATK == 20):
                  bmHP -= 20
                  if(p5.mouseIsPressed == True):
                    Turns1 = 2

            elif(p5.key == 'd'):
              print('dodge')
              bmHP = bmHP
              if(p5.mouseIsPressed == True):
                Turns1 = 2

            #else:
              #pass
        elif(character == griffith):
          print('Character HP =', chHP)
          print('Character DMG =', chDMG)
          print('Character SPD =', chSPD)
          if(p5.keyIsPressed == True):
            print('key is pressed')
            if(p5.key == 'l'):
              print('low attack')
              bmHP -= 40
              if(p5.mouseIsPressed == True):
                Turns1 = 2

            elif(p5.key == 'h'):
              print('high attack')
              ATKR = p5.random(1,2)
              if(ATKR >1.5):
                print('high roll')
                ATK = 50
                if(ATK == 50):
                  bmHP -= 50
                  if(p5.mouseIsPressed == True):
                    Turns1 = 2
              elif(ATKR < 1.6):
                print('low roll')
                ATK = 20
                if(ATK == 20):
                  bmHP -= 20
                  if(p5.mouseIsPressed == True):
                    Turns1 = 2

            elif(p5.key == 'd'):
              print('dodge')
              bmHP = bmHP
              if(p5.mouseIsPressed == True):
                Turns1 = 2

        #else:
          #pass
          
          
 
      elif(Turns1 == 3):
        print('Turn 3')
        print('Character HP =', chHP)
        #print('Character DMG =', chDMG)
        #print('Character SPD =', chSPD)
        print('Beast Mothers HP =', bmHP)
        
      elif(Turns1 == 4):
        print('Turn 4')
        print('Character HP =', chHP)
        #print('Character DMG =', chDMG)
        #print('Character SPD =', chSPD)
        print('Beast Mothers HP =', bmHP)
        if(character == ulya):
          BMATKR = p5.random(1,5)
          if(BMATKR == 1):
            BMATK = bite
            if(BMATK == bite):
              chHP -= 30
              p5.fill(0,0,180)
              p5.stroke(180,0,0)
              p5.textSize(17)
              p5.text('The Beast Mother bites you.',15,260)
              p5.text('you lose 20 HP.',15,280)
              print('Character HP =', chHP)
              print('Character DMG =', chDMG)
              print('Character SPD =', chSPD)
              if(p5.mouseIsPressed == True):
                Turns1 = 2
              else:
                pass
            else:
              pass


          elif(BMATKR > 2):
            if(BMATKR < 3):
              BMATK = Hands
              if(BMATK == Hands):
                chHP -=25
                p5.fill(0,0,180)
                p5.stroke(180,0,0)
                p5.textSize(15)
                p5.text('The Beast Mothers hands squeeze your body',15,260)
                p5.text('you lose 20 HP',15,280)
                print('Character HP =', chHP)
                print('Character DMG =', chDMG)
                print('Character SPD =', chSPD)
                if(p5.mouseIsPressed == True):
                  Turns1 = 2
                else:
                  pass
              else:
                pass

          elif(BMATKR > 3):
            if(BMATKR < 4):
              BMATK = CallOfTheWild
              if(BMATK == CallofTheWild):
                chDMG -= 10
                p5.fill(0,0,180)
                p5.stroke(180,0,0)
                p5.textSize(15)
                p5.text('The Beast Mother Howls.',10,170)
                p5.text('your damage decreases by 10.',10,190)
                print('Character HP =', chHP)
                print('Character DMG =', chDMG)
                print('Character SPD =', chSPD)
                if(p5.mouseIsPressed == True):
                  Turns1 = 2
                else:
                  pass
              else:
                pass

          elif(BMATKR > 4):
            BMATK = dodge
            if(BMATK == dodge):
              p5.fill(0,0,180)
              p5.stroke(180,0,0)
              p5.textSize(17)
              p5.text('The Beast Mother dodges your attack',15,260)
              print('Character HP =', chHP)
              print('Character DMG =', chDMG)
              print('Character SPD =', chSPD)
              if(p5.mouseIsPressed == True):
                Turns1 = 2
              else:
                pass
            else:
              pass
    
      elif(Turns1 == 5):
        print('Turn 5')
        print('Character HP =', chHP)
        #print('Character DMG =', chDMG)
        #print('Character SPD =', chSPD)
        print('Beast Mothers HP =', bmHP)
    
      elif(Turns1 == 6):
        print('Turn 6')
        print('Character HP =', chHP)
        #print('Character DMG =', chDMG)
        #print('Character SPD =', chSPD)
        print('Beast Mothers HP =', bmHP)
    
      elif(Turns1 == 7):
        print('Turn 7')
        print('Character HP =', chHP)
        #print('Character DMG =', chDMG)
        #print('Character SPD =', chSPD)
        print('Beast Mothers HP =', bmHP)
    
      elif(Turns1 == 8):
        print('Turn 8')
        print('Character HP =', chHP)
        #print('Character DMG =', chDMG)
        #print('Character SPD =', chSPD)
        print('Beast Mothers HP =', bmHP)
    
      elif(Turns1 == 9):
        print('Turn 9')
        print('Character HP =', chHP)
        #print('Character DMG =', chDMG)
        #print('Character SPD =', chSPD)
        print('Beast Mothers HP =', bmHP)
    
      elif(Turns1 == 10):
        print('Turn 10')
        print('Character HP =', chHP)
        #print('Character DMG =', chDMG)
        #print('Character SPD =', chSPD)
        print('Beast Mothers HP =', bmHP)
        if(bmHP > 1):
          ending_1.draw()
        elif(bmHP < 1):
          ending_2.draw()
          
