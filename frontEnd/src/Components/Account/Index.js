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
        console.log(this.props.match.params.id)
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

        if (id === "orders") {
            mainContent = <Orders />
        } else if (id === "addresses") {
            mainContent = <Addresses />
        } else {
            mainContent = <Main />
        }



        return (
            <Container id="accountIndexWrapper">
                <FirstRow />
                <Row className="mb-5">
                    <Col>
                        <Link to="/UsefulInformation/main">
                            <Button variant="primary">Main</Button>
                        </Link>
                        <Link to="/UsefulInformation/addresses">
                            <Button variant="primary">Addresses</Button>
                        </Link>
                        <Link to="/UsefulInformation/orders">
                            <Button variant="primary">Orders</Button>
                        </Link>
                        {/* <Link to="/UsefulInformation/About Us">
                            <Button variant="primary">Logout</Button>
                        </Link> */}
                    </Col>
                </Row>
                {mainContent}
            </Container>
        )
    }

}

export default Index;