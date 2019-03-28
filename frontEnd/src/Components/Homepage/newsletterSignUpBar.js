import React from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col';
import InputGroup from 'react-bootstrap/InputGroup'
import FormControl from 'react-bootstrap/FormControl'
import Button from 'react-bootstrap/Button'


const NewsletterSignUpBar = () => {
    return (
        <div id="newsLetterSignUpBar">
            <Container>
                <Row>
                    <Col>
                        <InputGroup className="mt-2 mb-2">
                            <FormControl
                                placeholder="Join our mailing list for exclusive news & offers"
                            />
                            <InputGroup.Append>
                                <Button variant="outline-secondary">SIGN UP</Button>
                            </InputGroup.Append>
                        </InputGroup>
                    </Col>
                </Row>
            </Container>
        </div>
    )
}

export default NewsletterSignUpBar