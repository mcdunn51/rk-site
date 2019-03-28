import React from 'react';

import { Container, Col, Row } from 'react-bootstrap';

const Footer = () => {
    return (
        <Container fluid={true} id="footerContainer">
            <Container>
                <Row>
                    <Col>
                        <ul>
                            <h6>Tower</h6>
                            <li>Trade Enquiries</li>
                            <li>Recycling</li>
                            <li>Product Recalls</li>
                            <li>About Us</li>
                        </ul>
                    </Col>
                    <Col>
                        <ul>
                            <h6>Support</h6>
                            <li>Privacy Policy</li>
                            <li>Cookie Policy</li>
                            <li>Terms of Use</li>
                            <li>Terms & Conditions</li>
                            <li>Delivery & Returns</li>
                        </ul>
                    </Col>
                    <Col>
                        <ul>
                            <h6>Features</h6>
                            <li>Extend Your Warranty</li>
                            <li>Reviwes</li>
                        </ul>
                    </Col>
                </Row>
            </Container>
        </Container>
    )
}

export default Footer;