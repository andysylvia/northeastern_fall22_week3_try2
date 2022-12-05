



import time

def three_one_answer():

    epoch = time.time() #amount of time in epoch

    total_sec = epoch % 86400 #modulo remainder seconds in epoch, used for calculating epoch time

    hours = int (total_sec//3600)%12 # current time in hours, epoch seconds/number of seconds in an hour without a remainder

    mins = int(total_sec//60)%60#current time in minutes, epoch seconds/number of seconds in a minute without a remainder

    sec = int(total_sec//1)%60 #current time in seconds, removing remainder

    days = int(epoch//86400) #days since epoch, no remainder



    # Convert from numeric values to character strings, in preparation for printing.

    hours = str(hours)

    mins = str(mins)

    sec = str(sec)

    days = str(days)



    # Add leading zero if necessary.

    if (len(hours)<2):

        hours = str(0) + hours

    if (len(mins)<2):

        mins = str(0) + mins

    if (len(sec)<2):

        sec = str(0) + sec



    # Print results

    print("")

    print ("The Current Time (GMT) Is: " + hours + ":" + mins + ":" + sec)

    print ("Days since Epoch: " + days)

    print("")





three_one_answer()

