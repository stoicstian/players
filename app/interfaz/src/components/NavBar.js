import React, { Fragment } from "react";
import "./sass/navbar.scss";

function NavBar() {
  return (
    <Fragment>
      <ul className="navbar">
        <li className="navbar navbar__box">
          <a className="navbar navbar__link" href="#home">
            Home
          </a>
        </li>
        <li className="navbar navbar__box">
          <a className="navbar navbar__link" href="#news">
            News
          </a>
        </li>
        <li className="navbar navbar__box">
          <a className="navbar navbar__link" href="#contact">
            Contact
          </a>
        </li>
        <li className="navbar navbar__box">
          <a className="navbar navbar__link" href="about">
            About
          </a>
        </li>
      </ul>
    </Fragment>
  );
}

export default NavBar;
