function solution(genres, plays) {
    let answer = [];
    
    let obj = {};
    for (let i=0; i<genres.length; i++) {
        let genre = genres[i];
        let play = parseInt(plays[i]);
        obj[genre] = obj[genre] !== undefined ?
            {
                sum : obj[genre].sum + play,
                index: [...obj[genre].index, i],
                plays: [...obj[genre].plays, play]
            } :
            {
                sum : play,
                index: [i],
                plays: [play]
            };
    }
    console.log(obj);
    
    
    
    return answer;
}
