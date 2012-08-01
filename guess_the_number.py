#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  guess_the_number.py
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

import random as r
GC = 0 # Guess count
GCstr = ""
minNum = 1
maxNum = 20
num = r.randint(minNum,maxNum)
guess = 0
print "Guess my number, it's between 1 and 20"
while guess != num:
	try:
		guess = int(raw_input("Guess a number: "))
		print "Your guess is "+str(guess)
		
		if guess<minNum or guess>maxNum:
			print "The number is between 1 and 20"
		else:
			GC+=1
			GCstr = str(GC)
			if guess<num:
				print "The number is higher. Try number "+GCstr
			elif guess>num:
				print "The number is lower. Try number "+GCstr
			else:
				print "Ding ding ding! You guessed it! Nice work! You guesset it with "+GCstr+" tryes!"
	except:
		print "Come on, give me a number!"
