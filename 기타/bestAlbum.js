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
    // console.log(obj);
    
    let stack = [];
    for (key of Object.keys(obj)) {
        stack.push({
            name: key,
            ...obj[key]
        });
    }
    // console.log(stack);
    
    let sorted = stack.sort(function(a, b) {
        return b.sum - a.sum;
    });
    // console.log(sorted);
    
    let answer = [];
    for (i=0; i<sorted.length; i++) {
        stack = [];
        for (key of sorted[i].index) {
            stack.push({index: key, plays: plays[key]})
            // console.log(stack);
        }
        stack = stack.sort(function(a, b) {
            return b.plays - a.plays
        });
        console.log(stack);
        for (let j=0; j<2; j++) {
            answer.push(stack[j].index);
        }
        console.log(answer);
    }
    return answer;
}
