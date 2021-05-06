import React, { Component } from "react";
import StarRating from "./starrating";
import "../styles/productcard.css";
import Tag from "./tag";

class ProductCard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pid: this.props.productid,
      imageurl: this.props.imgurl,
      productname: this.props.productname,
      reviews: this.props.reviews,
      rating: this.props.rating,
      stock: this.props.stock,
      price: this.props.price,
      tags1: this.props.tag1,
      tags2: this.props.tag2,
      tags3: this.props.tag3,
      tags: []
    };
    this.getTagsRow = this.getTagsRow.bind(this);
    this.tagsSet = this.tagsSet.bind(this);
  }

  componentDidMount() {
    this.tagsSet()
  }

  getTagsRow = async() => {

    let tags = []

    if (this.state.tags1) {
      await this.getTag(this.state.tags1).then((e) => tags.push(e))
    }
    if (this.state.tags2) {
      await this.getTag(this.state.tags2).then((e) => tags.push(e))
    }
    if (this.state.tags3) {
      await this.getTag(this.state.tags3).then((e) => tags.push(e))
    }
    return tags;

  }

  tagsSet() {
    this.getTagsRow().then((data) => this.setState({tags:data}))
  }


  async getTag(id) {
    let tag = null;
    await fetch("http://127.0.0.1:8000/tags/" + id)
    .then((response) => response.json())
    .then((data) =>
    tag = data
  )
  return tag;
  }



  render() {

    return (
      <div className="productcardmain">
        <div className="cardbox">
          <div className="cardimage">
            <img
              src={"http://127.0.0.1:8000" + this.state.imageurl}
              alt="Product image"
            />
          </div>
          <div className="productname">
            <p>{this.state.productname}</p>
            {this.state.tags.map(function(data, i) {
              return <Tag tagname={data.Name} tagcolor={data.Color_HEX} key={i}></Tag>
            })}
          </div>

          <div className="rating">
            <StarRating size={30} value={this.state.rating}></StarRating>
            <p className="reviewcount">({this.state.reviews} reviews)</p>
          </div>
          <div className="stock">
            <p>{this.state.stock} left in stock</p>
          </div>
          <div className="bottomcontainer">
            <div className="price">
              <p>{this.state.price}$</p>
            </div>

            <div className="buybtn">
              <a href={"/details/" + this.state.pid}>Details</a>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default ProductCard;
