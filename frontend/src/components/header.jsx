import React, { Component } from "react";
import "../styles/header.css";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";


class Header extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    return (
      <header>
        <a href="#" className="logo">
          Rshop
        </a>
        <div className="middlesection">
          <ul>
            <li><Link to="/home">Home</Link></li>
            <li><Link to="/categories">Categories</Link> </li>
            <li><Link to="/tags">Tags</Link> </li>
            <li><Link to="/offers">Offers</Link> </li>
            <li><Link to="/faqs">FAQs</Link> </li>
          </ul>
        </div>
        <div className="rightsection">
          <div className="search icon">
            <a href="#search"><svg
              xmlns="http://www.w3.org/2000/svg"
              width="33.12"
              height="33.12"
              viewBox="0 0 33.12 33.12"
            >
              <path
                d="M25.675,21.268a13.1,13.1,0,1,0-4.409,4.406l8.887,8.886,4.407-4.409ZM14.508,22.594a8.08,8.08,0,1,1,8.084-8.076,8.093,8.093,0,0,1-8.084,8.076Z"
                transform="translate(-1.44 -1.44)"
              />
            </svg></a>
          </div>
          <div className="cart icon">
            <a href="#cart"><svg
              xmlns="http://www.w3.org/2000/svg"
              width="36"
              height="34.5"
              viewBox="0 0 36 34.5"
            >
              <path
                d="M15,31.5A1.5,1.5,0,1,1,13.5,30,1.5,1.5,0,0,1,15,31.5Z"
                fill="none"
                stroke="#000"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="3"
              />
              <path
                d="M31.5,31.5A1.5,1.5,0,1,1,30,30,1.5,1.5,0,0,1,31.5,31.5Z"
                fill="none"
                stroke="#000"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="3"
              />
              <path
                d="M1.5,1.5h6l4.02,20.085a3,3,0,0,0,3,2.415H29.1a3,3,0,0,0,3-2.415L34.5,9H9"
                fill="none"
                stroke="#000"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="3"
              />
            </svg></a>
          </div>
          <div className="help icon">
            <a href="#help"><svg
              xmlns="http://www.w3.org/2000/svg"
              width="33"
              height="33"
              viewBox="0 0 33 33"
            >
              <g transform="translate(-1.5 -1.5)">
                <path
                  d="M33,18A15,15,0,1,1,18,3,15,15,0,0,1,33,18Z"
                  fill="none"
                  stroke="#000"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="3"
                />
                <path
                  d="M13.635,13.5A4.5,4.5,0,0,1,22.38,15c0,3-4.5,4.5-4.5,4.5"
                  fill="none"
                  stroke="#000"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="3"
                />
                <path
                  d="M18,25.5h0"
                  fill="none"
                  stroke="#000"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="3"
                />
              </g>
            </svg></a>
          </div>
          <div className="account icon">
            <a href="#account"><svg
              xmlns="http://www.w3.org/2000/svg"
              width="30"
              height="30"
              viewBox="0 0 30 30"
            >
              <path
                d="M18,3A15,15,0,1,0,33,18,15.005,15.005,0,0,0,18,3Zm0,4.5A4.5,4.5,0,1,1,13.5,12,4.494,4.494,0,0,1,18,7.5Zm0,21.3a10.8,10.8,0,0,1-9-4.83c.045-2.985,6-4.62,9-4.62s8.955,1.635,9,4.62a10.8,10.8,0,0,1-9,4.83Z"
                transform="translate(-3 -3)"
              />
                    </svg>
                    </a>
          </div>
        </div>
      </header>
    );
  }
}

export default Header;
