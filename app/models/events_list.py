from app.models.event import *


event1 = Event("03/12/2020", 
"Santas Grotto", 
"50", 
"The North Pole", 
"Tours of Santas Grotto", "true")
events = []

def add_new_event(event):
    events.append(event)