import React, { Component } from 'react'
import { Container, Row, Col, Card, Button } from 'react-bootstrap'

class Index extends Component {
    render() {
        return (
            <Container id="accountIndexWrapper">
                <Row>
                    <Col>
                        <h2>Hello David Blyth,</h2>
                        <div>
                            Customer Number: ?
                        </div>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Button variant="primary">Orders</Button>
                        <Button variant="primary">Addresses</Button>
                        <Button variant="primary">Logout</Button>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Card>
                            <Card.Title>Card Title</Card.Title>
                            <Card.Body>
                                <Card.Text>
                                    Some quick example text to build on the card title and make up the bulk of
                                    the card's content.
                                </Card.Text>
                                <Button variant="primary">Go somewhere</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col>
                        <Card>
                            <Card.Title>Card Title</Card.Title>
                            <Card.Body>
                                <Card.Text>
                                    Some quick example text to build on the card title and make up the bulk of
                                    the card's content.
                                </Card.Text>
                                <Button variant="primary">Go somewhere</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col>
                        <Card>
                            <Card.Title>Card Title</Card.Title>
                            <Card.Body>
                                <Card.Text>
                                    Some quick example text to build on the card title and make up the bulk of
                                    the card's content.
                                </Card.Text>
                                <Button variant="primary">Go somewhere</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default Index;