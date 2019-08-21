import React from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          href="/graphql"
          target="_blank"
          rel="noopener noreferrer"
        >
          Check out the GraphQL Endpoint!
        </a>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://github.com/BennettDixon/synth"
          target="_blank"
          rel="noopener noreferrer"
        >
          Thanks for using Synth!!!
        </a>
      </header>
    </div>
  );
}

export default App;
