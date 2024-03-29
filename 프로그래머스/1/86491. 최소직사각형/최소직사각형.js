function solution(sizes) {
    let x = 0;
    let y = 0;
    for (size of sizes){
         size.sort((a, b) => a - b);
        x = Math.max(size[0], x);
        y = Math.max(size[1], y);
    }
    return x*y;
}