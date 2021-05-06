import react, { Component } from "react";
import Header from "../components/header";
import { withRouter } from "react-router-dom";
import "../styles/details.css";

class Details extends Component {

  constructor(props) {
    super(props);
    this.state = {
      details: {},
      variations: [],
    };
    this.fetchData = this.fetchData.bind(this);
    this.fetchVariations = this.fetchVariations.bind(this);
  };

    componentDidMount() {
    const id = this.props.match.params.id;
      this.fetchData(id);
      this.fetchVariations(id)

  }

  fetchData(id) {
    console.log("fetching product details...");
    fetch("http://127.0.0.1:8000/product/get/" + id)
    .then((response) => response.json())
    .then((data) => this.setState({
      details: data
    }))
  }


  fetchVariations(pk) {
    console.log("Fetching product variations ...");
    fetch("http://127.0.0.1:8000/variations/" + pk)
      .then((response) => response.json())
      .then((data) => this.setState({
      variations: data
    }))
   }


  render() {
    let product = this.state.details;
    let varitaions = this.state.variations;
    return (
      <div className="maindetails">
        <Header></Header>
        <h2 className="ProductName">{product.Title}</h2>
        <h2 className="ProductPricd">{product.Price}</h2>
        <p className="Productdetails">{product.Description}</p>
        <p className="Productdetails">{product.Description}</p>

        <h2>Variations</h2>
        <ul>
          {varitaions.map(function(varient, i) {
            return (
              <li>{varient.Title }</li>
            );
          })}
        </ul>
      </div>
    )
  }
}

export default withRouter(Details);
