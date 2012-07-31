END = '\033[0m' # End formating.

a = 0;
while a<100:
	t = '\033['+str(a)+'m';
	print t+"ABCDEFGHIJKLMNOPQRSTUVWXYZ ---------- "+str(a)+END
	a+=1
