import datetime
from time import sleep
class person():
    def __init__(self,name,last,age,haircolor,eyecolor):
        self.first_name= name
        self.last_name= last
        self.gender= ""
        self.weight= 0
        self.height= 0
        self.age= age
        self.strength= 0
        self.speed= 0
        self.haircolor= haircolor
        self.eyecolor= eyecolor
        self.race= ""
        self.vision= 0
        self.voice= 0
        self.iq= 0
        self.bday= datetime.datetime.now()
        self.lastbday= self.bday
    def intro(self):
        print("Hello my name is "+self.first_name +" "+ self.last_name+" I have "+ self.eyecolor + " eyes and "+ self.haircolor+ " hair. I am "+ str(self.age) +" years old")
    def get_older(self):
        ctime= datetime.datetime.now().time()
        delta= datetime.timedelta(minutes= 1)
        checktime= self.lastbday + delta
        if ctime >= checktime:
            self.age+= 1
            self.lastbday= ctime
    def old(self):
        self.age+=1
    def consume(self):
        print("what would you like to eat today")
bob= person("bob","ross",90,"grey","blue")
bob.intro()
isa= person("Isabella","End",45,"blue","brown")
isa.intro()
sam= person("Sam","Time",25,"brown","green")
sam.intro()
cob= person("old","Cob",320,"grey","blue")
cob.intro()
kim= person("Kim","Kill",28,"black","red")
kim.intro()
tim= person("tim","tim",4,"blonde","blue")
tim.intro()
print(bob)
print(isa)
print(sam)
#myOffset   = datetime.timedelta(hours=-7)
#myTimezone = datetime.timezone(myOffset   )
#now= datetime.datetime.now(myTimezone)
#currentTime = datetime.time(now.hour, now.minute, now.second, 0, myTimezone)
#print(currentTime.strftime("%I:%M
while True:
    cob.intro()
    sleep(6)
    cob.old()