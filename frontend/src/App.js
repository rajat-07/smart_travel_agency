import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/Navbar';
import Cart from './components/Cart';
import Details from './components/Details';
import Default from './components/Default';
import HotelList from './components/HotelList';
import PlaceList from './components/PlaceList';
import Itinerary from './components/Itinerary';
import Product from './components/Product';

class App extends Component {
  render(){
    return (
      <React.Fragment>
        <Navbar /> 
        <Switch>
          <Route exact path = "/" component = {HotelList}></Route>
          <Route path = "/places" component = {PlaceList}></Route>
          <Route path = "/itinerary" component = {Itinerary}></Route>
          <Route component = {Default}></Route>
        </Switch>
      </React.Fragment>
    );
  }
}

export default App;
