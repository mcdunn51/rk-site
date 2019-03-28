import React, { Component } from 'react';
import MainNavBar from './Components/MainNavBar/MainNavBar';
import Footer from './Components/Footer/Footer';
import CopyrightRKW from './Components/Footer/CopyrightRKW';
import Router from './Router';



class App extends Component {
  render() {
    return (
      <div className="App">
        <MainNavBar />
        <Router/>
        <Footer />
        <CopyrightRKW/>
      </div>
    );
  }
}

export default App;
