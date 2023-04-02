function solution(n) {
    var temp = n.toString(2);
    var idx = temp.indexOf("11");
    var f_str = temp.slice(0, idx).slice(0, -1);
    temp = temp.slice(idx-1);
    var o_str = temp.replace(/0/g,'');
    var z_str = "0".repeat(temp.length - o_str.length);
    temp = f_str + "1" + z_str + o_str.slice(1);
    var answer = parseInt(temp, 2);
    return answer;
}
