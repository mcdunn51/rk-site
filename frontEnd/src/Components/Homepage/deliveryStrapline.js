import React from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row' 
import Col from 'react-bootstrap/Col'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faShippingFast } from '@fortawesome/free-solid-svg-icons'

const DeliveryStrapline = () => {
    return (
        <Container id="deliveryStrapline" fluid={true}>
            <Row>
                <Col>
                    <h2><FontAwesomeIcon icon={faShippingFast} flip="horizontal" />Order by 1pm for NEXT DAY DELIVERY</h2> 
                </Col>
            </Row>
        </Container>
    )
}

export default DeliveryStrapline;