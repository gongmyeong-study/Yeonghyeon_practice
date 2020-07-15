/* 프로젝트에 리덕스 적용하기 */
import { combineReducers } from 'redux';
import counter from './counter';
import todos from './todos';

const rootReducer = combineReducers({
  counter,
  todos
});

export default rootReducer;

export type RootState = ReturnType<typeof rootReducer>;