import turtle as k 
import time 
for i in range(99):
    k.color("red")
    k.speed(100)
    k.circle(55)
    k.forward(0.5)
    k.left(67)
for i in range(11):
    print(f"\rProcessing step {i}/10", end="", flush=True)
    time.sleep(0.5)
print("\nTURTLE DONE")
k.done()
