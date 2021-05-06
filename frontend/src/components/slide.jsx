import React, { Component } from "react";
import "../styles/slide.css";

class Slide extends Component {
  constructor(props) {
    super(props);
    this.state = {
      banners: [],
      widthOfImage: this.props.widthimg,
      heightOfImage: this.props.heightimg,
    };
    this.fetchBanners = this.fetchBanners.bind(this);
  }

  componentDidMount() {
    this.fetchBanners();
  }

  fetchBanners = () => {

    fetch("http://127.0.0.1:8000/banner")
      .then((response) => response.json())
      .then((data) =>
        this.setState({
          banners: data,
        })
      );
  };

  render() {
    let banners = this.state.banners;
    return (
      <div className="mainslide" style={{ "--w": this.state.widthOfImage }}>
        <div
          id="carouselExampleIndicators"
          className="carousel slide"
          data-bs-ride="carousel"
        >
          <div className="carousel-indicators">
            {banners.map((banner, index) => {
              if (index === 0) {
                return (
                  <button
                    type="button"
                    key={index}
                    data-bs-target="#carouselExampleIndicators"
                    data-bs-slide-to={index}
                    className="active"
                    aria-current="true"
                    aria-label={"Slide " + (index + 1)}
                  ></button>
                );
              } else {
                return (
                  <button
                    key={index}
                    type="button"
                    data-bs-target="#carouselExampleIndicators"
                    data-bs-slide-to={index}
                    aria-label={"Slide " + (index + 1)}
                  ></button>
                );
              }
            })}
          </div>
          <div className="carousel-inner">
            {banners.map((banner, index) => {
              if (index === 0) {
                return (
                  <div className="carousel-item active" key={index}>
                    <img
                      style={{ "--h": this.state.heightOfImage }}
                      src={"http://127.0.0.1:8000" + banner.Image}
                      className="d-block w-100 slideimage"
                      alt={banner.Name}
                    />
                  </div>
                );
              } else {
                return (
                  <div className="carousel-item" key={index}>
                    <img
                      style={{ "--h": this.state.heightOfImage }}
                      src={"http://127.0.0.1:8000" + banner.Image}
                      className="d-block w-100 slideimage"
                      alt={banner.Name}
                    />
                  </div>
                );
              }
            })}
          </div>
          <button
            className="carousel-control-prev"
            type="button"
            data-bs-target="#carouselExampleIndicators"
            data-bs-slide="prev"
          >
            <span className="carousel-control-prev-icon" aria-hidden="true"></span>
            <span className="visually-hidden">Previous</span>
          </button>
          <button
            className="carousel-control-next"
            type="button"
            data-bs-target="#carouselExampleIndicators"
            data-bs-slide="next"
          >
            <span className="carousel-control-next-icon" aria-hidden="true"></span>
            <span className="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    );
  }
}

export default Slide;
