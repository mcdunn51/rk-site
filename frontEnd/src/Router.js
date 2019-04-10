import React from 'react';
import { Route } from 'react-router-dom';

import HomePage from './pages/Home';
import Products from './pages/Products';
import Checkout from './pages/Checkout';
import Cart from './pages/Cart';
import UsefulInformation from './pages/UsefulInformation';
// import Error from './pages/Error';
// import Login from './pages/login'


const Router = () => {
    return (
        <div>
            <Route exact path="/" component={HomePage} />
            <Route path="/products/:id" component={Products} />
            <Route exact path="/checkout" component={Checkout} />
            <Route exact path="/cart" component={Cart} />
            <Route path="/UsefulInformation/:id" component={UsefulInformation} />
            {/* <Route exact path="/login" component={Login} /> */}
            {/* <Route component={Error} /> */}
        </div>
    )
}

export default Router; 
