import React, { Component } from 'react'
import { Container, Row, Col, Button } from 'react-bootstrap'
import { Link } from 'react-router-dom'

import FirstRow from './firstRow'
import Main from './Main'
import Orders from './Orders'
import Addresses from './Addresses'


class Index extends Component {
    constructor(props) {
        super(props);
        this.state = { id: this.props.match.params.id }
    }

    componentDidUpdate(prevProps, prevState) {
        const id = this.props.match.params.id
        const prevId = prevState.id
        if (id !== prevId) {
            this.setState({ id: id })
        }
    }

    render() {

        const id = this.state.id

        let mainContent

        if (id === "About Us") {
            // heading = <h2>About Us</h2>
            // text = <AboutUs/>
            mainContent = </>

        } else if (id === "Delivery Information") {
            heading = <h2>Delivery Information</h2>
            text = <DeliveryInformation/>

        } else if (id === "Privacy & Cookies Policies") {
            heading = <h2>Privacy & Cookies Policies</h2>
            text = <PrivacyAndCookiePolicy/>
        } 



        return (
            <Container id="accountIndexWrapper">
                <FirstRow />
                <Row className="mb-5">
                    <Col>
                        <Link to="/UsefulInformation/About Us">
                            <Button variant="primary">Orders</Button>
                        </Link>
                        <Link to="/UsefulInformation/About Us">
                            <Button variant="primary">Addresses</Button>
                        </Link>
                        <Link to="/UsefulInformation/About Us">
                            <Button variant="primary">Logout</Button>
                        </Link>
                    </Col>
                </Row>
            </Container>
        )
    }

}

export default Index;