#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dragon_cave.py
#  
#  Copyright 2012 Ilari Saastamoinen <ilari@gurnarok.me>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import random, time
#global STR, DEX, LVL, HIT
STR = 10
HIT = 50
DEX = 5
LVL = 1

def character():
	print ""
	print "You are Sir Spank-a-lot, level "+str(LVL)+" spanking knight."
	print "You wield your mighty whip, causing "+str(STR)+" points of damage"
	print "and you have a "+str((DEX*10)/2)+"% chance to dodge."
	print "Health: "+str(HIT)	

def lvlUp():
	global STR, LVL, HIT, DEX
	STR+=1
	LVL+=1
	HIT+=5
	if LVL%2==0:
		DEX+=1

def dungeon():
	print "You slowly move towards a dungeon, bones of animals and humans, smelling the sulphur in the air."
	time.sleep(2)
	global dragonLVL, dragonHIT, dragonTYPE, dragonSTR
	
	dragonLVL = random.randint(1,15)
	
	if dragonLVL<5:
		dragonTYPE = "baby "
	elif dragonLVL<10:
		dragonTYPE = ""
	elif dragonLVL<15:
		dragonTYPE = "big "
	else:
		dragonTYPE = "ancient "
	
	r = random.randint(1,11)
	if r>7:
		dragonHIT = 50+random.randint(5,10)+(5*dragonLVL)
		dragonSTR = 7+random.randint(1,3)+dragonLVL
		dragonTYPE = "strong "+dragonTYPE
	elif r<5:
		dragonHIT = 50-random.randint(5,10)+(5*dragonLVL)
		dragonSTR = 7-random.randint(1,3)+dragonLVL
		dragonTYPE = "weak "+dragonTYPE
	else:
		dragonHIT = 50+(5*dragonLVL)
		dragonSTR = 7+dragonLVL
	
	print "You find a "+dragonTYPE+"dragon!"
	print "\tLEVEL: "+str(dragonLVL)
	print "\tHEALTH: "+str(dragonHIT)
	print "\tSTR: "+str(dragonSTR)
	
	com = raw_input("What do you do? FIGHT or FLIGHT: ").lower()
	if com=="fight":
		print "You feel a rush of adrenaline, gripping your whip harder and charging towards the dragon."
		combat()
	elif com=="flight":
		print "Your feet start to tremble, palms getting sweaty and you slowly start to creep away from the dragon."
		#run_away()
	else:
		print "You stand there in shock and the dragon eats you."
		global HIT
		HIT = 0
		
def combat():
	global STR, DEX, LVL, HIT, dragonLVL, dragonHIT, dragonTYPE, dragonSTR
	turn=1
	while HIT>0 or dragonHIT>0:
		
		print "Turn "+str(turn)
		
		print "You attack the dragon!"
		hit=random.randint(0,2)
		if hit==0:
			print "Oh no! You miss!"
		elif hit==1:
			print "You hit the dragon with "+str(STR)+" damage!"
			dragonHIT-=STR;
		else:
			print "CRITICAL HIT! You deal double damage!"
			print "You hit the dragon with "+str(STR*2)+" damage!"
			dragonHIT-=STR*2
			
		
		
		print "Dragon attacks you!"
		hit=random.randint(0,5)
		if hit<3:
			print "The dragon misses!"
		elif hit==5:
			print "Oh no! The dragon hit's you critically, causing double damage!"
			print "The dragon hit's you with "+str(dragonSTR*2)+" damage!"
			HIT-=dragonSTR*2
		else:
			print "Oh no! The dragon hit's you!"
			print "The dragon hit's you with "+str(dragonSTR)+" damage!"
			HIT-=dragonSTR
		
		print "Your hitpoints: "+str(HIT)
		print "Dragons hitpoints: "+str(dragonHIT)
		print "----------\n"
		
		if HIT<1:
			print "Oh no! You died!"
			break
		
		if dragonHIT<1:
			print "You defeated the dragon! You gain a level!"
			lvlUp()
			character()
			break
			
		
		time.sleep(2)
		turn+=1

i = 1
while i==1:
	com = raw_input("What to do? ")
	if com=="c" or com == "char":
		character()
	elif com == "d" or com=="dungeon":
		dungeon()
		print ""
	elif com == "q" or com=="quit":
		break
	
	if HIT<1:
		print "You are dead! X_x"
		break
