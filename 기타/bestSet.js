function solution(n, s) {
    let answer = [];
    if (s/n < 1) {
        return [-1];
    }
    
    let floor = Math.floor(s/n);
    for (let i=0; i<n; i++) {
        answer.push(floor);
    }
    let rest = s - floor*n;
    for (i=n-1; i>0; i--) {
        if (rest <= 0) {
            break;
        }
        answer[i] += 1;
        rest --;
    }
    return answer;
}
