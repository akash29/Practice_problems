def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    i = 0
    while days > 0:
        prev_value = 0
        while i < len(states):
            if i == 0:
                prev_value = states[i]
                states[i] = states[i+1] ^ 0
            elif i+1 == len(states):
                temp = states[i]
                states[i] = prev_value ^ 0
                prev_value = temp
            else:
                temp = states[i]
                states[i] = prev_value ^ states[i+1]
                prev_value = temp
            i+=1
        days-=1
        i=0
    print (states)

stat = [1,1,1,0,1,1,1,1]
days=2
print (120>>1)
cellCompete(stat,days)