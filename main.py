import time, os

timer_input = input("Enter time in minute : ")
timer = timer_input.split(":")
hour = timer[0]
minute = timer[1]
second = timer[2]

for hours in range (int(hour), -1, -1):
    for mins in range (int(minute), -1, -1):
        for sec in range (int(second), -1, -1):
            os.system('cls')
            time_remaining = f"{hours} jam {mins} menit {sec} detik"
            print("+" + "-" * 30 + "+")
            print("|", end="")
            print('{:^30s}'.format("Timer"), end="")
            print("|")
            print("+" + "-" * 30 + "+")
            print("|", end="")
            print('{:^30s}'.format(time_remaining), end="")
            print("|")
            print("+" + "-" * 30 + "+")
            time.sleep(1)
        second = 59
    minute = 59


print(" "*100, end='\r')
print("waktu hbis bg, turu")