import { createStore, combineReducers} from 'redux';
import { reducer as formReducer } from 'redux-form';
import { brandsReducer, electricalsReducer, housewaresReducer } from './Components/MainNavBar/reducer';
import productsReducer from './Components/Products/reducer';
import productDetailedReducer from './Components/Product/reducer';
import loginReducer from './Components/Login/reducer';

const rooReducer = combineReducers({
    brands: brandsReducer,
    electricals: electricalsReducer,
    housewares: housewaresReducer,
    products: productsReducer,
    product: productDetailedReducer,
    form: formReducer,
    accessToken: loginReducer
})

const store = createStore(
    rooReducer, 
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
)

export default store;