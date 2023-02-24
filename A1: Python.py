#using the distance formula and the radius to determine whether circles intersect
# sqrt((x2-x1)**2 + (y2 - y1)**2)

def calcDistance(circle1, circle2):
  x1 = circle1[0]
  y1 = circle1[1]
  
  x2 = circle2[0]
  y2 = circle2[1]
  
  distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

  return distance

def isCluster(c_tuples):  
  for i in range(len(c_tuples)-1):
    #iterate through the list of circles to determine if radii overlap
    j = i + 1
    r1 = c_tuples[i][2]
    r2 = c_tuples[j][2]
    print(f"x1: {c_tuples[i][0]}, y1: {c_tuples[i][1]}, radius1: {r1}")
    print(f"x2: {c_tuples[j][0]}, y2: {c_tuples[j][1]}, radius2: {r2}")

    dististance = calcDistance(c_tuples[i], c_tuples[j])

    print(f"Distance between circles is {dististance}, radii combined is {r1 + r2}")
    if dististance > (r1 + r2):
      print(f"Distance between circles is {(dististance - (r1 + r2))}")
      print("False")
      return False
  return True
    
def main(): 
  #test cases, lists of tuples representing circles as follows: [(x_coord, y_coord, radius),...]
  test1 = [(1,3,0.7),(2,3,0.4),(3,3,0.9)]
  test2 = [(1.5,1.5,1.3),(4,4,0.7)]
  test3 = [(0.5,0.5,0.5),(1.5,1.5,1.1),(0.7,0.7,0.4),(4,4,0.7)]
  test4 = [(2,2,2),(2,2,1),(2,2,5),(3,2,0.5)]
  #test suite containing all test cases 
  testSuite = [test1, test2, test3, test4]

  for i in testSuite:
    print(f"\ntest case {i}")
    if isCluster(i):
      print("True")

if __name__ == "__main__":
  main()
