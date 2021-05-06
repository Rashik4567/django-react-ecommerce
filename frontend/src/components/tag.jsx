import react, { Component } from "react";
import "../styles/tags.css";

class Tag extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: this.props.tagname,
      color: this.props.tagcolor,
    };
  }


  render() {
    return (
      <div className="tag" style={{ "--tag-color": this.state.color }}>
        <p className="tagtext"> {this.state.name} </p>
      </div>
    );
  }
}

export default Tag;
