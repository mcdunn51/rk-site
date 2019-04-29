import React, { Component } from "react";
import axios from "axios";
import { Container, Row, Col, Card, Button } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {faPhone, faEnvelope, faMobileAlt} from "@fortawesome/free-solid-svg-icons";
import { connect } from "react-redux";

class Index extends Component {
    getAccountInfo() {
        const { loadAccountDetails } = this.props;

        axios({
            method: "get",
            url: `http://100.1.253.16:8000/OCustomer/?username=<inser username>`,
            // headers: { Authorization: "Bearer Sg41nV4aocWG1swPCQmZRU0iIdDBKo" }
        }).then(res => {
            console.log(res.data);
            loadAccountDetails(res.data);
        });
    }

    componentDidMount() {
        this.getAccountInfo();
    }

    componentDidUpdate(prevProps) {
        if (this.props.id !== prevProps.id) {
            this.getAccountInfo();
        }
    }

    render() {
        return (
            <Container id="accountIndexWrapper">
                <Row className="mb-5">
                    <Col id="firstCol">
                        <h2>Hello David Blyth,</h2>
                        <div id="customerNumberWrapper">Customer Number: ?</div>
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
                                <div className="nameWrapper">Matthew Dunning</div>
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
                                <div className="nameWrapper">Matthew Dunning</div>
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
                                <div className="nameWrapper">Matthew Dunning</div>
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
                                <div className="nameWrapper">Matthew Dunning</div>
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
                                <div className="nameWrapper">Matthew Dunning</div>
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
                                <Card.Title className="mb-1">Need Assistance?</Card.Title>
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
            </Container>
        )
    }
}

function mapStateToProps(state) {
    return {
        // products: state.products,
        // accessToken: state.accessToken
    };
}

function mapDispatchToProps(dispatch) {
    return {
        loadAccountDetails: accoutDetails => {
            dispatch({ type: "LOAD_ACCOUNT_DETAILS", payload: accoutDetails });
        }
    };
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(Index);
