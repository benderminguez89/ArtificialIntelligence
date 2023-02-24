from random import random, randrange
# x = x + alpha*gradient(f(x)), where alpha is the step size

def value(problem, state, alpha):
  if problem == "f(x)":
    return 2 - state**2
    #state + alpha*(-2*state)
  elif problem == "g(x)":
    return (0.0051)*(state**5)-(0.1357)*(state**4)+(1.24)*(state**3)-(4.456)*(state**2)+(5.66)*state-0.287
    #state + alpha*((0.0255*state**4)+(0.5468*state**3)+(3.72*state**2)+(8.912*state)+5.66)

def hillClimbing(problem, alpha):
  if problem == "f(x)":
    neighbors = [*range(-5,6)]
  elif problem == "g(x)":
    neighbors = [*range(0,11)]

  index = 0
  flag = True
  current = neighbors[index]
  print(problem, alpha)
  while(current < max(neighbors) and flag):
    neighbor = current + alpha
    print(f"current: {current}, neighbor: {neighbor}")
    if value(problem,neighbor, alpha) <= value(problem, current, alpha):
        flag = False
        return current
    else:
        current = neighbor
        #print(f"n:{value(problem,neighbor, alpha)}, c:{value(problem, current, alpha)}")        
  return current

def randRestartHC(problem, alpha, iterations):
  if problem == "f(x)":
    neighbors = [*range(-5,6)]
  elif problem == "g(x)":
    neighbors = [*range(0,11)]

  temp = 0
  count = 1
  index = 0
  flag = True
  current = neighbors[randrange(0,max(neighbors))]
  print(problem, alpha)
  while(current < max(neighbors) and count < 20):
    neighbor = current + alpha
    print(f"current: {current}, neighbor: {neighbor}")
    if value(problem,neighbor, alpha) <= value(problem, current, alpha):
        print("random restart")
        count += 1
        if value(problem,temp, alpha) <= value(problem, current, alpha):
          temp = current
        current = neighbors[randrange(0,max(neighbors))]
    else:
        current = neighbor
        #print(f"n:{value(problem,neighbor, alpha)}, c:{value(problem, current, alpha)}")        
  return temp


def main():
  step1 = 0.5
  step2 = 0.01
  a1 = hillClimbing('f(x)', step1)
  b1 = hillClimbing('f(x)', step2)
  
  a2 = randRestartHC("g(x)", step1, 20)
  b2 = hillClimbing("g(x)", step1)
  print("______________________________\n")
  print(f"1A:\t{a1}")
  print(f"1B:\t{b1}")
  print(f"2A:\t{a2}")
  print(f"2B:\t{b2}")
#if __name__ == "main":

main()
