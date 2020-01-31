import React, { Component } from 'react';
import Hotel from './Hotel';
import Place from './Place';
import Title from './Title';
import { HotelConsumer } from '../hotelcontext';

class PlaceList extends Component {
  render() {
    return (
      <React.Fragment>
        <div className="py-5">
          <div className="container">
            <Title name="Hotel" title="Reviews" />
            <div className="row">
              <HotelConsumer>
                {value => {
                  return value.hotels.map(place => {
                    return <Place key={place.id} hotel={place} />;
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

export default PlaceList;
