import React from 'react';
import { Container } from 'react-bootstrap';
import { Row } from 'react-bootstrap';
import { Col } from 'react-bootstrap';
import { Form } from 'react-bootstrap';
import { FormControl } from 'react-bootstrap';
import { Button } from 'react-bootstrap';
import { InputGroup } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch, faUser, faShoppingBasket } from '@fortawesome/free-solid-svg-icons';

import RKWLogo from '../../images/rkwlogo.jpg'

const Header = () => {
    return (
            <Container id="header">
                <Row>
                    <Col id="firstCol">
                        <Form>
                            <InputGroup>
                                <FormControl
                                    placeholder="search"
                                    aria-label="Recipient's username"
                                    aria-describedby="basic-addon2"
                                />
                                <InputGroup.Append>
                                    <Button variant="outline-secondary">
                                        <FontAwesomeIcon icon={faSearch} />
                                    </Button>
                                </InputGroup.Append>
                            </InputGroup>
                        </Form>
                    </Col>
                    <Col id="secondCol">
                        <img src={RKWLogo} />
                    </Col>
                    <Col id="thirdCol">
            
                            <FontAwesomeIcon icon={faUser} />
                            <p id="loginText">Login/Register</p>
                            <FontAwesomeIcon icon={faShoppingBasket} />
                            <p id="basketText">Basket</p>
                    
                    </Col>
                </Row>
            </Container>
    )
}

export default Header;
