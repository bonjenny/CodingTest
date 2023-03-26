function solution(s) {
    let answer = s.toLowerCase().split(' ').map((str) => str.charAt(0).toUpperCase() + str.slice(1)).join(' ');
    return answer;
}
