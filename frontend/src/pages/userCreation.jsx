import React, { Component } from "react";
import "../styles/userform.css";

class UserForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      email: "",
      password: "",
      password2: "",
      message: [],
    };
    this.handleUsernameChange = this.handleUsernameChange.bind(this);
    this.handleEmailChange = this.handleEmailChange.bind(this);
    this.handlePasswordChange = this.handlePasswordChange.bind(this);
    this.handlePassword2Change = this.handlePassword2Change.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleUsernameChange = (e) => {
    e.preventDefault();
    let usernametemp = e.target.value;

    this.setState({
      username: usernametemp,
    });
  };

  handleEmailChange = (e) => {
    e.preventDefault();
    let emailtemp = e.target.value;

    this.setState({
      email: emailtemp,
    });
  };

  handlePasswordChange = (e) => {
    e.preventDefault();
    let passwordtemp = e.target.value;

    this.setState({
      password: passwordtemp,
    });
  };

  handlePassword2Change = (e) => {
    e.preventDefault();
    let password2temp = e.target.value;

    this.setState({
      password2: password2temp,
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://127.0.0.1:8000/rest-auth/registration/", {
      method: "POST",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        
          "username": this.state.username,
          "email": this.state.email,
          "password1": this.state.password,
          "password2": this.state.password2
      
      })
    })
      .then((response) => response.json())
      .then((data) => this.setState({
      message: data
    }))



  };

  render() {
    let msgs = this.state.message;
    return (
      <div className="formcreate">
        {console.log(msgs)}
        <form className="usercreateform" onSubmit={this.handleSubmit}>
          <h3>Please create an account</h3>
          <div class="mb-3">
            <label for="exampleInputText1" class="form-label">
              Username
            </label>
            <input
              type="text"
              class="form-control"
              id="exampleInputText1"
              aria-describedby="textHelp"
              placeholder="Username"
              onChange={this.handleUsernameChange}
              required
            />
            <div id="emailHelp" class="form-text">
              <span style={{ color: "red" }}>NOTE: </span> username <b>must</b>{" "}
              be unique. You can use numbers, letters, and symbols.
            </div>
          </div>
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">
              Email
            </label>
            <input
              type="email"
              class="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
              placeholder="Email address"
              onChange={this.handleEmailChange}
              required
            />
          </div>

          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">
              Password
            </label>
            <input
              type="password"
              class="form-control"
              id="exampleInputPassword1"
              placeholder="Password"
              onChange={this.handlePasswordChange}
              required
            />
          </div>
          <div class="mb-3">
            <label for="exampleInputPassword2" class="form-label">
              Password (Re-type)
            </label>
            <input
              type="password"
              class="form-control"
              id="exampleInputPassword2"
              placeholder="Password comfirm"
              onChange={this.handlePassword2Change}
              required
            />
          </div>
          <div className="btnctn">
            <button type="submit" class="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default UserForm;
