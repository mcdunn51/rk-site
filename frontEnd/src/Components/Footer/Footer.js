import React from 'react';
import { Container, Col, Row } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faInfoCircle, faPhone, faEnvelope } from '@fortawesome/free-solid-svg-icons'
import {faLinkedin, faTwitter, faFacebook} from '@fortawesome/free-brands-svg-icons'
import {Link} from 'react-router-dom'


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
                            <li> 
                                <Link to="/UsefulInformation/AboutUs">About Us</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/DeliveryInformation">Delivery Information</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/Privacy&CookiesPolicies">Privacy and Cookies Policies</Link>
                            </li>
                            <li> 
                                <Link to="/UsefulInformation/ReturnsAndCancelations">Returns and Cancelations Policy</Link>
                            </li>
                            <li> 
                                <Link to="/UsefulInformation/SiteTerms&Conditions">Site Terms and Conditions</Link>
                            </li>
                            <li> 
                                <Link to="/UsefulInformation/Showroom">Showroom</Link>
                            </li>
                            <li> 
                                <Link to="/UsefulInformation/TradeAccountRegistration">Trade Account Registration</Link>
                            </li>
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
                    <Col xs={12} md={4} id="column3">
                        <ul>
                            <h6>FOLLOW US ON</h6>
                            <FontAwesomeIcon size="4x" id="linkedIn" className="icon" icon={faLinkedin}/>
                        </ul>
                    </Col>
                </Row>
            </Container>
        </div>
    )
}

export default Footer;