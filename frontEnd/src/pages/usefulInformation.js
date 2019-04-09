import React, { Component } from 'react'
// import SideNavigationBar from '../Components/UsefulInformation/SideNavigationBar'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import { Link } from 'react-router-dom'

import AboutUs from '../Components/UsefulInformation/AboutUs'
import ContactUs from '../Components/UsefulInformation/ContactUs'
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
        console.log(this.props.match.params.id)
        if (id !== prevId) {
            this.setState({id: id})
        }
        // console.log(this.props.match.params.id)
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
            heading = <h2>SiteTerms & Conditions</h2>
            text = <SiteTermsAndConditions/>

        } else if (id === "Showroom") {
            heading = <h2>Showroom</h2>
            text = <Showroom/>

        } else if (id === "Trade Account Registration") {
            heading = <h2>Trade Account Registration</h2>
            text = <TradeAccountRegistration/>
        }

        
        return (
            <Container id="usefulInformation">
                <Row>
                    <Col md={3} />
                    <Col md={9}>
                        {heading}
                    </Col>
                </Row>
                <Row>
                    <Col md={3} id="sideNavigationBar">
                        <ul>
                            <li>
                                UsefulInformation
                            </li>
                            <li>
                                <Link to="/UsefulInformation/About Us">About Us</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/Delivery Information">Delivery Information</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/Privacy & Cookies Policies">Privacy and Cookies Policies</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/Returns & Cancelations">Returns and Cancelations Policy</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/SiteTerms & Conditions">Site Terms and Conditions</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/Showroom">Showroom</Link>
                            </li>
                            <li>
                                <Link to="/UsefulInformation/Trade Account Registration">Trade Account Registration</Link>
                            </li>
                        </ul>
                    </Col>
                    <Col md={9} id="textCol">
                        {text}
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default UsefulInformation;


