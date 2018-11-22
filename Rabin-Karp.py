def RKMatcher(Text,Pattern,d,q):
	n = len(Text)
	m = len(Pattern)
	h = pow(d,m-1)%q
	p = 0 # hash vaue of the pattern
	t = 0 # hash value of the text
	for i in range(0,m):
		p = (p*d + ord(Pattern[i])) %q
		t = (t*d + ord(Text[i])) %q
	# matching the pattern in the text
	for i in range(0,n-m+1):
		
		if p==t :
			for j in range(0,m):
				if Text[i+j] !=Pattern[j]:
					break
			print("Pattern found in location: " + str(i))
		if i < n-m:
			t = (d*(t-ord(Text[i])*h) + ord(Text[i+m]))%q 
  
			if t < 0: 
				t = t+q  # make sure that t >= 0
RKMatcher("GGGAAAGG","AA",256,101)