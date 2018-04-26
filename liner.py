def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * modinv(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

s0 = 2818206783446335158
s1 = 3026581076925130250
s2 = 136214319011561377
s3 = 359019108775045580
s4 = 2386075359657550866
s5 = 1705259547463444505
s6 = 2102452637059633432

s1 = s0*m + c  (mod n)
s2 = s1*m + c  (mod n)
s3 = s2*m + c  (mod n)
t0 = s1 - s0
t1 = s2 - s1 = (s1*m + c) - (s0*m + c) = m*(s1 - s0) = m*t0 (mod n)
t2 = s3 - s2 = (s2*m + c) - (s1*m + c) = m*(s2 - s1) = m*t1 (mod n)
t3 = s4 - s3 = (s3*m + c) - (s2*m + c) = m*(s3 - s2) = m*t2 (mod n)
