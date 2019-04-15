import React, { Component } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faMinus, faPlus } from '@fortawesome/free-solid-svg-icons'
// import { Col } from 'react-bootstrap';

class Filters extends Component {
    render() {
        return (
            <form id="filters">
                <div className="filterWrapper">
                    <div>
                        <h3>BRAND</h3>
                        <FontAwesomeIcon icon={faPlus} />
                    </div>
                    <ul class="filtersList">
                        <li><input type="checkbox"></input>red</li>
                        <li><input type="checkbox"></input>green</li>
                        <li><input type="checkbox"></input>blue</li>
                        <li><input type="checkbox"></input>pink</li>
                    </ul>
                </div>
                <div>
                    <h3>PRODUCT CATEGORY</h3>
                    <h3>COLOUR</h3>
                    <h3>PRICE</h3>
                    <h3>MINIMUM AVAILABLE QTY</h3>
                </div>
            </form>
        )
    }
}

export default Filters;
