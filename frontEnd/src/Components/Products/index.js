import React, { Component } from 'react';
import axios from 'axios';
import { Container, Row, Col, Card } from 'react-bootstrap';
import { connect } from 'react-redux';
import Button from './addToCartBtn';

import CardImage from '../../images/cardImage.jpg';
import Filters from './filters';


class ProductsIndex extends Component {

    componentDidMount() {

        const { loadProducts } = this.props

        axios.get(`http://100.1.253.16:8000/Productlist/?access_token=SDhm0d95wxYxnBzeFIEXL2Fbev14GW&manufacturerCode=${this.props.id}`)
            .then(res => {
                // console.log(res.data);
                loadProducts(res.data);
            })
    }

    render() {

        const { products, addToCart } = this.props

        return (
            <Container fluid={true}>
                <Row>
                    <Col md={1} />
                    <Filters />
                    {products.map(product =>
                        <Col md={2}>
                            <Card className="text-center">
                                <Card.Img variant="top" src={CardImage} />
                                <Card.Body>
                                    <Card.Title>Product id: {product.id}</Card.Title>
                                    <Card.Text>
                                        {product.description}
                                    </Card.Text>
                                    £{product.price}
                                    <Button variant="primary" product={product} addToCart={addToCart}>Add product</Button>
                                </Card.Body>
                            </Card>
                        </Col>,
                        <Col md={1} />
                    )}
                </Row>
            </Container>
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

export default connect(mapStateToProps, mapDispatchToProps)(ProductsIndex);