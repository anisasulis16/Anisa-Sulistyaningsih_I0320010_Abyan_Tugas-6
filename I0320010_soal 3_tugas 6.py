#membuat program

for i in range(10, 25):
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
        print('%i adalah bilangan prima' %i)
    else:
        print('%i bukan prima' %i)
    i+=1