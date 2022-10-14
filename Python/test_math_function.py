import math as m

from numpy import roots

def f(x):
    return round((m.asin(2*(x-0.5)))/3.14 + 0.5, 4)

def g(x):
    return round((((1.346*m.asin(2*(x-0.5)))/3.14)**(3/5)) + 0.5, 4)

steps = 25

for t in range(1, steps+1):
    # print(f"t={t} \t g(1/t)={g(t/40)} \t delay={round(g(t/40)*90534)} \t delta_delay={round(g(t/40)*90534 - g((t-1)/40)*90534)} \n")
    print(f"t={t} \t f(1/t)={f(t/steps)} \t delay={round(f(t/steps)*9534)} \t delta_delay={round(f(t/steps)*9534 - f((t-1)/steps)*9534)} \n")

print(f"***** {m.asin(2*(0-0.5))/3.14 + 0.5} ******")