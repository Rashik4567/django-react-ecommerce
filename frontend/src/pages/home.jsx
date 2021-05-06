import React, { Component } from "react";
import "../styles/home.css";
import Header from "../components/header";
import Slide from "../components/slide";
import ProductCard from "../components/productcard";
import Footer from "../components/footer";

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      products: [],
      productCount: 12,
    };
    this.fetchProducts = this.fetchProducts.bind(this);
  }

  componentDidMount() {
    this.fetchProducts();
  }

  fetchProducts = () => {
    let value = this.state.productCount;
    console.log("Fetching product in range: " + value);
    fetch("http://127.0.0.1:8000/products/" + value)
      .then((response) => response.json())
      .then((data) =>
        this.setState({
          products: data,
        })
      );
  };

  handleMoreBtn = async(e) => {
    e.preventDefault();
    let temp = this.state.productCount;
    await this.setState({
      productCount: (temp + 12),
    })
    this.fetchProducts();
  }

  render() {
    let products = this.state.products;
    return (
      <div className="main">
        <Header></Header>
        <Slide widthimg="70%" heightimg="50vh"></Slide>

        <div className="productsection">
          <h3 className="sectiontitle">Explore New Products</h3>
          <div className="products">
            <div className="row">
              {products.map((product, i) => {
                return (
                  <div className="col-sm-3 product" key={i}>
                    <ProductCard
                      imgurl={product.Main_picture}
                      productname={product.Title}
                      reviews={45}
                      rating={5}
                      stock={product.Stock}
                      price={product.Price}
                      tag1={product.Tag1}
                      tag2={product.Tag2}
                      tag3={product.Tag3}
                      productid={product.id}
                    ></ProductCard>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
        <br />
        <br />

<div className="btncontainer">
        <button className="showmorebtn" onClick={this.handleMoreBtn}>Show more</button>
      </div><br />

    <Footer></Footer>

      </div>
    );
  }
}

export default Home;
