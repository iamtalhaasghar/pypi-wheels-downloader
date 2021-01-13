f = open('cmd_output.txt')
links = list()
lines = f.readlines()
for i in range(len(lines)):
    for w in lines[i].split():        
        if(w.startswith('https://')):
            nextHalf = lines[i+1].split()[0]
            h = '%s%s' % (w,nextHalf.strip())
            links.append(h.strip())
f.close()
f = open('links.txt','w')
for i in links:
    f.write('%s\n'%i)
f.close()
f = open('packages.txt','w')
for i in links:
    temp = i.split('/')[-1]
    f.write('%s\n'% temp)
f.close()
