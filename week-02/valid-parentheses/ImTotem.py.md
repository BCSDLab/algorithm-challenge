# Intuition

스택을 이용해서 괄호를 판단한다.
# Approach

1. 괄호 쌍을 딕셔너리로 저장한다.
2. 스택에 괄호 외의 아무 문자(여기서는 '.')를 하나 넣어 생성한다.
	- 이렇게 하면 스택이 비어있는지 확인하는 조건 하나를 지울 수 있다.
3. 문자열을 순회하며 각 문자 $i$에 대해:
	- $i$가 여는 괄호("(", "{", "[")라면 스택에 추가한다.
	- $i$가 닫는 괄호라면 스택의 마지막 값을 pop하여 괄호 쌍이 되는지 확인한다.
		- 쌍이 맞지 않으면 즉시 False를 반환한다.
4. 모든 문자를 처리한 후, 스택에 초기에 넣은 '.' 문자만 남아있는지 확인한다.

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(n)$$
$n$은 문자열의 길이

# Code
```python
def isValid(s: str) -> bool:
    MAP = {")": "(", "}": "{", "]": "["}
    stack = ['.']
    for i in s:
        if i in "({[": stack.append(i)
        elif (stack.pop() != MAP[i]): return False
    
    return stack.pop() == '.'

with open("user.out", "w") as f:
    for case in map(loads, stdin):
        f.write(f"{str(isValid(case)).lower()}\n")

exit()
```