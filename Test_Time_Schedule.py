import time
import schedule
import datetime


def job():
    f = open('datetime.txt','a')
    f.write(datetime.datetime.now().strftime("%c\r"))
    f.close()
    print 'logged Datetime'
    

#Not Working 
#for x in range(0,9):
#    schedule.every(1).second.do(job)
#    (X)



schedule.every(1).hour.do(job)

#schedule.every().day.at("04:19").do(job)
#schedule.every().day.at("04:22").do(job)
#schedule.every().day.at("23:00").do(job)
#schedule.every().day.at("24:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
