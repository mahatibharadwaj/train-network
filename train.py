from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client 
import htmlPy
import json
import time
import calendar

db = GraphDatabase("http://localhost:7474", username="neo4j", password="abhigna")

##### creating train database #######

train = db.labels.create("Train")
t1 = db.nodes.create(name="howrah-mumbai-cst-durontoexpress",number=12261,total_capacity=700,rundays=["tu","w","th"],type="duronto",start_time=[17,15],end_time=[19,40],total_travel_time=[26,25])
t2 = db.nodes.create(name="kolkata-duronto",number=12273,total_capacity=700,rundays=["m","f"],type="duronto",start_time=[12,45],end_time=[06,25],total_travel_time=[17,40])
t3 = db.nodes.create(name="yeshvantpur-dorontoexpress",number=12214,total_capacity=700,rundays=["m"],type="duronto",start_time=[23,00],end_time=[07,55],total_travel_time=[32,55])
t4 = db.nodes.create(name="howrah-yeshvantpur-duronto",number=12245,total_capacity=700,rundays=["m","tu","w","th","f","sa","s"],type="duronto",start_time=[11,00],end_time=[16,00],total_travel_time=[29,00])
t5 = db.nodes.create(name="howrah-yeshvantpur-sfexpress",number=12863,total_capacity=700,rundays=["m","tu","w","th","f","sa","s"],type="superfast",start_time=[20,35],end_time=[07,45],total_travel_time=[34,40])
t6 = db.nodes.create(name="falaknuma-sfexpress",number=12703,total_capacity=700,rundays=["m","tu","w","th","f","sa","s"],type="superfast",start_time=[07,25],end_time=[9,35],total_travel_time=[26,10])
t7 = db.nodes.create(name="ald-hwh-special",number=4120,total_capacity=700,rundays=["f","s"],type="special",start_time=[20,15],end_time=[16,15],total_travel_time=[20,00])
t8 = db.nodes.create(name="hwh-adi-express",number=12834,total_capacity=700,rundays=["m","tu","w","th","f","sa","s"],type="express",start_time=[23,55],end_time=[9,02],total_travel_time=[33,06])
t9 = db.nodes.create(name="hapa-oka-link",number=22906,total_capacity=700,rundays=["f","sa","tu"],type="regular",start_time=[22,50],end_time=[04,55],total_travel_time=[30,00])
t10 = db.nodes.create(name="poorva-express",number=12303,total_capacity=700,rundays=["m","tu","w","th","f","sa","s"],type="superfast",start_time=[8,05],end_time=[06,05],total_travel_time=[23,10])
t11 = db.nodes.create(name="hwh-jsm",number=12371,total_capacity=700,rundays=["m"],type="express",start_time=[8,15],end_time=[10,20],total_travel_time=[26,00])
t12 = db.nodes.create(name="hwh-chennai-mail",number=12839,total_capacity=700,rundays=["m","tu","w","th","f","sa","s"],type="superfast",start_time=[23,45],end_time=[03,50],total_travel_time=[28,05])
t13 = db.nodes.create(name="kamakhya-ypr-weekly-ac-sfexpress",number=12552,total_capacity=700,rundays=["w"],type="ac-superfast",start_time=[14,00],end_time=[18,25],total_travel_time=[45,15])
t14 = db.nodes.create(name="charminar-sfexpress",number=12760,total_capacity=700,rundays=["m","tu","w","th","f","sa","s"],type="sfexpress",start_time=[18,30],end_time=[8,15],total_travel_time=[13,20])
t15 = db.nodes.create(name="grandtrunk-express",number=12615,total_capacity=700,rundays=["m","tu","w","th","f","sa"],type="sfexpress",start_time=[19,15],end_time=[07,10],total_travel_time=[35,05])
t16 = db.nodes.create(name="geetanjali-express",number=12859,total_capacity=700,rundays=["m","tu","w","th","f","sa","s"],type="sfexpress",start_time=[06,00],end_time=[12,30],total_travel_time=[30,30])
t17 = db.nodes.create(name="cstm-hwh-mail",number=12809,total_capacity=700,rundays=["m","tu","w","th","f","sa","s"],type="sfexpress",start_time=[17,15],end_time=[19,40],total_travel_time=[33,15])
t18 = db.nodes.create(name="satavahana",number=12714,total_capacity=700,rundays=["m","tu","w","th","f","sa","s"],type="sfexpress",start_time=[16,15],end_time=[22,10],total_travel_time=[05,55])
t19 = db.nodes.create(name="secunderabad-rajkot-express",number=17018,total_capacity=700,rundays=["m","tu","sa"],type="express",start_time=[15,00],end_time=[19,00],total_travel_time=[26,00])
t20 = db.nodes.create(name="mumbai-rajdhani",number=12951,total_capacity=700,rundays=["m","tu","w","th","f","sa","s"],type="rajdhani",start_time=[17,00],end_time=[8,35],total_travel_time=[15,35])
t21 = db.nodes.create(name="amritsar-express",number=11057,total_capacity=700,rundays=["m","tu","w","th","f","sa","s"],type="mail-express",start_time=[23,30],end_time=[04,15],total_travel_time=[30,45])
t22 = db.nodes.create(name="mumbai-newdelhi-garibrath",number=12216,total_capacity=700,rundays=["tu","w","f","s"],type="garibrath",start_time=[12,45],end_time=[11,52],total_travel_time=[11,07])
t23 = db.nodes.create(name="ypr-lko-weekly-express",number=22683,total_capacity=700,rundays=["tu"],type="mail-express",start_time=[10,40],end_time=[12,45],total_travel_time=[26,00])
t24 = db.nodes.create(name="mumbai-surat-shatabdi-express",number=12009,total_capacity=700,rundays=["m","tu","w","th","f","sa"],type="shatabdi",start_time=[06,25],end_time=[9,31],total_travel_time=[03,06])

