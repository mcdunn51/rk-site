import { createStore, combineReducers} from 'redux';
import { reducer as formReducer } from 'redux-form';
import { brandsReducer, electricalsReducer, housewaresReducer } from './Components/MainNavBar/reducer';
import productsReducer from './Components/Products/reducer';


const rooReducer = combineReducers({
    brands: brandsReducer,
    electricals: electricalsReducer,
    housewares: housewaresReducer,
    products: productsReducer,
    form: formReducer
})

const store = createStore(
    rooReducer, 
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
)

export default store;