# Union-Find 알고리즘 사용!
# 이 알고리즘에서는 싸이클 발생 여부를 확인하기 위해 사용!
def get_parent(parent_list, element):
  if parent_list[element] == element:
    return element
  parent_list[element] = get_parent(parent_list, parent_list[element])
  return parent_list[element]

def union_parent(parent_list, element1, element2):
  element1 = get_parent(parent_list, element1)
  element2 = get_parent(parent_list, element2)
  if element1 < element2:
    parent_list[element2] = element1
  else:
    parent_list[element1] = element2

def find_parent(parent_list, element1, element2):
  element1 = get_parent(parent_list, element1)
  element2 = get_parent(parent_list, element2)
  if element1 == element2:
    return True
  return False

# 간선 클래스 선언
class Edge:
  distance = 0

  def __init__(self, a, b, distance):
    self.node = [0, 0]
    self.node[0] = a
    self.node[1] = b
    self.distance = distance

node = 7
line = 11
edge_list = list()

edge_list.append(Edge(1, 7, 12))
edge_list.append(Edge(1, 4, 28))
edge_list.append(Edge(1, 2, 67))
edge_list.append(Edge(1, 5, 17))
edge_list.append(Edge(2, 4, 24))
edge_list.append(Edge(2, 5, 62))
edge_list.append(Edge(3, 5, 20))
edge_list.append(Edge(3, 6, 37))
edge_list.append(Edge(4, 7, 13))
edge_list.append(Edge(5, 6, 45))
edge_list.append(Edge(5, 7, 73))

# 간선의 비용을 기준으로 오름차순 정렬
# 정렬을 위해 퀵소트 사용
def quick_sort(a, start, end):
  if end- start <= 0:
      return
  pivot = a[end]
  i = start
  for j in range(start, end):
    if a[j].distance <= pivot.distance:
      a[i], a[j] = a[j], a[i]
      i += 1
  a[i], a[end] = a[end], a[i]
  quick_sort(a, start, i-1)
  quick_sort(a, i+1, end)

quick_sort(edge_list, 0, len(edge_list)-1)

# 각 정점이 포함된 그래프가 어디인지 저장
parent= [i for i in range(node)]

sum = 0
for i in range(len(edge_list)):
  # 사이클이 발생하지 않는 경우 그래프에 포함
  if not find_parent(parent, edge_list[i].node[0]-1, edge_list[i].node[1]-1):
    sum += edge_list[i].distance
    union_parent(parent, edge_list[i].node[0]-1, edge_list[i].node[1]-1)
print(sum)

