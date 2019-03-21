import React, { Component } from 'react';
import { Navbar, Nav, NavDropdown, Form, FormControl, Button } from 'react-bootstrap';
import { IndexLinkContainer } from 'react-router-bootstrap';
import axios from 'axios';
import { connect } from 'react-redux';

class MainNavbar extends Component {

    // get all brand names
    componentDidMount() {

        const { loadBrands } = this.props

        axios({
            method: 'get',
            url: `http://100.1.253.16:8000/Manufacturer/`,
            headers: { 'Authorization': 'Bearer SDhm0d95wxYxnBzeFIEXL2Fbev14GW' },
        })
            .then(res => {
                const manufacturerCodes = [];
                res.data.forEach(element => {
                    if (element.manufacturerCode.startsWith('s') || element.manufacturerCode.startsWith('S')) {
                        manufacturerCodes.push(element.manufacturerCode);
                    }
                })
                loadBrands(manufacturerCodes)
            })
    };


    render() {
        const { brands } = this.props

        return (
            <Navbar id="MainNavBar" bg="light" expand="lg">
                <Navbar.Brand href="#home">Matt and Mike's Eccomerce Site</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        <IndexLinkContainer to="/">
                            <Nav.Link>Home</Nav.Link>
                        </IndexLinkContainer>

                        <NavDropdown title="Brands" id="basic-nav-dropdown">
                            {
                                brands.map(brand =>
                                    <IndexLinkContainer to={`/products/${brand}`}>
                                        <NavDropdown.Item>{brand}</NavDropdown.Item>
                                    </IndexLinkContainer>
                                )
                            }
                        </NavDropdown>
                        <IndexLinkContainer to="/cart">
                            <Nav.Link>Cart</Nav.Link>
                        </IndexLinkContainer>
                        <IndexLinkContainer to="/checkout">
                            <Nav.Link>Checkout</Nav.Link>
                        </IndexLinkContainer>
                        <IndexLinkContainer to="/login">
                            <Nav.Link>Login</Nav.Link>
                        </IndexLinkContainer>
                    </Nav>
                    <Form inline>
                        <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                        <Button variant="outline-success">Search</Button>
                    </Form>
                </Navbar.Collapse>
            </Navbar>
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


