import numpy as np

def delay(data,frame=44100,amp=0.5,repeat=5):
    out = []
    amp_list = [amp ** i for i in range(repeat+1)]

    for i in range(len(data)):
        # y(i)を適宜計算
        d = 0
        for j in range(repeat + 1):
            index = i - frame * j # delay元となるindexを計算
            if index >= 0:
                d += data[index] * amp_list[j]
                d *= 0.7 # 加算しているので適宜クリッピング
        out.append(d) # y(i)をlistに格納

    return np.array(out) # y(n)をnumpy.ndarrayに変換して返す
