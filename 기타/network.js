function solution(n, computers) {
    let answer = 0;
    let stack = [];
    let s;
    
    for (let i=0; i<computers.length; i++) {
        s = [i];
        for (let j=i+1; j<computers[i].length; j++) {
            if (computers[i][j] === 1) {
                s.push(j);
                // console.log(i, j, s, stack);
            } else {
                // console.log(i, j, s, stack);
            }
        }
        if (stack.length === 0) { stack.push(s); }
        else {
            for (j=0; j<stack.length; j++) {
                // console.log('비교:', 's', s, 'stack', stack, '결과', stack[j].filter(it => s.includes(it)));
                if (stack[j].filter(it => s.includes(it)).length === 0) {
                    stack.push(s);
                    // console.log(j, 's', s, 'stack', stack);
                    break;
                } else {
                    stack[j] = stack[j].concat(s);
                    // console.log('s', s, 'stack', stack);
                }
            }
        }
    }
    
    answer = stack.length;
    return answer;
}
