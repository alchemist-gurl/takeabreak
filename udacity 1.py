import time
import webbrowser

total_breaks = 3
break_count = 0
print("time started at " + time.ctime())
while(break_count < total_breaks):
    time.sleep(3*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=itKtosLoGk4&frags=pl%2Cwn")
    break_count = break_count + 1