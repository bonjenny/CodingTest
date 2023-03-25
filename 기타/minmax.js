function solution(s) {
    let answer = '';
    let array = s.split(' ').map(Number);
    let max = Math.max.apply(null, array);
    let min = Math.min.apply(null, array);
    answer = min.toString() + ' ' + max.toString();
    return answer;
}
