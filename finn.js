function solution(n) {
    var answer = 0;
    str = n.toString();
    if (['1','2','4'].includes(str)) {
      answer = 1;
    }
    else if (['3','5','6'].includes(str)) {
      answer = 2;
    }
    else {
        var count = 0;
        for(var i; i < n; i = i + 1) {
            var temp = n/i
            if(Number.isInteger(temp*2) && temp >= 3) {
                count += 1;
            }
      }
      answer = count;
    }
    return answer;
}
