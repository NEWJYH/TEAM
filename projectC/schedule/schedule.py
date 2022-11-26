import threading 
import time
# test code
class BackgroundTasks(threading.Thread):
    def __init__(self):
        super().__init__()
        self.curtime = None

    def set_time(self):
        self.curtime = time.localtime()

    def set_fuction(self, fuc):
        pass


    def run(self,*args,**kwargs):
        a = True
        while True:
            self.set_time()
            if a == True:
                if self.curtime.tm_sec == 0:
                    a = False
                    # print(self.curtime)
                    # print('this')
            if a == False:
                if self.curtime.tm_sec == 5:
                    a = True
