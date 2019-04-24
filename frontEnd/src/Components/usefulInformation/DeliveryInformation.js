import React from 'react'
import { Row, Col } from 'react-bootstrap'

const DeliveryInformation = () => {
    return (
        <Col md={10} id="deliveryInformation">
            <Row>
                <Col>
                    <p id="firstParagraph">
                        Trade customers can benefit from Drop Shipping and next day delivery when ordering by 2pm
                    </p>
                    <p className="subtitles">
                        Trade Customers
                    </p>
                    <p>
                        Those trade customers who sign up for Drop Ship services can enjoy next-day delivery or choose specific days on which to receive their order. Goods can also be made available for collection
                        by your nominated carrier.
                    </p>
                    <p className="subtitles">
                        Wholesale and retail
                    </p>
                    <p className="mb-4">
                        For wholesale and/or retail outlets, goods can be delivered palletised, in single or multiples, or for smaller orders, delivered by parcel courier. Deliveries can be made 24/7, with advance
                        booking notification, and the option to deliver direct into specic DCs or individual stores.
                    </p>
                    <img src="http://placekitten.com/920/300" />
                </Col>
            </Row>
        </Col>
    )
}

export default DeliveryInformation;