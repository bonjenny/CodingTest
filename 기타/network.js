function solution(n, computers) {
    let answer = 0;
    let stack = [];
    let s;
    let temp = [];
    let flag = [];
    
    for (let i=0; i<computers.length; i++) {
        s = new Set([i]);
        for (let j=i+1; j<computers[i].length; j++) {
            if (computers[i][j] === 1) { s.add(j); }
        }
        
        if (stack.length === 0) { stack.push(s); continue; }
        flag = [];
        
        for (j=0; j<stack.length; j++) {
            // console.log(i, '비교:', stack[j], s, [...stack[j]].filter(x => s.has(x)));
            if ([...stack[j]].filter(x => s.has(x)).length !== 0) {
                temp = [...stack[j]];
                stack[j] = new Set([...s, ...temp]);
                flag.push(j);
                // console.log(flag);
            }
        }
        
        if (flag.length === 0) { stack.push(s); }
        else {
            for (j=0; j<flag.legnth; j++) {
                // console.log('얍!');
            }
        }
    }
    
    answer = stack.length;
    return answer;
}
