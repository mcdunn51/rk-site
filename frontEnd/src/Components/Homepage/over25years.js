import React from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import backgroundImg from '../../images/over25years.jpg'


const background = {
    backgroundImage: `linear-gradient(to bottom, rgba(255,255,255,0.1) 0%,rgba(255,255,255,0.1) 100%), url(${backgroundImg})`,
    width: "100%",
    height: "auto",
}

const over25years = () => {
    return (
        <Container id="over25years" fluid={true}>
            <Row>
                <Col style={background}>
                    <div id="textWrapper">
                        <h3>Over <span>25</span> Years</h3>
                        <h3>in the Business</h3>
                        <p>Europe's leading Electrical and Housewares Distributor</p>
                    </div>
                </Col>
            </Row>
        </Container>
    )
}

export default over25years;