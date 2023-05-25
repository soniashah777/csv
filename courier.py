import csv
def courier_add():
     while True:
          try:
               fh = open ("courier.csv","r")
                               
          except:
               fh = open ("courier.csv","w",newline='')
               headerlist=["cid","s_name","source","destination"]
               wtr= csv.writer(fh)
               wtr.writerow(headerlist)
               fh.close()
          finally:
               fh = open ("courier.csv","a",newline='')
               wtr= csv.writer(fh)
               cid=input ("Enter customer id")
               s_name=input ("Enter sender name")
               source=input ("Enter source address")
               destination=input ("Enter destination address")
               wtr.writerow([cid,s_name,source,destination])
               fh.close()
               break
def courier_search():
     destin=input("Enter destination to search") 
     fh = open ("courier.csv","r")
     rdr=csv.reader(fh)   
     for r in rdr:
          #print (len(r))
          if (len(r)>0 and r[3]==destin  ):
               print (r)
while True:
     print ("Enter a to add record")
     print ("Enter s to search record")
     ch=input()
     if ch.lower()=='a':
          courier_add()
     elif ch.lower()=='s':
          try:
               courier_search()
          except Exception as e:
               print (e)
     else:
          print ("Wrong choice")
          
          

