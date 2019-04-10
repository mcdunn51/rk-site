import React, { Component } from 'react';
import MainNavBar from './Components/MainNavBar/MainNavBar';
import Footer from './Components/Footer/Footer';
import CopyrightRKW from './Components/Footer/CopyrightRKW';
import Router from './Router';
import Header from './Components/Header/header';
import DeliveryStrapline from './Components/Homepage/deliveryStrapline'
import NewsletterSignUpBar from './Components/Homepage/newsletterSignUpBar';


class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <MainNavBar />
        <DeliveryStrapline/>
        <Router/>
        <NewsletterSignUpBar/>
        <Footer />
        <CopyrightRKW />
      </div>
    );
  }
}

export default App;
