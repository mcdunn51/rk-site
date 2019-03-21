import React from 'react';

import { Container, Col, Row } from 'react-bootstrap';

const Footer = () => {
    return (
        <Container fluid={true} className="mt-5 pt-5 pb-5" id="footerContainer">
            <Row>
                <Col md={{ span: 2, offset: 1 }}>
                    <ul>
                        <h6>Tower</h6>
                        <li>Trade Enquiries</li>
                        <li>Recycling</li>
                        <li>Product Recalls</li>
                        <li>About Us</li>
                    </ul>
                </Col>
                <Col md={2}>
                    <ul>
                        <h6>Support</h6>
                        <li>Privacy Policy</li>
                        <li>Cookie Policy</li>
                        <li>Terms of Use</li>
                        <li>Terms & Conditions</li>
                        <li>Delivery & Returns</li>
                    </ul>
                </Col>
                <Col md={2}>
                    <ul>
                        <h6>Features</h6>
                        <li>Extend Your Warranty</li>
                        <li>Reviwes</li>
                    </ul>
                </Col>
                <Col md={2}>
                    <ul>
                        <h6>Best Sellers</h6>
                        <li>Pressure Cookers</li>
                        <li>Knives</li>
                        <li>Microwaves</li>
                        <li>Mini Ovens</li>
                    </ul>
                </Col>
                <Col md={2}>
                    <ul>
                        <h6>Payments</h6>
                        <li>Pellentesque ac</li>
                        <li>malesuada fames</li>
                        <li>Vivamus</li>
                        <li>Sed suscipit</li>
                    </ul>
                </Col>
            </Row>
        </Container>
    )
}

export default Footer;