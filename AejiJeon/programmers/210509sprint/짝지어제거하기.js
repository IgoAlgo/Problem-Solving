function solution(s) {
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    stack.push(s.charAt(i));

    // 짝이 있는 경우 -> stack에서 제거
    if (
      stack.length >= 2 &&
      stack[stack.length - 1] === stack[stack.length - 2]
    ) {
      stack.pop();
      stack.pop();
    }
  }
  // stack이 빈 경우 -> 모든 문자들이 짝지어 제거됨
  return stack.length === 0 ? 1 : 0;
}

// test
console.log(solution("baabaa"));
console.log(solution("cdcd"));
