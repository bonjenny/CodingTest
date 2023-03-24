function solution(genres, plays) {
    let answer = [];
    
    let obj = {};
    for (let i=0; i<genres.length; i++) {
        let index = genres[i];
        let play = parseInt(plays[i]);
        obj[index] = obj[index] !== undefined ? obj[index] + play :  play;
        console.log(obj);
    }
    
    let sorted = Object.entries(obj).sort((a, b) => b[1] - a[1]);
    console.log(sorted);
    
    let stack = []
    for (let i=0; i<sorted.length; i++) {
        let genre = sorted[i][0];
        console.log(genre);
        for (let j=0; j<genres.length; j++) {
            if (genre === genres[j]) {
                stack.push(j);
            }
            console.log(stack);
        }
    }
    
    return answer;
}
