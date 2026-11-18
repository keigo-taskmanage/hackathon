import React from "react";
import "./App.css";
import test_image from "./test_image.jpg";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={test_image} className="App-logo2" alt="test_image" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
