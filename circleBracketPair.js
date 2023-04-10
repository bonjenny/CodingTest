function solution(s) {
    let answer = true;
    let stack = [];
    
    if (s[0] === ')') {
        return false;
    }
    
    stack.push(s[0]);
    for (let i=1; i<s.length; i++) {
        if (s[i] === ')') {
            stack.pop();
            console.log(stack);
        } else {
            stack.push(s[i]);
            console.log(stack);
        }
    }
    
    answer = stack.length === 0 ? true : false;
    return answer;
}
