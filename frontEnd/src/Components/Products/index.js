import React, { Component } from 'react';
import axios from 'axios';
import { Container, Row, Col, Card, Form } from 'react-bootstrap';
import { connect } from 'react-redux';
import Button from './addToCartBtn';

import CardImage from '../../images/cardImage.jpg';
import Filters from './filters';


class Index extends Component {

    componentDidMount() {

        const { loadProducts } = this.props

        // don't forget to allow for search parameters
        // you need to allow for any combination of top level to third level parameters e.g. electricals, kitchen appliances, kettles

        axios({
            method: 'get',
            url: `http://100.1.253.16:8000/OProductlist/?IPG=${this.props.id}`,
            headers: { 'Authorization': 'Bearer Bymg0PGzTYP8x4r9trJiC0V5fyAT5V' },
        })
            .then(res => {
                console.log(res.data)
                // const products = [];
                // res.data.forEach(product => {
                //     products.push(product);
                // })
                loadProducts(res.data)
            })


    }

    render() {

        const { products, addToCart } = this.props

        return (
            <Container id="productsPageContainer">
                <Row id="firstRow">
                    <Col>
                        <Form.Group controlId="exampleForm.ControlSelect1">
                            <Form.Control as="select">
                                <option>Price: Low - High</option>
                                <option>Price: High - Low</option>
                                <option>Alphabetical</option>
                            </Form.Control>
                        </Form.Group>
                    </Col>
                </Row>
                <Row>
                    <Col md={2} className="d-none">
                        <Filters/>
                    </Col>
                    <Col md={10}>
                        <Row>
                            {products.map(product =>
                                <Col md={4} lg={3}>
                                    <Card className="text-center">
                                        <Card.Img variant="top" src={CardImage} />
                                        <Card.Body>
                                            <Card.Title>{product.description}</Card.Title>
                                            <Card.Text>
                                                SSP: £{product.SSP} RRP: £{product.RRP}
                                            </Card.Text>
                                            <Card.Text>
                                                Your Price: £?
                                    </Card.Text>
                                            <Card.Text>
                                                Colours: ?
                                    </Card.Text>
                                            <Card.Text>
                                                {/* not sure wether to use a form here */}
                                                <input type="number" placeholder="Qty" />(PCS)
                                        <input type="submit" value="Submit" />
                                            </Card.Text>
                                            £{product.price}
                                            <Button variant="primary" product={product} addToCart={addToCart}>Add product</Button>
                                        </Card.Body>
                                    </Card>
                                </Col>
                            )}
                        </Row>
                    </Col>
                </Row>
            </Container >
        )
    }
}

function mapStateToProps(state) {
    return {
        products: state.products
    }
}

function mapDispatchToProps(dispatch) {
    return {
        loadProducts: (products) => {
            dispatch({ type: 'LOAD_PRODUCTS', payload: products })
        },
        addToCart: (item) => {
            dispatch({ type: 'ADD_TO_CART', payload: item })
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Index);