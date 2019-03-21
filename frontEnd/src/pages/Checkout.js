import React, { Component } from 'react';
import { Container, Col, Row } from 'react-bootstrap';
import axios from 'axios';


class Checkout extends Component {
    componentDidMount() {
        axios({
            method: 'post',
            url: 'http://100.1.253.16:8000/Address/?access_token=SDhm0d95wxYxnBzeFIEXL2Fbev14GW',
            data: {
                customerID: 1,
                address1: "Sutton House",
                address2: "Berry Hill Road",
                town: "Staffordshire",
                county: "Staffordshire",
                postcode: "ST4 2NL",
                phoneNumber: "01782 838822",
                email: "rkw@rkwltd.com",
                country: "UK",
                city: 'stoke-on-trent'
            }
        })
            .then(res => {
                console.log(res.data);
                // this.setState({ products: res.data });
            })
    }
    render() {
        return (
            <Container>
                <h2>Checkout</h2>
                <Row className="mt-5">
                    <Col md={6} id="checkoutSummary">
                        <Row>
                            <Col md={2}>
                                picture
                            </Col>
                            <Col md={4}>
                                description
                            </Col>
                            <Col md={3}>
                                Qty
                            </Col>
                            <Col md={3}>
                                price
                            </Col>
                        </Row>
                        <Row>
                            <Col md={2}>
                                picture
                            </Col>
                            <Col md={4}>
                                description
                            </Col>
                            <Col md={3}>
                                Qty
                            </Col>
                            <Col md={3}>
                                price
                            </Col>
                        </Row>
                    </Col>
                    <Col md={6} id="addressCol">

                    </Col>
                </Row>
            </Container>
        )
    }

}



export default Checkout;