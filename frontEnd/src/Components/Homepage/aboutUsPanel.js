import React, { Component } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUserCircle, faCheckCircle, faRegistered } from '@fortawesome/free-regular-svg-icons'

import benefitsOfUsImg1 from '../../images/benefitsOfUsImg1.jpg';
import benefitsOfUsImg2 from '../../images/benefitsOfUsImg2.jpg';
import benefitsOfUsImg3 from '../../images/benefitsOfUsImg3.jpg';

const MoreBtn = () => {
    return (
        <Button id="moreBtn" variant="primary">MORE</Button>
    )
}

class AboutUsPanel extends Component {
    constructor(props) {
        super(props);
        this.state = { picTextBtn: 'about' }

        this.changePicAndText = this.changePicAndText.bind(this);
    }

    changePicAndText(value) {
        this.setState(state => ({
            picTextBtn: value
        }));
    }

    render() {

        const value = this.state.picTextBtn;
        let picture, text, btn

        if (value === 'about') {
            picture = benefitsOfUsImg1;
            text = <div id="text">
                <h3>About us</h3>
                <p>We supply trade customers including John Lewis, Tesco,
                Amazon, Very and Wayfair with high volume products
                spanning cookware, houseware, heating, and SDAs, as well
                as selling direct to consumers through our wholly owned
                        and licensed brands.</p>
            </div>;
        } else if (value === 'benefits') {
            picture = benefitsOfUsImg1;
            text = <div id="text">
                <h3>Benefits of us</h3>
                <ul>
                    <li>Dedicated account manager</li>
                    <li>UK-based customer services</li>
                    <li>Real-time stock control</li>
                    <li>Next-day delivery</li>
                    <li>1000’s of quality products in stock</li>
                    <li>Unbeatable trade prices</li>
                </ul>
            </div>;
        }
        else {
            picture = benefitsOfUsImg1;
            text = <div id="text">
                <h3>Trade with us</h3>
                <p>Creating a trade account at RKW Ltd is the quickest and
                easiest way to ensure that you have access to a range of
                high quality products from prestigious housewares and
                electricals brands and are able to take advantage of the
                        services we offer.</p>
            </div>;
        }

        return (
            <Container fluid={true} id="aboutUsPanel">
                <Row>
                    <Col md={6} id="firstCol">
                        <img id="aboutUsImages" src="https://placekitten.com/940/542" />
                        {/* <img id="aboutUsImages" src={picture} /> */}
                    </Col>
                    <Col md={6} id="secondCol">
                        {text}
                        <Row>
                            <Col id="buttonsCol">
                                <FontAwesomeIcon onClick={() => this.changePicAndText('about')} size="4x" id="userCircle" icon={faUserCircle} />
                                <FontAwesomeIcon onClick={() => this.changePicAndText('benefits')} size="4x" id="tick" icon={faCheckCircle} />
                                <FontAwesomeIcon onClick={() => this.changePicAndText('trade')} size="4x" id="handshake" icon={faRegistered} />
                                <MoreBtn />
                            </Col>
                        </Row>
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default AboutUsPanel