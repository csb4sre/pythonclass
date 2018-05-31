a = open('textsample.txt','w')
a.write('''There is no Internet connection
Try:

Checking the network cables, modem, and router
Reconnecting to Wi-Fi
Running Windows Network Diagnostics
DNS_PROBE_FINISHED_NO_INTERNET''')
a.close()

a = open('textsample.txt','r')
print (a.readline())

line = a.readline()
for i in line:
    print(line)
