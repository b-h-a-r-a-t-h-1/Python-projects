List=[71,23,45,13,26,42,69,32]
print('LIST=',List)
for i in range(1,len(List)):
	key=List[i]
	j=i-1
	while j>=0 and key< List[j]:
		List[j+1]=List[j]
		j=j-1
	else:
	    List[j+1]=key
print('list after sorting:',List)