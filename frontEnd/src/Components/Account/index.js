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
                                <Card.Title>Card Title</Card.Title>
                                <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
                                <Card.Text>
                                    Some quick example text to build on the card title and make up the bulk of
                                    the card's content.
                                </Card.Text>
                                <Card.Link href="#">Card Link</Card.Link>
                                <Card.Link href="#">Another Link</Card.Link>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default Index;