import React, { Component } from 'react'
import {Row, Col} from 'react-bootstrap'

class FirstRow extends Component {
    render() {
        return (
            <Row className="mb-5">
                <Col id="firstCol">
                    <h2>Hello David Blyth,</h2>
                    <div id="customerNumberWrapper">Customer Number: ?</div>
                </Col>
            </Row>
        )
    }

}

export default FirstRow