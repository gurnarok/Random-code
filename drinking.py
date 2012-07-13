#!/usr/bin/python
import random as ran
a = 0;
players = [];
drinks = [];
print "Add names.\nEnter a blank value to proceed.\n";
while a!="":
	a = raw_input("Enter a name: ")
	if a!="":
		players.append(a);
	else:
		print "There are ",players.__len__()," names\n\n";

a = 0;
print "Add drinks.\nEnter a blank value to proceed.\n";
while a!="":
	a = raw_input("Enter a drink: ")
	if a!="":
		drinks.append(a);
	else:
		print "There are ",drinks.__len__()," drinks\n\n";

a = 0;
print "Start the games!\nEnter q to quit the game.\n";
while a!="q":
	print ran.choice(players)," drinks ", ran.choice(drinks)
		
	a = raw_input("Continue games? ");
