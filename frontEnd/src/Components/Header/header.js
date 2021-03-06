import React from 'react';
import { Container } from 'react-bootstrap';
import { Row } from 'react-bootstrap';
import { Col } from 'react-bootstrap';
import { Form } from 'react-bootstrap';
import { FormControl } from 'react-bootstrap';
import { Button } from 'react-bootstrap';
import { InputGroup } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars, faSearch, faUser, faShoppingBasket } from '@fortawesome/free-solid-svg-icons';
import { Link } from 'react-router-dom';

import RKWLogo from '../../images/rkwlogo.jpg'

const Header = () => {
    return (
        // mobile & tablet
        <div>
            <Container id="mobileTabletHeader">
                <Row id="firstRow">
                    <Col id="firstCol">
                        <FontAwesomeIcon icon={faBars} />
                    </Col>
                    <Col id="secondCol">
                        <img src={RKWLogo} />
                    </Col>
                    <Col id="thirdCol">
                        <FontAwesomeIcon icon={faUser} />
                        <FontAwesomeIcon icon={faShoppingBasket} />
                    </Col>
                </Row>
                <Row>
                    <Col>
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
                </Row>
            </Container>

            {/* desktop & up */}
            <Container id="desktopHeader">
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
                        <Link to="/">
                            <img src={RKWLogo} />
                        </Link>
                    </Col>
                    <Col id="thirdCol">
                        <Link to="/login">
                            <FontAwesomeIcon icon={faUser} />
                            <p id="loginText">Login/Register</p>
                        </Link>
                        <Link to="/">
                            <FontAwesomeIcon icon={faShoppingBasket} />
                            <p id="basketText">Basket</p>
                        </Link>
                    </Col>
                </Row>
            </Container>
        </div>
    )
}

export default Header;
