function solution(bandage, health, attacks) {
    let nowHealth = health; // 현재 체력
    const t = bandage[0]; // 시전 시간
    const x = bandage[1]; // 초당 회복량 
    const y = bandage[2]; // 추가 회복량
    let gap = 0; // 이전 공격과 현재 공격 사이 시간
    
    for (let i = 0; i < attacks.length; i++){
        
        if(i !== 0){
            gap = attacks[i][0] - attacks[i-1][0] - 1
            if (gap < t ){
                nowHealth += x*gap
            } else {
                nowHealth += (x*gap)+(y*Math.floor(gap/t))
            }
            if(health < nowHealth) {
                nowHealth = health; // 최대 체력 넘어가지 않도록
            } 
        }
        
        nowHealth -= attacks[i][1] // 공격!
        console.log(nowHealth)
        if(nowHealth < 1){
            return -1
        } 
    }
    return nowHealth;
}