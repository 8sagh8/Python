# -*- coding: utf-8 -*-
"""
title: ISHA QAZA TIME CALCULATOR

created by: SAMMAR ABBAS
"""

def hr_mint(time):
    pos = time.find(":")
    hr = int(time[0:pos])
    mint = int(time[pos+1:])
    
    lst = []
    lst.append(hr)
    lst.append(mint)
    
    return lst

def accurate_time(time, event):
    new_time = ""
    while time[0] < 0 or time[0] > 24 or time[1] < 0 or time[1] > 60 or (time[0] == 24 and time[1] > 0):
        new_time = input (f"INVALID TIME: enter correct {event} time: ")
        time = hr_mint(new_time)

    return time

def diff_time (fajr_time, magrib_time):
    fj_hr = fajr_time[0]
    mg_hr = magrib_time[0]
    
    while not(fj_hr == mg_hr):
        fj_hr -= 1
        if not(fj_hr == mg_hr):
            if fj_hr == 0:
                fj_hr = 24
    
        if not (fj_hr == mg_hr):
            mg_hr += 1
            if not(fj_hr == mg_hr):
                if mg_hr == 24:
                    mg_hr = 0    
    mid_hr = fj_hr
    print(f"Done line 44: fajr time: {fj_hr} .. mgrib: {mg_hr}")
    fj_hr = ((mid_hr + 1) * 60) + fajr_time[1]
    mg_hr = ((mid_hr - 1) * 60) + magrib_time[1]
    print(f"fajr time: {fj_hr} .. mgrib: {mg_hr}")
    while not(fj_hr == mg_hr):
        fj_hr -= 1
        print(f"Done line 50: fajr time: {fj_hr} .. mgrib: {mg_hr}")
        if fj_hr == 0:
            fj_hr = 12 * 60
        mg_hr += 1
        
    mid = fj_hr
    lst = []
    lst.append(mid // 60)
    lst.append(mid % 60)
    
    return lst
    
  #######  MAIN PART ########
magrib_time = []
fajr_time = []
time = []
  
magrib = input("Please enter Magrib time: ")
time = hr_mint(magrib)
time[0] = time[0] + 12
magrib_time = accurate_time(time, "Magrib")
    
fajr = input("Please enter Fajr time: ")
time = hr_mint(fajr)
fajr_time = accurate_time(time, "Fajr")

time = diff_time (fajr_time, magrib_time)

if magrib_time[0] < 12:
    magrib_time[0] = magrib_time[0] - 12

print()
print(f"fajr is at {fajr_time[0]}:{fajr_time[1]} am and magrib is at {magrib_time[0]}:{magrib_time[1]} pm")
print
print(f"Esha will Qaza at {time[0]}:{time[1]}", end='')

if time[0] < 12:
    print("pm.")
else:
    print("am.")