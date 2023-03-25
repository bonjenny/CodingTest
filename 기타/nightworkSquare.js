function solution(n, works) {
    var answer = 0;
    works = works.sort((a, b) => b-a);

    let i=0;
    while (n > 0) {
        if (works[works.length -1] === 0) break;
        if (works[i] < works[i+1]) i++;
        if (works[0] >= works[i]) i=0;
        if (i > works.length) { i=0; }
        works[i] -= 1;
        n--;
    }

    for (i=0; i<works.length; i++) {
        answer += works[i]**2;
    }
    return answer;
}
