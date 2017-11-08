import controller
import interface

c = controller.Controller()
i = interface.Interface(c)
active = True
print("Scavenger hunt program now running. Enter -1 to quit")
while active == True:
  ret = input(">")
  if ret == "-1":
    active = False
  else:
    i.command(ret)
  

print("test game setup\n")
i.command("login admin kittens")
i.command("create landmark l1 c1 q1 a1")
i.command("create landmark l2 c2 q2 a2")
i.command("create team t1 p1")
i.command("create game l1,l2,l3 t1,t2")   #should fail
i.command("create game l1,l2 t1")
i.command("start")
if(c.Game.isActive):
    print("success!\n")

print("test game interaction GM")
i.command("get status")   #GM status, all teams
i.command("end")
i.command("logout")
if(c.Game.isActive == False):
    print("success!\n")

c.Game.isActive = True

print("test game interaction user")
i.command("login t1 p1")
i.command("create team t2 p2")
i.command("login t2 p2")
i.command("get status")
#i.command("

