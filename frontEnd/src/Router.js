import React from 'react';
import { Route } from 'react-router-dom';

import HomePage from './pages/Home';
import Products from './pages/Products';
import Product from './pages/Product';
import Checkout from './pages/Checkout';
import Cart from './pages/Cart';
import UsefulInformation from './pages/UsefulInformation';
import Login from './pages/Login';
import ResetPwd from './pages/resetPwd'
import Account from './pages/Account'

// import Error from './pages/Error';



const Router = () => {
    return (
        <div>
            <Route exact path="/" component={HomePage} />
            <Route path="/products/:id" component={Products} />
            <Route exact path="/checkout" component={Checkout} />
            <Route exact path="/cart" component={Cart} />
            <Route path="/UsefulInformation/:id" component={UsefulInformation} />
            <Route exact path="/login" component={Login} />
            <Route exact path="/pwdreset" component={ResetPwd} />
            <Route path="/product/:id" component={Product} />
            {/* should only be able to see this why logged in */}
            <Route exact path="/account" component={Account} />
            {/* <Route component={Error} /> */}
        </div>
    )
}

export default Router; 
