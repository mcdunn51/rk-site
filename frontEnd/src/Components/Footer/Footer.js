import React from 'react';
import { Container, Col, Row } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faInfoCircle, faPhone, faEnvelope } from '@fortawesome/free-solid-svg-icons'
import {faLinkedin, faTwitter, faFacebook} from '@fortawesome/free-brands-svg-icons'


const Footer = () => {
    return (
        <div id="footerContainer">
            <Container>
                <Row>
                    <Col id="column1">
                        <ul>
                            <div class="text-center">
                                <FontAwesomeIcon size="4x" className="icon" id="information" icon={faInfoCircle}/>
                            </div>
                            <h6>USEFUL INFORMATION</h6>
                            <li>About Us</li>
                            <li>Delivery Information</li>
                            <li>Privacy and Cookies Policies</li>
                            <li>Returns and Cancelations Policy</li>
                            <li>Site Terms and Conditions</li>
                            <li>Showroom</li>
                            <li>Trade Account Registration</li>
                        </ul>
                    </Col>
                    <Col id="column2">
                        <ul>
                            <FontAwesomeIcon size="4x" rotation={90} className="icon" id="phone" icon={faPhone}/>
                            <h6 id="callUs">CALL US</h6>
                            <li>0333 220 6070</li>
                            <FontAwesomeIcon size="4x" className="icon" id="email" icon={faEnvelope}/>
                            <h6>Email US</h6>
                            <li>sales@rkwltd.com</li>
                        </ul>
                    </Col>
                    <Col id="column3">
                        <ul>
                            <h6>FOLLOW US ON</h6>
                            <FontAwesomeIcon size="4x" id="linkedIn" className="icon" icon={faLinkedin}/>
                            <FontAwesomeIcon size="4x" id="twitter" className="icon" icon={faTwitter}/>
                            <FontAwesomeIcon size="4x" className="icon" icon={faFacebook}/>
                        </ul>
                    </Col>
                </Row>
            </Container>
        </div>
    )
}

export default Footer;