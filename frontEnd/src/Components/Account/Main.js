import React, { Component } from "react";
import axios from "axios";
import { Row, Col, Card, } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPhone, faEnvelope, faMobileAlt } from "@fortawesome/free-solid-svg-icons";
import { connect } from "react-redux";

class Main extends Component {
    getAccountInfo() {
        const { loadAccountDetails } = this.props;

        axios({
            method: "get",
            url: `http://100.1.253.16:8000/OCustomer/?username=test`,
            headers: { Authorization: "Bearer cxRgNcThHBzefnmcD4mvsqOsKV5Yaf" }
        }).then(res => {
            console.log(res.data);
            loadAccountDetails(res.data[0]);
        });
    }

    componentDidMount() {
        this.getAccountInfo();
    }

    
    render() {

        const { account } = this.props;
        console.log(account.customerno)
        return (
            <div>
                <Row>
                    <Col>
                        <Card className="mb-5">
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
                        <Card className="mb-5">
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
                        <Card className="mb-5">
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
                <Row>
                    <Col>
                        <Card className="mb-5">
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
                        <Card className="mb-5">
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
                        <Card className="mb-5">
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
            </div>
        )
    }
}

function mapStateToProps(state) {
    return {
        account: state.account
    };
}

function mapDispatchToProps(dispatch) {
    return {
        loadAccountDetails: accoutDetails => {
            dispatch({ type: "LOAD_MAIN_ACCOUNT_DETAILS", payload: accoutDetails });
        }
    };
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(Main);
