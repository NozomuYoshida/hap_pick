class Tremolo():
    '''
    member
        depth : 変調深度
        freq  : 変調周波数[hz]
        rate  : サンプリングレート[hz]
        n     : 現在フレーム
    '''
   
    def __init__(self,depth=0.2, freq=2, rate=44100):
        self.depth = depth
        self.freq  = freq
        self.rate  = rate 
        self.n     = 0

    def process(self,data):
        vfunc = np.vectorize(self.effect)
        return vfunc(data)

    def effect(self,d):
        d = d * (1.0 + self.depth * np.sin(self.n * ( 2 * np.pi * self.freq / self.rate)))
        self.n += 1
        return d

# in_dataにnumpy.array型の信号を格納済み
tremolo = Tremolo()
out_data = tremolo.process(in_data)
