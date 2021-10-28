import React, { Component } from "react";
import Popup from 'reactjs-popup';
import Consent from './Consent';
//import Popup from 'react-popup';
//import moment from "moment";

import "./App.css";
import 'reactjs-popup/dist/index.css';


const PopupExample = () => (
  <Popup trigger={<button> Trigger</button>} position="right center">
    <div>Popup content here !!</div>
  </Popup>
);

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      error: null
    };

  }
  // use comonentDidMount lifecycle method
  componentDidMount() {
    PopupExample();
    console.log("loaded!");
  }

  render() {
    return (
      <div className="App">
        <Consent />
      </div>
    );
  }
}

export default App;
