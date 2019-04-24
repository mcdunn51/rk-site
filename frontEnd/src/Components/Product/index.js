import React, { Component } from 'react';
import Slider from 'react-slick';
import { Container, Row, Col, Form, Button, Tabs, Tab } from 'react-bootstrap';
import { connect } from 'react-redux';
import axios from 'axios'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCircle } from '@fortawesome/free-regular-svg-icons'

class Index extends Component {

    getDetailedProductInfo() {
        const { loadDetailedProduct } = this.props

        axios({
            method: 'get',
            url: `http://100.1.253.16:8000/OProdDetailed/?itemno=${this.props.id}`,
            headers: { 'Authorization': 'Bearer Bymg0PGzTYP8x4r9trJiC0V5fyAT5V' },
        })
            .then(res => {
                console.log(res.data[0])
                loadDetailedProduct(res.data[0])
            })
    }


    componentDidMount() {
        this.getDetailedProductInfo()
    }

    componentDidUpdate(prevProps) {
        if (this.props.id !== prevProps.id) {
            this.getDetailedProductInfo()
        }
    }



    render() {

        const { productDetailed, addToCart } = this.props

        // const settingsSliderMainImage = {
        //     slidesToShow: 1,
        //     slidesToScroll: 1,
        //     arrows: false,
        //     fade: true,
        //     asNavFor: '.slider-nav'
        
        // }
        
        // const settingsSliderNav = {
        
        //     slidesToShow: 3,
        //     slidesToScroll: 1,
        //     asNavFor: '.slider-for',
        //     dots: true,
        //     centerMode: true,
        //     focusOnSelect: true
        
        // }

        return (

            <Container id="productContainer">
                <Row className="mb-5">

                    <Col md={5}>
                        {/* <Slider {...settingsSliderMainImage}/>
                        <div>
                            <h1>1</h1>
                        </div>
                        <div>
                            <h1>2</h1>
                        </div>
                        <div>
                            <h1>3</h1>
                        </div>
                        <div>
                            <h1>4</h1>
                        </div>
                        <div>
                            <h1>5</h1>
                        </div>
                        <div>
                            <h1>6</h1>
                        </div>
                        <div>
                            <h1>7</h1>
                        </div>
                        <div>
                            <h1>8</h1>
                        </div>
                        <div>
                            <h1>9</h1>
                        </div> */}

                        {/* <Slider {...settingsSliderNav}/>
                        <div>
                            <h1>1</h1>
                        </div>
                        <div>
                            <h1>2</h1>
                        </div>
                        <div>
                            <h1>3</h1>
                        </div>
                        <div>
                            <h1>4</h1>
                        </div>
                        <div>
                            <h1>5</h1>
                        </div>
                        <div>
                            <h1>6</h1>
                        </div>
                        <div>
                            <h1>7</h1>
                        </div>
                        <div>
                            <h1>8</h1>
                        </div>
                        <div>
                            <h1>9</h1>
                        </div> */}
                    </Col> 
                    <Col md={7}>

                        <div>
                            <h2>{productDetailed.description}</h2>
                            <p>product code: {productDetailed.itemno}</p>
                            <h3>£??.??</h3>
                            <p>SSP:{productDetailed.SSP}</p>
                            <p>RRP:{productDetailed.RRP}</p>
                        </div>

                        <p>Colours:
                            <span>
                                <FontAwesomeIcon onClick={() => this.changePicAndText('about')} id="colourCircle" icon={faCircle} />
                                <FontAwesomeIcon onClick={() => this.changePicAndText('about')} id="colourCircle" icon={faCircle} />
                                <FontAwesomeIcon onClick={() => this.changePicAndText('about')} id="colourCircle" icon={faCircle} />
                            </span>
                        </p>
                        <Row className="mb-5">
                            <Col>
                                <Form>
                                    <Row>
                                        <Col md={2}>
                                            <Form.Control placeholder="Qty" />
                                        </Col>
                                        <Col md={3}>
                                            <Form.Control as="select">
                                                <option>Pieces</option>
                                                <option>Cartons</option>
                                                <option>Pallets</option>
                                            </Form.Control>
                                        </Col>
                                        <Col md={7}>
                                            <Button variant="primary" type="submit">
                                                Add To Basket
                                        </Button>
                                        </Col>
                                    </Row>
                                </Form>
                            </Col>
                        </Row>

                        <Row id="tabsRow">
                            <Col>
                                <Tabs defaultActiveKey="description" id="uncontrolled-tab-example">
                                    <Tab eventKey="description" title="Product Description">
                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. In quis magna at ante sagittis ultricies sed eget sapien. Proin erat erat, tincidunt vel varius fringilla, placerat eget libero. Donec sit amet sapien dictum, ornare nisi nec, congue quam. Aenean et cursus turpis, ac efficitur ligula. Nullam fringilla feugiat erat, vitae viverra magna eleifend at. Pellentesque accumsan sed quam et elementum. Aliquam eu lacus quis metus hendrerit efficitur. Morbi ut vestibulum magna, vitae auctor metus. Vestibulum nibh sem, condimentum non ipsum id, vulputate venenatis quam. Vestibulum fermentum lorem sed velit accumsan malesuada id vel arcu. Pellentesque faucibus velit eu neque facilisis, id hendrerit ipsum egestas.
                                    </Tab>
                                    <Tab eventKey="specification" title="Product Specification">
                                        {productDetailed.ItemSpec1}
                                    </Tab>
                                    <Tab eventKey="downloads" title="Downloads" disabled>
                                        Ut eu vulputate enim. Aliquam sed molestie mauris. Donec et magna tempor, bibendum mauris pulvinar, lobortis nisl. Donec id commodo urna, bibendum pulvinar libero. Morbi nulla sem, porta tincidunt rhoncus dignissim, tincidunt ac nunc. Duis dapibus ornare dolor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam hendrerit imperdiet lacus, ut iaculis lectus dapibus ut. Vivamus ultricies lobortis risus, in laoreet odio elementum eu. Maecenas ultrices dolor et lorem auctor suscipit. Nam pharetra tellus vitae lectus cursus, eget tempus urna pulvinar. Pellentesque pulvinar eu quam vel sollicitudin. Cras non enim vitae eros venenatis maximus vitae ac sapien. Nam porttitor rutrum risus id iaculis. Cras tincidunt, diam at luctus dignissim, quam ex varius sem, nec ornare ante nisi in ipsum.
                                    </Tab>
                                </Tabs>
                            </Col>
                        </Row>

                    </Col>
                </Row>
                <Row className="mb-5">
                    <Col className="text-center">
                        <h3 className="mb-4">The Collection</h3>
                        <img src="http://placekitten.com/1110/350"/>
                    </Col>
                </Row>


            </Container>
        )
    }
}

function mapStateToProps(state) {
    return {
        productDetailed: state.product
    }
}

function mapDispatchToProps(dispatch) {
    return {
        loadDetailedProduct: (productDetailed) => {
            dispatch({ type: 'LOAD_DETAILED_PRODUCT', payload: productDetailed })
        },
        addToCart: (item) => {
            dispatch({ type: 'ADD_TO_CART', payload: item })
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Index);