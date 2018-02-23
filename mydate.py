import datetime
class mydate():
    _y = int(str(datetime.datetime.now().date()).split('-')[0])
    _m = int(str(datetime.datetime.now().date()).split('-')[1])
    _d = int(str(datetime.datetime.now().date()).split('-')[2])

    def __init__(self,y=_y,m=_m,d=_d):

        self.y=y
        self.m=m
        self.d=d
        self.now=datetime.datetime(y,m,d).date()

    def __repr__(self):
        return str(self.now)

    def next(self):
        return mydate(self.y,self.m,self.d+1)



