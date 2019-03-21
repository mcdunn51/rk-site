import React, { Component } from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import { connect } from 'react-redux';

class Cart extends Component {

    render() {
        // console.log(this.props.cart)
       const { cart } = this.props


        return (
            <Container>
                <Row>
                    <Col md={12}>
                        <h1>Cart</h1>
                        <Row className="mt-5">
                            <Col md={6} id="cartTable">
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
                                        d
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
                    </Col>
                </Row>
            </Container>
        )
    }

}

function mapStateToProps(state) {
    return {
        cart: state.cart,
    }
}


export default connect(mapStateToProps)(Cart);
