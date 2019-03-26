import React from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row' 
import Col from 'react-bootstrap/Col'

const over25years = () => {
    return (
        <Container id="over25years" fluid={true}>
            <Row>
                <Col>
                    <h3>Over <span>25</span> Years in the Business</h3>
                    <p>Europe's leading Electrical and Housewares Distributor</p>
                </Col>
            </Row>
        </Container>
    )
}

export default over25years;