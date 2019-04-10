import React from 'react';
import { Container, Col, Row } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faInfoCircle, faPhone, faEnvelope } from '@fortawesome/free-solid-svg-icons'
import { faLinkedin } from '@fortawesome/free-brands-svg-icons'
import { Link } from 'react-router-dom'


const Footer = () => {
    return (
        <Container id="footerContainer" fluid={true}>
            <Container>
                <Row>
                    <Col id="column1">
                        <ul>
                            <div class="text-center">
                                <FontAwesomeIcon size="4x" className="icon" id="information" icon={faInfoCircle} />
                            </div>
                            <h6>USEFUL INFORMATION</h6>
                            <li className="sideBarLi">
                                <Link to="/UsefulInformation/About Us">About Us</Link>
                            </li>
                            <li className="sideBarLi">
                                <Link to="/UsefulInformation/Delivery Information">Delivery Information</Link>
                            </li>
                            <li className="sideBarLi">
                                <Link to="/UsefulInformation/Privacy & Cookies Policies">Privacy & Cookies Policies</Link>
                            </li>
                            <li className="sideBarLi">
                                <Link to="/UsefulInformation/Returns & Cancelations">Returns & Cancelations Policy</Link>
                            </li>
                            <li className="sideBarLi">
                                <Link to="/UsefulInformation/SiteTerms & Conditions">Site Terms & Conditions</Link>
                            </li>
                            <li className="sideBarLi">
                                <Link to="/UsefulInformation/Showroom">Showroom</Link>
                            </li>
                            <li className="sideBarLi">
                                <Link to="/UsefulInformation/Trade Account Registration">Trade Account Registration</Link>
                            </li>
                            <li className="sideBarLi">
                                <Link to="/UsefulInformation/Contact Us">Contact Us</Link>
                            </li>
                        </ul>
                    </Col>
                    <Col id="column2">
                        <ul>
                            <FontAwesomeIcon size="4x" rotation={90} className="icon" id="phone" icon={faPhone} />
                            <h6 id="callUs">CALL US</h6>
                            <li>0333 220 6070</li>
                            <FontAwesomeIcon size="4x" className="icon" id="email" icon={faEnvelope} />
                            <h6>Email US</h6>
                            <li>sales@rkwltd.com</li>
                        </ul>
                    </Col>
                    <Col xs={12} md={4} id="column3">
                        <ul>
                            <h6>FOLLOW US ON</h6>
                            <FontAwesomeIcon size="4x" id="linkedIn" className="icon" icon={faLinkedin} />
                        </ul>
                    </Col>
                </Row>
            </Container>
        </Container>
    )
}

export default Footer;