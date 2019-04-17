import React, { Component } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUserCircle, faCheckCircle, faRegistered } from '@fortawesome/free-regular-svg-icons'

import benefitsOfUsImg1 from '../../images/aboutUsBanner/aboutUs.jpg';
import benefitsOfUsImg2 from '../../images/aboutUsBanner/benefits.jpg';
import benefitsOfUsImg3 from '../../images/aboutUsBanner/register.jpg';

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
                <h3>About RKW</h3>
                <p>We supply trade customers including John Lewis, Tesco,
                Amazon, Very and Wayfair with high volume products
                spanning cookware, houseware, heating, and SDAs, as well
                as selling direct to consumers through our wholly owned
                        and licensed brands.</p>
            </div>;
        } else if (value === 'benefits') {
            picture = benefitsOfUsImg2;
            text = <div id="text">
                <h3>Benefits of RKW</h3>
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
            picture = benefitsOfUsImg3;
            text = <div id="text">
                <h3>Trade with RKW</h3>
                <p>Creating a trade account at RKW Ltd is the quickest and
                easiest way to ensure that you have access to a range of
                high quality products from prestigious housewares and
                electricals brands and are able to take advantage of the
                        services we offer.</p>
            </div>;
        }

        return (
            <Container id="aboutUsPanel">
                <Row>
                    <Col lg={6} className="d-none d-lg-block" id="firstCol">
                        {/* <img id="aboutUsImages" src="https://placekitten.com/555/387" /> */}
                        <img id="aboutUsImages" src={picture} />
                    </Col>
                    <Col md={12} lg={6} id="secondCol">
                        <Row>
                            <Col>
                                {text}
                            </Col>
                        </Row>

                        <Row id="secondRow">
                            <Col id="buttonsCol">
                                <FontAwesomeIcon onClick={() => this.changePicAndText('about')} id="userCircle" icon={faUserCircle} />
                                <FontAwesomeIcon onClick={() => this.changePicAndText('benefits')} id="tick" icon={faCheckCircle} />
                                <FontAwesomeIcon onClick={() => this.changePicAndText('trade')} id="handshake" icon={faRegistered} />
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