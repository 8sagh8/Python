
##########One Pie out --  PIE CHART #############

from matplotlib import pyplot as plt

def avg (l):
    s = 0
    for i in l:
        s = s + i
    a = s / len(l)
    return a


days = [1,2,3,4,5,6,7]

sleeping = [8,7,6,7,5,4,9]
study = [4,2,6,1,3,5,5]
workout = [1,2,1,1,2,3,1]
phone=[5,3,2,4,1,3,4]
other=[6,10,9,11,13,9,5]

hrs = [avg(sleeping),avg(study),avg(workout),avg(phone),avg(other)]  # taking avg of all the activities
activities = ["sleeping", "study", "workout", "phone", "other"] #labels list
clrs = ["m", "c", "r", "k", "b"] #colors list

plt.pie(hrs, labels = activities, colors = clrs, explode = (0.3,0,0,0.1,0)) #explode is to pull a pie out

plt.title("PIE CHART")  # title


plt.show()
