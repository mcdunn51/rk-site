// coppied most of this from the login page 
import React from 'react';
import { Container, Row, Col, Card, Form, Button } from 'react-bootstrap';
// import axios from 'axios';

const ResetPwd = () => {

    return (
        <Container id="resetPwd">
            <Row>
                <Col md={6}>
                    <Card>
                        <Card.Body>
                            <Card.Title>Password Reset</Card.Title>
                            <Form>
                                <Form.Group controlId="formBasicEmail">
                                    <Form.Label>Email address</Form.Label>
                                    <Form.Control type="email" placeholder="Enter email" />
                                </Form.Group>
                                <Button variant="primary" type="submit">
                                    SUBMIT
                            </Button>
                            </Form>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
    )
}


export default ResetPwd;

