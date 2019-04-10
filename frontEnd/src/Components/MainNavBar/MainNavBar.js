import React, { Component } from 'react';
import { Container, Nav, NavDropdown } from 'react-bootstrap';
import { IndexLinkContainer } from 'react-router-bootstrap';
import axios from 'axios';
import { connect } from 'react-redux';

class MainNavbar extends Component {


    componentDidMount() {

        const { loadBrands } = this.props

        // get all brand names
        axios({
            method: 'get',
            url: 'http://100.1.253.16:8000/Manufacturer/',
            headers: { 'Authorization': 'Bearer SDhm0d95wxYxnBzeFIEXL2Fbev14GW' },
        })
            .then(res => {
                console.log(res.data)
                const manufacturerCodes = [];
                res.data.forEach(element => {
                    manufacturerCodes.push(element.manufacturerCode);
                })
                loadBrands(manufacturerCodes)
            })
    };


    render() {

        const { brands } = this.props

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
                        <Nav.Item>
                            <Nav.Link eventKey="1" href="#/home">
                                NavLink 1 content
                        </Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link eventKey="2" title="Item">
                                NavLink 2 content
                        </Nav.Link>
                        </Nav.Item>
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
        brands: state.brands
    }
}

function mapDispatchToProps(dispatch) {
    return {
        loadBrands: (brands) => {
            dispatch({ type: 'LOAD_BRANDS', payload: brands })
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(MainNavbar);


