const dfs = (num, target, path) => {
  // numbers 배열에 들어있는 숫자들을 전부 다 사용한 경우 target값과 비교
  if (path.length === 0) {
    return num === target ? 1 : 0;
  }
  // 배열의 첫 번째 숫자를 더하는 경우와 빼는 경우 전부 다 고려
  return (
    dfs(num + path[0], target, path.slice(1)) +
    dfs(num - path[0], target, path.slice(1))
  );
};

const solution = (numbers, target) => {
  count = 0;
  count += dfs(0, target, numbers);
  return count;
};

//test
console.log(solution([1, 1, 1, 1, 1], 3));
