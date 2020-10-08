import React, { Fragment } from "react";
import { NavBar } from "./components/exports";
import "bootstrap/dist/css/bootstrap.min.css";
import Button from "react-bootstrap/Button";
import "./App.scss";

function App() {
  return (
    <Fragment>
      <div className="App">
        <button type="button" className="btn btn-primary">
          Botón
        </button>
        <hr />
        <Button>Botón</Button>
      </div>
    </Fragment>
  );
}

export default App;
