import React, { Component } from 'react';
/* import { hotels } from './hoteldata'; */

import axios from 'axios';
const hotels = [];
axios.get('http://127.0.0.1:8000/tap/city/1').then(({ data }) => {
  console.log(data);
  for (let i = 0; i < 8; i += 1) {
    const d = {
      id: i,
      name: data.hotels[i].Name,
      img: `img/hotel-${i + 1}.jpg`,
      sentiment: data.hotels[i].Blob,
      desc: data.hotels[i].Description.slice(0, 150) + '...',
      review: data.hotels[i].Reviews.slice(0, 2)
    };
    hotels.push(d);
  }
});

const HotelContext = React.createContext();
// Provider
// Consumer

class HotelProvider extends Component {
  state = {
    hotels: hotels
  };
  render() {
    return (
      <HotelContext.Provider
        value={{
          ...this.state
        }}
      >
        {this.props.children}
      </HotelContext.Provider>
    );
  }
}

const HotelConsumer = HotelContext.Consumer;

export { HotelProvider, HotelConsumer };
