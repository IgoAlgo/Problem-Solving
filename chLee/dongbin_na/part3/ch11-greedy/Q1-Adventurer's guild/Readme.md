# 모험가 길드

## Solution
공포도 내림차순 정렬. 앞에서부터 그대로 팀 인원 채우기.
-> 조건을 확인안함 **모든 모험가를 넣을 필요가 없다!!!!**  
1 1 1 1 4의 경우, 그룹 4개를 만들 수 있어야 하지만, 이 방식대로 풀면 2개 그룹밖에 못만듦.


## Solution - official
오름차순 정렬 -> 하나씩 그룹에 넣고, *조건*에 부합하면 그룹 수 증가시키기    
*조건: '마지막으로 추가된 모험가의 공포도' <= '그룹에 포함된 모험가의 수'*