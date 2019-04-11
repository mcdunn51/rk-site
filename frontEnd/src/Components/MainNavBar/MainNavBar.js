import React, { Component } from 'react';
import { Container, Nav, NavDropdown } from 'react-bootstrap';
import { IndexLinkContainer } from 'react-router-bootstrap';
import axios from 'axios';
import { connect } from 'react-redux';

class MainNavbar extends Component {


    componentDidMount() {

        const { loadBrands, loadElectricals, loadHousewares } = this.props

        // get all brand names
        axios({
            method: 'get',
            url: 'http://100.1.253.16:8000/Manufacturer/',
            headers: { 'Authorization': 'Bearer SDhm0d95wxYxnBzeFIEXL2Fbev14GW' },
        })
            .then(res => {
                // console.log(res.data)
                const manufacturerCodes = [];
                res.data.forEach(element => {
                    manufacturerCodes.push(element.manufacturerCode);
                })
                loadBrands(manufacturerCodes)
            })

        // get all electrical options
        axios({
            method: 'get',
            url: 'http://100.1.253.16:8000/IPG/?Electrical_or_Housewares=Electrical'
        })
            .then(res => {
                // console.log(res.data)
                const electricals = [];
                res.data.forEach(element => {
                    electricals.push(element.IPG);
                })
                loadElectricals(electricals)
            })

        // get all Houseware options
        axios({
            method: 'get',
            url: 'http://100.1.253.16:8000/IPG/?Electrical_or_Housewares=Housewares'
        })
            .then(res => {
                // console.log(res.data)
                const housewares = [];
                res.data.forEach(element => {
                    housewares.push(element.IPG);
                })
                loadHousewares(housewares)
            })

    };


    render() {

        const { brands, electricals, housewares } = this.props

        return (
            <Container fluid={true} id="mainNavBar">
                <Container>
                    <Nav>
                        <NavDropdown title="Brands" id="nav-dropdown">
                            {
                                brands.map(brand =>
                                    <IndexLinkContainer to={`/products/${brand}`}>
                                        <NavDropdown.Item>{brand}</NavDropdown.Item>
                                    </IndexLinkContainer>
                                )
                            }
                        </NavDropdown>
                        <NavDropdown title="Electricals" id="nav-dropdown">
                            {
                                electricals.map(electrical =>
                                    <IndexLinkContainer to={`/products/${electrical}`}>
                                        <NavDropdown.Item>{electrical}</NavDropdown.Item>
                                    </IndexLinkContainer>
                                )
                            }
                        </NavDropdown>

                        <NavDropdown title="Housewares" id="nav-dropdown">
                            {
                                housewares.map(houseware =>
                                    <IndexLinkContainer to={`/products/${houseware}`}>
                                        <NavDropdown.Item>{houseware}</NavDropdown.Item>
                                    </IndexLinkContainer>
                                )
                            }
                        </NavDropdown>

                        <Nav.Item>
                            <Nav.Link eventKey="3" disabled>
                                NavLink 3 content
                        </Nav.Link>
                        </Nav.Item>

                    </Nav>
                </Container>
            </Container>
        )
    }
}


function mapStateToProps(state) {
    return {
        brands: state.brands,
        electricals: state.electricals,
        housewares: state.housewares
    }
}

function mapDispatchToProps(dispatch) {
    return {
        loadBrands: (brands) => {
            dispatch({ type: 'LOAD_BRANDS', payload: brands })
        },
        loadElectricals: (electricals) => {
            dispatch({ type: 'LOAD_ELECTRICALS', payload: electricals })
        },
        loadHousewares: (housewares) => {
            dispatch({ type: 'LOAD_HOUSEWARES', payload: housewares })
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(MainNavbar);


