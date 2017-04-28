import htmlPy
import json
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client 
import train 
from train import station as cs
import time
import random
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client 

#db = GraphDatabase("http://localhost:7474", username="neo4j", password="abhigna")

db = GraphDatabase("http://localhost:7474", username="neo4j", password="abhigna")


class BackEnd(htmlPy.Object):	
    def __init__(self, app):
        super(BackEnd, self).__init__()
        self.app = app

    #use-case-1: Generate trains    
    @htmlPy.Slot()
    def generate_trains(self):
        list=[]
        names = 'MATCH (t:Train) RETURN DISTINCT t.name'
        results = db.query(names, returns=(str))  
        for r in results:
            list.append(r)
        self.app.html = unicode(str(list))

    #use-case-2: Connecting trains
    @htmlPy.Slot()
    def connecting_train(self):
        list=[]
        connectors='MATCH (r:Train)-[:origin]->(s:Station)-[:destination]->(t:Train) RETURN DISTINCT r.name,s.name,t.name'
        #connectors='MATCH '
        re = db.query(connectors, returns=(str,str,str))
        for r in re:
            list.append(r)
        self.app.html = unicode(str(list))

    #use-case-3: trains between two stations
    @htmlPy.Slot(str, result=str)
    def find_trains(self, station):
        print station
        list2=[]
        form_data1 = json.loads(station)
        #form_data2 = json.loads(station2)
        print form_data1['name1']
        print form_data1['name2']
        q = 'MATCH (st1:Station)-[:destination]->(t:Train)-[:origin]->(st2:Station) WHERE st1.name="'+form_data1['name1']+'" AND st2.name="'+form_data1['name2']+'" RETURN DISTINCT t.name'# "db" as defined above
        print 'Hello 2'
        results = db.query(q, returns=(str))
        for r in results:
            list2.append(r)
        self.app.html= unicode(str(list2))
    
    #use-case-4: show delay time
    @htmlPy.Slot(str,result=str)
    def show_train_delay(self,train_name):
        form_data=json.loads(train_name)
        #station = db.labels.create("Station")
        #s90=db.nodes.create(name="'+form_data['train']+'",numplatform=12)
        #station.add(s90)
        #station_name='MATCH (d:Station) WHERE d.name="'+form_data['train']+'" RETURN DISTINCT d.name'
        #e=db.query(station_name,returns=(str))
        #for w in e:
         #   print ("%s" % (w[0]))
        arrival_time='MATCH (st1:Train) WHERE st1.name="'+form_data['train']+'" RETURN DISTINCT st1.start_time[0],st1.start_time[1]'
        re=db.query(arrival_time,returns=(int))
        for r in re:
            list_standard=[]
            list_standard.append(r[0])
            list_standard.append(r[1])
            a=random.randint(r[0]-1,r[0]+2)
            b=random.randint(r[1],r[1]+59)
            delay_time = a-list_standard[0]
            if (delay_time>0):
                self.app.html=unicode("train is delayed by" + str(delay_time) + "hour")
            else:
                self.app.html=unicode("train scheduled on correct time")
    
