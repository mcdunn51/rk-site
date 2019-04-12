import React, {Component} from 'react';
import { Col } from 'react-bootstrap';

class Filters extends Component {
    render () {
    return (
        <Col md={2} id="filters">
        <h3>Filters</h3>
        <h3>Brand</h3>
        <h3>Product Category</h3>
        <h3>Colour</h3>
        <h3>Price</h3>
        <h3>Minimum available qty</h3> 
            <ul id="filtersList">
                <li><input type="checkbox"></input>red</li>
                <li><input type="checkbox"></input>green</li>
                <li><input type="checkbox"></input>blue</li>
                <li><input type="checkbox"></input>pink</li>
            </ul>
        </Col>
    )} 
}

export default Filters;