train.add(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23, t24)

#ticket = db.labels.create("Ticket")

station = db.labels.create("Station")
s1 = db.nodes.create(name="mumbai-cst",numplatform=8)
s2 = db.nodes.create(name="secunderabad",numplatform=10)
s3 = db.nodes.create(name="howrah",numplatform=12)
s4 = db.nodes.create(name="vijayawada",numplatform=10)
s5 = db.nodes.create(name="surat",numplatform=8)
s6 = db.nodes.create(name="allahabad",numplatform=10)
s7 = db.nodes.create(name="new-delhi",numplatform=12)
s8 = db.nodes.create(name="chennai-central",numplatform=8)
s9 = db.nodes.create(name="yeshvantpur",numplatform=6)
station.add(s1,s2,s3,s4,s5,s6,s7,s8,s9)

t1.relationships.create("origin", s1)
t16.relationships.create("origin", s1)
t17.relationships.create("origin", s1)
t20.relationships.create("origin", s1)
t21.relationships.create("origin", s1)
t22.relationships.create("origin", s1)
t24.relationships.create("origin", s1)

t3.relationships.create("intermediate",s2)
t14.relationships.create("origin", s2)
t18.relationships.create("origin", s2)
t19.relationships.create("origin", s2)
t23.relationships.create("origin", s2)
t14.relationships.create("intermediate",s2)

t2.relationships.create("origin", s3)
t4.relationships.create("origin", s3)
t5.relationships.create("origin", s3)
t6.relationships.create("origin", s3)
t8.relationships.create("origin", s3)
t9.relationships.create("origin", s3)
t10.relationships.create("origin", s3)
t11.relationships.create("origin", s3)
t12.relationships.create("origin", s3)
t13.relationships.create("origin", s3)

t4.relationships.create("intermediate",s4)
t5.relationships.create("intermediate",s4)
t6.relationships.create("intermediate",s4)
t13.relationships.create("intermediate",s4)
t12.relationships.create("intermediate",s4)
t14.relationships.create("intermediate",s4)
t15.relationships.create("intermediate",s4)

t20.relationships.create("intermediate",s5)
t22.relationships.create("intermediate",s5)

t7.relationships.create("origin", s6)
t10.relationships.create("intermediate",s6)

t3.relationships.create("origin", s7)

t15.relationships.create("origin", s8)
t13.relationships.create("intermediate",s8)

s2.relationships.create("destination", t6)

s3.relationships.create("destination", t7)
s3.relationships.create("destination", t1)
s3.relationships.create("destination", t16)
s3.relationships.create("destination", t17)

s4.relationships.create("destination", t18)

s5.relationships.create("destination", t8)
s5.relationships.create("destination", t9)
s5.relationships.create("destination", t19)
s5.relationships.create("destination", t24)

s6.relationships.create("destination", t23)

s7.relationships.create("destination", t2)
s7.relationships.create("destination", t10)
s7.relationships.create("destination", t11)
s7.relationships.create("destination", t20)
s7.relationships.create("destination", t15)
s7.relationships.create("destination", t21)
s7.relationships.create("destination", t22)

s8.relationships.create("destination",t14)

s9.relationships.create("destination", t3)
s9.relationships.create("destination", t4)
s9.relationships.create("destination", t5)
s9.relationships.create("destination", t13)

