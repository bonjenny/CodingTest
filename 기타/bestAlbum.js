function solution(genres, plays) {
    
    let obj = {};
    for (let i=0; i<genres.length; i++) {
        let genre = genres[i];
        let play = parseInt(plays[i]);
        obj[genre] = obj[genre] !== undefined ?
            {
                sum : obj[genre].sum + play,
                index: [...obj[genre].index, i]
            } :
            {
                sum : play,
                index: [i]
            };
    }
    
    let stack = [];
    for (key of Object.keys(obj)) {
        stack.push({
            name: key,
            ...obj[key]
        });
    }
    
    let sorted = stack.sort(function(a, b) {
        return b.sum - a.sum;
    });
    
    let answer = [];
    for (i=0; i<sorted.length; i++) {
        stack = [];
        for (key of sorted[i].index) {
            stack.push({index: key, plays: plays[key]})
        }
        stack = stack.sort(function(a, b) {
            return b.plays - a.plays
        });
        if (stack.length >= 2) {
            for (let j=0; j<2; j++) {
                answer.push(stack[j].index);
            }
        } else {
            answer.push(stack[0].index);
        }
    }
    return answer;
}
