import React, { Component } from 'react';
import { places } from './placedata';

const PlaceContext = React.createContext();
// Provider
// Consumer

class PlaceProvider extends Component{
	state = {
		places : places,
	}
	render(){
		return(
			<PlaceContext.Provider 
				value={{
					...this.state
				}}
			>
				{ this.props.children }
			</PlaceContext.Provider>
		)
	}
}

const PlaceConsumer = PlaceContext.Consumer;

export { PlaceProvider, PlaceConsumer };