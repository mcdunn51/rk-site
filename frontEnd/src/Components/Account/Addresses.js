import React, { Component } from 'react';
import { Row, Col, Card, } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPhone } from "@fortawesome/free-solid-svg-icons";

class Addresses extends Component {
    render() {
        return (
            <div>
                <Row>
                    <Col>
                        <Card className="mb-5">
                            <div className="cardTitleWrapper">
                                <Card.Title>Address 1</Card.Title>
                            </div>
                            <Card.Body>
                                <Card.Text>
                                    <address>
                                        51 Derwent Close,<br/>
                                        Alsager,<br/>
                                        Stoke-On-Trent,<br/>
                                        ST7 2EL
                                    </address>
                                    <a href="tel:+44 7526745507">
                                        <FontAwesomeIcon className="icon" icon={faPhone} />
                                        +44 7526745507
                                    </a>
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col>
                        <Card className="mb-5">
                            <div className="cardTitleWrapper">
                                <Card.Title>Card Title</Card.Title>
                            </div>
                            <Card.Body>
                                <Card.Text>

                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col>
                        <Card className="mb-5">
                            <div className="cardTitleWrapper">
                                <Card.Title>Card Title</Card.Title>
                            </div>
                            <Card.Body>
                                <Card.Text>

                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Card className="mb-5">
                            <div className="cardTitleWrapper">
                                <Card.Title>Card Title</Card.Title>
                            </div>
                            <Card.Body>
                                <Card.Text>

                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col>
                        <Card className="mb-5">
                            <div className="cardTitleWrapper">
                                <Card.Title>Card Title</Card.Title>
                            </div>
                            <Card.Body>
                                <Card.Text>

                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col>
                        <Card className="mb-5">
                            <Card.Body>
                                <Card.Title className="mb-1">Want to change or add an address?</Card.Title>
                                <Row>
                                    <Col id="needAssistanceCol" xs={9}>
                                        Why not call our Sales team for any queries or changes on{" "}
                                        <a href="tel:+44 7526745507">0333 1234 1234</a> and we'll be
                                        happy to help.
                                    </Col>
                                    <Col id="iconCol" xs={3}>
                                        <a id="phoneIcon" href="tel:+44 7526745507">
                                            <FontAwesomeIcon
                                                className="icon"
                                                size={4}
                                                icon={faPhone}
                                            />
                                        </a>
                                    </Col>
                                </Row>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </div>
        )
    }
}
export default Addresses;