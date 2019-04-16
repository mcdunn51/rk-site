import React, { Component } from 'react';
import axios from 'axios';
import { Container, Row, Col, Card, Form, Button } from 'react-bootstrap';
import { connect } from 'react-redux';
// import Button from './addToCartBtn';

// import CardImage from '../../images/cardImage.jpg';
import Filters from './filters';


class Index extends Component {

    getProductInfo() {
        const { loadProducts } = this.props

        // don't forget to allow for search parameters
        // you need to allow for any combination of top level to third level parameters e.g. electricals, kitchen appliances, kettles
        // also need to sort this for brands

        axios({
            method: 'get',
            url: `http://100.1.253.16:8000/OProductlist/?IPG=${this.props.id}`,
            headers: { 'Authorization': 'Bearer Bymg0PGzTYP8x4r9trJiC0V5fyAT5V' },
        })
            .then(res => {
                console.log(res)

                // const products = [];
                // res.data.forEach(product => {
                //     products.push(product);
                // })
                loadProducts(res.data)
            })
    }


    componentDidMount() {

        this.getProductInfo()

    }

    componentDidUpdate(prevProps) {
        if (this.props.id !== prevProps.id) {
            this.getProductInfo()
        }
    }




    render() {

        const { products, addToCart } = this.props

        const getImages = (product) => {
                const Images = JSON.parse(product.Image)
                console.log(Images)
                const Image = Images.image
                return (
                    Image
                )
        }

        return (
            <Container id="productsPageContainer">
                <Row id="firstRow">
                    <Col>
                        <Button className="d-md-none">Filters</Button>
                    </Col>
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
                    <Col md={2} className="d-none d-md-block">
                        <Filters />
                    </Col>
                    <Col md={10}>
                        <Row>
                            {products.map(product =>
                                <Col id="cardCol" xs={6} md={4} lg={3}>
                                    <Card className="text-center">
                                        <Card.Img variant="top" src={getImages(product)} />
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
                                            {/* <Card.Text id="noUnderline"> */}
                                            {/* not sure wether to use a form here */}
                                            {/* <input type="number" placeholder="Qty" />(PCS)
                                                <input type="submit" value="Add to basket" /> */}
                                            <form inline={true}>
                                                <div>
                                                    <Form.Control type="number" placeholder="Qty" />
                                                    <Form.Label>pcs</Form.Label>
                                                </div>
                                                <Button id="addToBasketBtn" variant="primary" type="submit">Add</Button>
                                            </form>


                                            {/* </Card.Text> */}
                                        </Card.Body>
                                    </Card>
                                </Col>
                            )}
                        </Row>
                    </Col>
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

export default connect(mapStateToProps, mapDispatchToProps)(Index);