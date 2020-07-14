/* 1. 액션 type 선언 */

const INCREASE = 'counter/INCREASE' as const;
const DECREASE = 'counter/DECREASE' as const;
const INCREASE_BY = 'counter/INCREASE_BY' as const;
    /*as const는 액션 생성함수로 액션 객체 만들 시에 
    type의 Typescript 타입이 string이 아닌 실제값 가르키게 함.*/

