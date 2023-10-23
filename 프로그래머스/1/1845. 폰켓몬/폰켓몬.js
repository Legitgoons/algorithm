function solution(nums) {
    var answer = 0;
    const sets = [...new Set(nums)]
    if (nums.length/2 < sets.length){
        answer = Math.floor(nums.length/2)
    } else {
        answer = sets.length
    }
    return answer;
}
/**
* 배열 nums 줄테니 N/2마리 선택 방법 중, 가장 많은 종류의 포켓몬 선택 방법을 찾아
* 포켓몬 종류 번호 개수를 return 하셈
*/
