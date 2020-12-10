bit_depth = 8
def bin_convert(n):
    N = bit_depth - 1
    p = 0
    X = []
    while N > 0:
        p = int(n/2**N)
        if p == 1:
            X.append(1)
            n -= 2**N
        else:
            X.append(0)
        N -= 1
    X.append(n)
    return X
print (bin_convert(255))

time = np.arange(0,t,1/48000)
time.sleep(0.05)
amplitude = (127*np.sin(w*time)+128)
lightNumber(amplitude)
plt.plot(time,amplitude)
plt.title('label')
plt.xlabel('label')
plt.ylabel('label')
plt.show()
pervi.GPIO.cleanup()