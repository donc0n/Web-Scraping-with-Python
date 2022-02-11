# ch05-7.py에서 저장한 DB로부터 BFS 방식으로 케빈 베이컨 페이지부터 타켓 페이지까지의 링크를 검색하는 코드  

import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='$lothd@m0n', db='mysql', charset='utf8')

cur = conn.cursor()
cur.execute("USE wikipedia")

class SolutionFound(RuntimeError):
    def __init__(self, message) -> None:
        self.message = message

def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]

def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}]*len(links)))
    return {}

# 링크 트리가 비어 있거나 링크가 여러 개 들어 있다.
def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        # 재귀를 중지하고 함수 종료
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            # 링크가 발견되지 않았으므로 이 노드에서는 탐색 불가
            return {}
    if targetPageId in linkTree.keys():
        print("TARGET "+str(targetPageId)+" FOUND!")
        raise SolutionFound("PAGE: "+str(currentPageId))

    for branchKey, branchValue in linkTree.items():
        try:
            # 재귀적으로 돌아와서 링크 트리 구축
            linkTree[branchKey] = searchDepth(targetPageId, branchKey, branchValue, depth-1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound("PAGE: "+str(currentPageId))
    return linkTree

try:
    searchDepth(2000, 2, {}, 5)
    print("No solution found")
except SolutionFound as e:
    print(e.message)