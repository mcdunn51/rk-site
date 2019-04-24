import React, { Component } from 'react'
// import SideNavigationBar from '../Components/UsefulInformation/SideNavigationBar'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import { Link } from 'react-router-dom'

import AboutUs from '../Components/UsefulInformation/AboutUs'
import DeliveryInformation from '../Components/UsefulInformation/DeliveryInformation'
import PrivacyAndCookiePolicy from '../Components/UsefulInformation/PrivacyAndCookiePolicy'
import ReturnsAndCancellationPolicy from '../Components/UsefulInformation/ReturnsAndCancellationPolicy'
import Showroom from '../Components/UsefulInformation/Showroom'
import SiteTermsAndConditions from '../Components/UsefulInformation/SiteTermsAndConditions'
import TradeAccountRegistration from '../Components/UsefulInformation/TradeAccountRegistration'

class UsefulInformation extends Component {
    constructor(props) {
        super(props);
        this.state = {id : this.props.match.params.id}
    }   

    componentDidUpdate(prevProps, prevState) {
        const id = this.props.match.params.id
        const prevId = prevState.id
        if (id !== prevId) {
            this.setState({id: id})
        }
    }

    

    render() {

        const id = this.state.id
        let heading, text

        if (id === "About Us") {
            heading = <h2>About Us</h2>
            text = <AboutUs/>

        } else if (id === "Delivery Information") {
            heading = <h2>Delivery Information</h2>
            text = <DeliveryInformation/>

        } else if (id === "Privacy & Cookies Policies") {
            heading = <h2>Privacy & Cookies Policies</h2>
            text = <PrivacyAndCookiePolicy/>

        } else if (id === "Returns & Cancelations") {
            heading = <h2>Returns & Cancelations</h2>
            text = <ReturnsAndCancellationPolicy/>

        } else if (id === "SiteTerms & Conditions") {
            heading = <h2>Site Terms & Conditions</h2>
            text = <SiteTermsAndConditions/>

        } else if (id === "Showroom") {
            heading = <h2>Showroom</h2>
            text = <Showroom/>

        } else if (id === "Trade Account Registration") {
            heading = <h2>Trade Account Registration</h2>
            text = <TradeAccountRegistration/>
        }

        
        return (
            <Container id="usefulInformation" className="mb-5">
                <Row>
                    <Col md={2} />
                    <Col md={10}>
                        {heading}
                    </Col>
                </Row>
                <Row id="secondRow">
                    <Col md={2} id="sideNavigationBar" className="d-none d-md-block pr-0">
                        <ul>
                            <li>
                                USEFUL INFORMATION
                            </li>
                            <li>
                                <Link to="/UsefulInformation/About Us">About Us</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/Delivery Information">Delivery Information</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/Privacy & Cookies Policies">Privacy & Cookies Policies</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/Returns & Cancelations">Returns & Cancelations Policy</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/SiteTerms & Conditions">Site Terms & Conditions</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/Showroom">Showroom</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/Trade Account Registration">Trade Account Registration</Link>
                            </li>
                        </ul>
                    </Col>
                        {text}
                </Row>
            </Container>
        )
    }
}

export default UsefulInformation;


