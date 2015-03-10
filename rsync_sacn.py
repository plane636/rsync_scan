import os
import time
import re
filename = raw_input('press file path:')
def rsync(ip):
  cmd = 'rsync '+ip+'::'
  print cmd
  f = os.popen(cmd)
  data = f.readline()
  return(data)
def rsync2(ip,moudle):
  cmd2 = 'rsync '+ip+'::'+moudle
  print cmd2
  f = os.popen(cmd2)
  data2 = f.readline()
  return(data2)
for line in open(filename,'r'):
    line=line.strip('\n')
    data1 = rsync(line)
    re1 = re.match(r'\S*', data1)
    data = re1.group()
    if data:
      data2 = rsync2(line,data)
      if data2:
        data+='\n'
        w = open('rsync_test.txt','a')
        w.write(ip,'/n',data,data2)
        print data2
      else:
        print line,data,'cant connect'
    else:
      print line,'cant connect'
else:
    print 'all done'