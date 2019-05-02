import React, { Component } from "react";
import axios from "axios";
import { Container, Row, Col, Card, Button } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPhone, faEnvelope, faMobileAlt } from "@fortawesome/free-solid-svg-icons";
import { connect } from "react-redux";

import Main from './Main'

class Index extends Component {


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

    componentDidUpdate(prevProps) {
        if (this.props.id !== prevProps.id) {
            this.getAccountInfo();
        }
    }



    render() {

        const { account } = this.props;
        console.log(account.customerno)
        return (
            <Container id="accountIndexWrapper">
                <Row className="mb-5">
                    <Col id="firstCol">
                        <h2>Hello David Blyth,</h2>
                        <div id="customerNumberWrapper">Customer Number: {account.customerno}</div>
                    </Col>
                </Row>
                <Row className="mb-5">
                    <Col>
                        <Button variant="primary">Orders</Button>
                        <Button variant="primary">Addresses</Button>
                        <Button variant="primary">Logout</Button>
                    </Col>
                </Row>
            </Container>
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
            dispatch({ type: "LOAD_ACCOUNT_DETAILS", payload: accoutDetails });
        }
    };
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(Index);
