import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import  'bootstrap/dist/css/bootstrap.min.css'


function App() {
  return (
    <div className="App">
      "farmfarmfarm"
      <div className="App list-group justify-content-center align-items-center mx-auto" style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}}>
        <h1>
          Todo Manager
        </h1>
        <h6>FARM Fast Api React Mongo</h6>
        <input className="form-control titleIn" placeholder="Title"></input>
        <input className="form-control mt-2 desIn" placeholder="Description"></input>
      </div>
    </div>
  );
}

export default App;
