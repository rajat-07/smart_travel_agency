import axios from 'axios';

const data = axios.get('http://127.0.0.1:8000/tap/city/1').then(({ data }) => {
  console.log(data);
  const hotels =[];
  for(let i=0;i<8;i+=1){
    d={'name':data.hotels[i].Name,

  }+

  }
  export hotels;
});


/* export const hotels = [
  {
    id: 1,
    name: 'Hotel 1',
    img: 'img/hotel-1.jpg',
    price: 10,
    sentiment: 'POSITIVE'
  },
  {
    id: 2,
    name: 'Hotel 2',
    img: 'img/hotel-2.jpg',
    price: 10,
    sentiment: 'NEGATIVE'
  },
  {
    id: 3,
    name: 'Hotel 3',
    img: 'img/hotel-3.jpg',
    price: 8,
    sentiment: 'NEUTRAL'
  },
  {
    id: 4,
    name: 'Hotel 4',
    img: 'img/hotel-4.jpg',
    price: 18,
    sentiment: 'POSITIVE'
  },
  {
    id: 5,
    name: 'Hotel 5',
    img: 'img/hotel-5.jpg',
    price: 24,
    sentiment: 'NEGATIVE'
  },
  {
    id: 6,
    name: 'Hotel 6',
    img: 'img/hotel-9.jpg',
    price: 17,
    sentiment: 'POSITIVE'
  },
  {
    id: 7,
    name: 'Hotel 7',
    img: 'img/hotel-7.jpg',
    price: 30,
    sentiment: 'POSITIVE'
  },
  {
    id: 8,
    name: 'Hotel 8',
    img: 'img/hotel-8.jpg',
    price: 2,
    sentiment: 'NEGATIVE'
  }
];
 */