function solution(s)
{
    let answer = -1;
    let flag = 0;
    
    for (let i=0; i<s.length-1; i++) {
        if (s[i] == s[i+1]) {
            s = s.slice(0, i) + s.slice(i+2);
            console.log('i:', i, s);
            flag = 1;
            break;
        }
    }
    if (flag == 0) { return 0; }
    
    flag = 1;
    
    while (true) {
        if (flag == 0) { break };
        flag = 0;
        for (let i=0; i<s.length-1; i++) {
            if (s[i] == s[i+1]) {
                s = s.slice(0, i) + s.slice(i+2);
                console.log('i:', i, s);
                flag = 1;
                break;
            }
        }
    }
    console.log('최종', s);
    
    if (s.length == 0) {
        answer = 1;
    }
    else {
        answer = 0;
    }

    return answer;
}