class Ticket(htmlPy.Object):
    ticket_count=0
    def __init__(self, app):
        super(Ticket, self).__init__()
        self.app = app

    #use-case-5: generate tickets    
    @htmlPy.Slot(str)
    def generate_tickets(self,ticket):# from, to , doj
    	form_data=json.loads(ticket)
    	print "hello"
    	Ticket.ticket_count=Ticket.ticket_count+1 
    	create_ticket='CREATE (n:Ticket{fro:"'+form_data['fro']+'",to:"'+form_data['to']+'",day:"'+form_data['day']+'",month:"'+form_data['month']+'",year:"'+form_data['year']+'"}) RETURN n'
    	tick=db.query(create_ticket,returns=(str,str,int,int,int,str))
    	#if():
    	#ticket_for_train = 'MATCH (t:Ticket),(tr:Train) WHERE (t.day="'+form_data['day']+'" AND t.month="'+form_data['month']+'") AND tr.name="'+form_data['name']+'" CREATE (tr)-[r:train_ticket{tick_count:"'+str(Ticket.ticket_count)+'"}]->(t) RETURN r.tick_count'
    	#count = db.query(ticket_for_train,returns=(int,int,int,str,int))
    	#increment_count = 'MATCH (t:Ticket)-[r:ticket_train]->(tr:Train) RETURN r.tick_count'
    	#c= db.query(increment_count,returns=(str))																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																	
    	list1=[]
    	for r in tick:
    		print r
    		list1.append(r)
    	#list2=[]
    	#for t in count[0]:
    	#	print t
    	#	list2.append(t)
    	#list3=[]
    	#for f in c[0]:
    	#	print f
    	#	list3.append(f)
    	#print Ticket.ticket_count
    	#return Ticket.ticket_count
    	#self.app.html=unicode(str(list))

    #use-case-6 : check_trains for intermediate stations
    @htmlPy.Slot(str,)
    def check_trains(self,station):# in a station
        #print station
        list2=[]
        form_data = json.loads(station)
        q='MATCH (st1:Station)<-[:intermediate]-(t1:Train)-[:intermediate]->(st2:Station)WHERE st1.name="'+form_data['source']+'" AND st2.name="'+form_data['destination']+'" RETURN DISTINCT t1.name'
        results = db.query(q, returns=(str)) #stores train names
        for r in results:
            list2.append(r)
        self.app.html= unicode(str(list2))   

    #use-case-7: checks ticket availability for a particular train on particular day
    @htmlPy.Slot(str, result=str)
    def ticket_availability(self, train):
    	print train
    	list2=[]
    	Ticket.ticket_count=Ticket.ticket_count+1
        #form_data2 = json.loads(station2)
        week_map={0:"m",1:"tu",2:"w",3:"th",4:"f",5:"sa",6:"s"}
        form_data=json.loads(train)
        fetch_day= form_data['day']
        fetch_month= form_data['month']
        fetch_year = form_data['year']
        #print "hello"
        day_value=calendar.weekday(int(fetch_year),int(fetch_month),int(fetch_day))
        #print day_value
        day_value = int(day_value)
        compare='MATCH (k:Train) WHERE k.name="'+form_data['name']+'" RETURN k.rundays'
        res=db.query(compare,returns=(list))
        #date='MATCH (u:Train)-[r:train_ticket]->(ti:Ticket) W'  #checks for ticket count on that particular day
        #print res
        #ticket_for_train = 'MATCH (t:Ticket),(tr:Train) WHERE (t.day="'+form_data['day']+'" AND t.month="'+form_data['month']+'") AND tr.name="'+form_data['name']+'" CREATE (tr)-[r:train_ticket{tick_count:"'+(str(Ticket.ticket_count)+'"}]->(t) RETURN r.tick_count'
    	#count = db.query(ticket_for_train,returns=(int,int,int,str,int))
        #increment_count = 'MATCH (t:Ticket)-[r:ticket_train]->(tr:Train) RETURN r.tick_count'
    	#c= db.query(increment_count,returns=(str))
    	ticket_for_train = 'MATCH (t:Ticket),(tr:Train) WHERE (t.day="'+form_data['day']+'" AND t.month="'+form_data['month']+'") AND tr.name="'+form_data['name']+'" CREATE (tr)-[r:train_ticket{tick_count:"'+str(Ticket.ticket_count)+'"}]->(t) RETURN r.tick_count'
    	count = db.query(ticket_for_train,returns=(int,int,int,str,int))
        a =[]
        for r in res:
        	a.append(r)
        #print a[0][0]
        list3=[]
    	for f in count:
    		print f
    		list3.append(f)
    	length=len(list3)
    	print length
        for i in a[0][0]:
        	print i
        	print"$$$$$$"
        	print week_map[day_value]
        	if (week_map[day_value]==i):
        		self.app.html=unicode("available")
         	else: 
         		self.app.html=unicode("not available")


        '''
        for r in res:
            for i in range(0,len(r)):
            	if (week_map[day_value]==r[0][0][i]):
            		self.app.html=unicode("available")
            	else: print r
		'''
#d = 'MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r'
#db.query(d,returns=(client.Node, str, client.Node))