import React from "react";
import "./App.css";
import hasimoto from "./hasimoto.png";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={hasimoto} className="hasimotoX" alt="hasimoto" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <p>たいせい君が夢になぜか出てくる、、、</p>
        <p>そんなあ、あなたに</p>
      </header>
    </div>
  );
}

export default App;
