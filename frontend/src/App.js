import "./App.css";
import React, { Component } from "react";
import Home from "./pages/home";
import Categories from "./pages/Categories";
import Details from "./pages/details";
import UserForm from "./pages/userCreation";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

class App extends Component {
  constructor(props) {
    super();
    this.state = {};
    this.getCookie = this.getCookie.bind(this);
  }

  getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  render() {
    return (
      <div className="App">
        <Router>
          <Switch>
            <Route path="/user/create"><UserForm></UserForm></Route>
            <Route path="/details/:id" children={<Details />} />
            <Route path="/categories">
              <Categories />
            </Route>
            <Route path="/">
              <Home />
            </Route>
          </Switch>
        </Router>
      </div>
    );
  }
}

export default App;
