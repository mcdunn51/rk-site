import React, { Component } from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import axios from 'axios';
import { connect } from 'react-redux';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPhone } from '@fortawesome/free-solid-svg-icons'

import LoginForm from './loginForm';

class Index extends Component {

    getLogInToken(values) {
        const {storeAccessToken} = this.props;
        let username = values.username
        let pwd = values.pwd
        
        axios({
            method: 'post',
            url: `http://100.1.253.16:8000/o/token/?grant_type=password&username=${username}&password=${pwd}&client_id=3USdTjmnjbcdTeNrdwjeaOlEcVg1n7oFmXHPz2q9&client_secret=QuZg0JK62clUelPFMJs1884zx1g1ZeFPcgPN74W58Z3ZKUrWrUFAaMwoxJ8sdLei5CvTUIvCErNcmIQk4hoRA5w5A3GC1u9Sbe4ctqWrV67SX12mZ8Rxp2hFwVhFXF5M`,
        })
            .then(res => {
               
                let accessToken = res.data.access_token;
                
                if (accessToken) {
                    storeAccessToken(accessToken);
                }
            })
    }

    render() {
        
        return (
            <Container id="login">
                <Row>
                    <Col md={6}>
                        <Card>
                            <Card.Body>
                                <h2>TRADE ACCOUNT</h2>
                                <Card.Title>Sign in</Card.Title>
                                <LoginForm onSubmit={(values) => this.getLogInToken(values)} />
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
                <Row>
                    <Col md={6}>
                        <Row>
                            <Col md={10}>
                                <h3>Don’t have a trade account?</h3>
                                <p>Why not call our Sales Team on 03331234 1234 and we'll be happy to help.</p>
                            </Col>
                            <Col md={2}>
                                <div id="phoneWrapper">
                                    <FontAwesomeIcon size="4x" className="icon" id="phone" icon={faPhone} />
                                </div>
                            </Col>
                        </Row>
                    </Col>
                </Row>
            </Container>
        )
    }
}


function mapDispatchToProps(dispatch) {
    return {
        storeAccessToken: (accessToken) => {
            dispatch({ type: 'STORE_ACCESS_TOKEN', payload: accessToken })
        }
    }
}

export default connect(null, mapDispatchToProps)(Index);

