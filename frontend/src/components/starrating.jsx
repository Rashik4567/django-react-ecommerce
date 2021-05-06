import react, { Component } from "react";
import { FaStar } from "react-icons/fa";

class StarRating extends Component {
    constructor(props) {
        super(props);
        this.state = {
            size: this.props.size,
            value: this.props.value,
        };
    }

    render() {
        return (
            <div>
                {[...Array(this.state.value)].map((star, i) => {
                    return <FaStar key={i} size={this.state.size} color="#FFF613"></FaStar>
                })}
            </div>
        );
    }
}

export default StarRating;
