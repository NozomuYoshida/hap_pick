def distortion(data,amp = 5.0,level=0.7):
    out = []
    for d in data:
        d *= amp
        d = min(d,1.0)
        d = max(d,-1.0)
        out.append(d)
    return np.array(out) * level
