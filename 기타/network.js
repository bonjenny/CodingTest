function solution(n, computers) {
    let answer = 0;
    let i, j, flag;
    const n_stack = Array.from({length: n}, (v, i) => i);
    
    let line = [0];
    for (i=0; i<line.length; i++) {
        for (j=0; j<computers[line[i]].length; j++) {
            if (line[i] !== j && !line.includes(j) && computers[line[i]][j] === 1) {
                line.push(j);
            }
        }
    }
    console.log(line);
    
    let diff = n_stack.filter(x => !line.includes(x));
    if (diff.length === 0) return 1;
    
    let a_stack = new Set();
    for (i=0; i<diff.length; i++) {
        console.log(diff[i]);
        flag = 0;
        for (j=0; j<computers[diff[i]].length; j++) {
            console.log(diff[i], j, computers[diff[i]]);
            if (diff[i] !== j && computers[diff[i]][j] === 1) {
                console.log(i, j, computers[diff[i]][j]);
                flag = 1;
                if (!diff.includes(j)) diff.push(j);
            }
        }
        if (flag === 0) a_stack.add(diff[i]);
    }
    console.log('a_stack', a_stack);
    
    answer = a_stack.size + 1;
    return answer;
}
