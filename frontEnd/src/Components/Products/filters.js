import React, {Component} from 'react';
import { Col } from 'react-bootstrap';

class Filters extends Component {
    render () {
    return (
        <Col md={2} id="filters">
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
