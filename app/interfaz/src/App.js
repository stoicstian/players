import React, { Fragment } from "react";
import { Header, Footer } from "./components/exports";
import "./App.scss";
import { CssBaseline } from "@material-ui/core";

function App() {
  return (
    <Fragment>
      <CssBaseline>
        <div className="App">
          <Header></Header>
          <Footer></Footer>
        </div>
      </CssBaseline>
    </Fragment>
  );
}

export default App;
