function solution(n, computers) {
    let answer = 0;
    let stack = [];
    let s;
    let flag;
    
    for (let i=0; i<computers.length; i++) {
        s = [i];
        for (let j=i+1; j<computers[i].length; j++) {
            if (computers[i][j] === 1) { s.push(j); }
        }
        if (stack.length === 0) { stack.push(s); }
        else {
            flag = 0;
            for (j=0; j<stack.length; j++) {
                if (stack[j].filter(it => s.includes(it)).length !== 0) {
                    stack[j] = stack[j].concat(s);
                    flag = 1;
                    break;
                }
            }
            if (flag === 0) {
                stack.push(s);
            }
        }
    }
    
    answer = stack.length;
    return answer;
}
