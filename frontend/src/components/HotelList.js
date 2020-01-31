import React, { Component } from 'react';
import Hotel from './Hotel';
import Title from './Title';
import { HotelConsumer } from '../hotelcontext';
import styled from 'styled-components';

class HotelList extends Component {
  render() {
    return (
      <React.Fragment>
        <div className="py-5">
          <div className="container">
            <Title name="" title="Hotels in Mumbai" />
            <div className="row">
              <HotelConsumer>
                {value => {
                  return value.hotels.map(hotel => {
                    return <Hotel key={hotel.id} hotel={hotel} />;
                  });
                }}
              </HotelConsumer>
            </div>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default HotelList;
