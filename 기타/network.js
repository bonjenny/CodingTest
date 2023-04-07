function solution(n, computers) {
    let answer = 0;
    let i, j;
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
    
    for (i=0; i<diff.length; i++) {
        for (j=0; j<computers[diff[i]].length; j++) {
            console.log(diff[i], j, computers[diff[i]]);
            if (diff[i] !== j && computers[diff[i]][j] === 1) {
                console.log(i, j, computers[diff[i]][j]);
                diff.push(j);
            }
        }
    }
    
    return answer;
}
