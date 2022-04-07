import logo from './logo.svg';
import './App.css';
import React from 'react';
import * as ReactDOM from 'react-dom';
import {Map} from '@esri/react-arcgis';
import {Scene} from '@esri/react-arcgis';
import {WebMap,WebScene} from '@esri/react-arcgis';
import Campus from './Campus';

function App() {
  ReactDOM.render(
  <Scene />,
  //<WebMap id="78cbdcdadd944abdb46a1473a02e42d3" /> ,
  //<WebScene id="f8aa0c25485a40a1ada1e4b600522681" />,
  document.getElementById('container')
);
}

//export default App; 
export default (props) => (
    <Scene style={{ width: '70vw', height: '90vh' }}
        //mapProperties={{ basemap: 'satellite' }}
        viewProperties={{
            center: [-118.28538,34.0205],
            zoom: 15
        }}>
        <Campus />
    </Scene>
)

