function solution(n, computers) {
    let i, j, count=0;
    let flag = Array.from({length: n}).fill(0);
    
    const n_stack = Array.from({length: n}, (v, i) => i);
    let alone_stack = [];
    let line_stack = [];
    
    const dfs = (line, computer) => {
        for (let i=0; i<line.length; i++) {
            for (let j=0; j<computer[line[i]].length; j++) {
                if (line[i] !== j && !line.includes(j) && computer[line[i]][j] === 1) {
                    line.push(j);
                    flag[j] = 1;
                }
            }
        } return [...new Set(line.sort((a, b) => a-b))];
    };
    
    for (i=0; i<n; i++) {
        line_stack = [];
        if (flag[i] === 1) continue;
        for (j=0; j<computers[i].length; j++) {
            if (i !== j && computers[i][j] === 1) {
                line_stack.push(j); flag[j] = 1;
            }
        }
        dfs(line_stack, computers);
        count++;
    }
    
    return count;
}
