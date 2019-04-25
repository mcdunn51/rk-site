import React, { Component } from "react";
import Slider from "react-slick";
import {Col} from 'react-bootstrap'

// nine images
// http://images.cdn.rkwltd.com/t11002.jpg
// http://images.cdn.rkwltd.com/t11002_02.jpg
// http://images.cdn.rkwltd.com/t11002_03.jpg
// http://images.cdn.rkwltd.com/t11002_04.jpg
// http://images.cdn.rkwltd.com/t11002_05.jpg
// http://images.cdn.rkwltd.com/t11002.jpg

class ProductSlider extends Component {
    constructor(props) {
        super(props);
        this.state = {
            nav1: null,
            nav2: null
        };
    }

    componentDidMount() {
        this.setState({
            nav1: this.slider1,
            nav2: this.slider2
        });
    }

    render() {
        return (
            <Col md={5} id="sliderWrapper">
                           
                <Slider
                    asNavFor={this.state.nav2}
                    ref={slider => (this.slider1 = slider)}
                    arrows={false}
                >
                    <div>
                        <img id="sliderMainImage" src="http://images.cdn.rkwltd.com/t11002.jpg" />
                    </div>
                    <div>
                        <img id="sliderMainImage" src="http://images.cdn.rkwltd.com/t11002_02.jpg" />
                    </div>
                    <div>
                        <img id="sliderMainImage" src="http://images.cdn.rkwltd.com/t11002_03.jpg" />
                    </div>
                    <div>
                        <img id="sliderMainImage" src=" http://images.cdn.rkwltd.com/t11002_04.jpg" />
                    </div>
                    <div>
                        <img id="sliderMainImage" src="http://images.cdn.rkwltd.com/t11002_05.jpg" />
                    </div>
                    <div>
                        <img id="sliderControlImg" src="http://images.cdn.rkwltd.com/t11002_06.jpg" />
                    </div>
                </Slider>


                <Slider
                    asNavFor={this.state.nav1}
                    ref={slider => (this.slider2 = slider)}
                    slidesToShow={5}
                    slidesToScroll = {1}
                    swipeToSlide={true}
                    focusOnSelect={true}
                    arrows={true}
                    // centerMode = {true}
                >
                    <div>
                        <img id="sliderControlImg" src="http://images.cdn.rkwltd.com/t11002.jpg" />
                    </div>
                    <div>
                        <img id="sliderControlImg" src="http://images.cdn.rkwltd.com/t11002_02.jpg" />
                    </div>
                    <div>
                        <img id="sliderControlImg" src="http://images.cdn.rkwltd.com/t11002_03.jpg" />
                    </div>
                    <div>
                        <img id="sliderControlImg" src=" http://images.cdn.rkwltd.com/t11002_04.jpg" />
                    </div>
                    <div>
                        <img id="sliderControlImg" src="http://images.cdn.rkwltd.com/t11002_05.jpg" />
                    </div>
                    <div>
                        <img id="sliderControlImg" src="http://images.cdn.rkwltd.com/t11002_06.jpg" />
                    </div>
                </Slider>
            </Col>
        )
    }
}

export default ProductSlider;