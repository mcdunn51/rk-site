import React, { Component } from 'react'
import { Container, Row, Col, Card, Button } from 'react-bootstrap'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPhone, faEnvelope, faMobileAlt } from '@fortawesome/free-solid-svg-icons'

class Index extends Component {
    render() {
        return (
            <Container id="accountIndexWrapper">
                <Row className="mb-5">
                    <Col id="firstCol">
                        <h2>Hello David Blyth,</h2>
                        <div id="customerNumberWrapper">
                            Customer Number: ?
                        </div>
                    </Col>
                </Row>
                <Row className="mb-5">
                    <Col>
                        <Button variant="primary">Orders</Button>
                        <Button variant="primary">Addresses</Button>
                        <Button variant="primary">Logout</Button>
                    </Col>
                </Row>
                <Row className="mb-5">
                    <Col>
                        <Card>
                            <div className="cardTitleWrapper">
                                <Card.Title>Card Title</Card.Title>
                            </div>
                            <Card.Body>
                                <div className="nameWrapper">
                                    Matthew Dunning
                                </div>
                                <Card.Text>
                                    <a href="tel:+44 7526745507">
                                        <FontAwesomeIcon className="icon" icon={faPhone} />
                                        +44 7526745507
                                    </a>
                                </Card.Text>
                                <Card.Text>
                                    <a href="tel:+44 7526745507">
                                        <FontAwesomeIcon className="icon" icon={faMobileAlt} />
                                        +44 7526745507
                                    </a>
                                </Card.Text>
                                <Card.Text>
                                    <a href="mailto:webmaster@example.com">
                                        <FontAwesomeIcon className="icon" icon={faEnvelope} />
                                        webmaster@example.com
                                    </a>
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col>
                        <Card>
                            <div className="cardTitleWrapper">
                                <Card.Title>Card Title</Card.Title>
                            </div>
                            <Card.Body>
                                <div className="nameWrapper">
                                    Matthew Dunning
                                </div>
                                <Card.Text>
                                    <a href="tel:+44 7526745507">
                                        <FontAwesomeIcon className="icon" icon={faPhone} />
                                        +44 7526745507
                                    </a>
                                </Card.Text>
                                <Card.Text>
                                    <a href="tel:+44 7526745507">
                                        <FontAwesomeIcon className="icon" icon={faMobileAlt} />
                                        +44 7526745507
                                    </a>
                                </Card.Text>
                                <Card.Text>
                                    <a href="mailto:webmaster@example.com">
                                        <FontAwesomeIcon className="icon" icon={faEnvelope} />
                                        webmaster@example.com
                                    </a>
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col>
                        <Card>
                            <div className="cardTitleWrapper">
                                <Card.Title>Card Title</Card.Title>
                            </div>
                            <Card.Body>
                                <div className="nameWrapper">
                                    Matthew Dunning
                                </div>
                                <Card.Text>
                                    <a href="tel:+44 7526745507">
                                        <FontAwesomeIcon className="icon" icon={faPhone} />
                                        +44 7526745507
                                    </a>
                                </Card.Text>
                                <Card.Text>
                                    <a href="tel:+44 7526745507">
                                        <FontAwesomeIcon className="icon" icon={faMobileAlt} />
                                        +44 7526745507
                                    </a>
                                </Card.Text>
                                <Card.Text>
                                    <a href="mailto:webmaster@example.com">
                                        <FontAwesomeIcon className="icon" icon={faEnvelope} />
                                        webmaster@example.com
                                    </a>
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
                <Row className="mb-5">
                    <Col>
                        <Card>
                            <div className="cardTitleWrapper">
                                <Card.Title>Card Title</Card.Title>
                            </div>
                            <Card.Body>
                                <div className="nameWrapper">
                                    Matthew Dunning
                                </div>
                                <Card.Text>
                                    <a href="tel:+44 7526745507">
                                        <FontAwesomeIcon className="icon" icon={faPhone} />
                                        +44 7526745507
                                    </a>
                                </Card.Text>
                                <Card.Text>
                                    <a href="tel:+44 7526745507">
                                        <FontAwesomeIcon className="icon" icon={faMobileAlt} />
                                        +44 7526745507
                                    </a>
                                </Card.Text>
                                <Card.Text>
                                    <a href="mailto:webmaster@example.com">
                                        <FontAwesomeIcon className="icon" icon={faEnvelope} />
                                        webmaster@example.com
                                    </a>
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col>
                        <Card>
                            <div className="cardTitleWrapper">
                                <Card.Title>Card Title</Card.Title>
                            </div>
                            <Card.Body>
                                <div className="nameWrapper">
                                    Matthew Dunning
                                </div>
                                <Card.Text>
                                    <a href="tel:+44 7526745507">
                                        <FontAwesomeIcon className="icon" icon={faPhone} />
                                        +44 7526745507
                                    </a>
                                </Card.Text>
                                <Card.Text>
                                    <a href="tel:+44 7526745507">
                                        <FontAwesomeIcon className="icon" icon={faMobileAlt} />
                                        +44 7526745507
                                    </a>
                                </Card.Text>
                                <Card.Text>
                                    <a href="mailto:webmaster@example.com">
                                        <FontAwesomeIcon className="icon" icon={faEnvelope} />
                                        webmaster@example.com
                                    </a>
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col>
                        <Card>
                            <Card.Body>
                                <Card.Title>Need Assistance?</Card.Title>
                                <div id="needAssistanceWrapper">
                                    Why not call our Sales team for any queries or changes on <a href="tel:+44 7526745507">0333 1234 1234</a> and we'll be happy to help.
                                    <p>
                                        <a href="tel:+44 7526745507">
                                            <FontAwesomeIcon className="icon" icon={faPhone} />
                                        </a>
                                    </p>
                                </div>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default Index;