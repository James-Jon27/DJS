import {
  legacy_createStore as createStore,
  applyMiddleware,
  compose,
  combineReducers,
} from "redux";
import thunk from "redux-thunk";
import sessionReducer from "./session";
import imageReducer from "./image";
import stashReducer from "./stash";
import commentReducer from "./comment";
import labelReducer from "./label";
import searchLabelReducer from "./searchLabel";
import userReducer from "./user";
import favoriteReducer from "./favorites";
import labelImageReducer from "./labelImages";




const rootReducer = combineReducers({
  session: sessionReducer,
  image: imageReducer,
  stash: stashReducer,
  comment: commentReducer,
  label: labelReducer,
  labelMatch: labelImageReducer,
  search_label: searchLabelReducer,
  user: userReducer,
  favorite: favoriteReducer
});

let enhancer;
if (import.meta.env.MODE === "production") {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = (await import("redux-logger")).default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
